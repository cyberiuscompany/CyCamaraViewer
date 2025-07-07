from flask import Flask, render_template, request
import shodan
import json
import requests
from concurrent.futures import ThreadPoolExecutor
import socket

# Leer configuración
with open("config.json") as f:
    config = json.load(f)

SHODAN_API_KEY = config["shodan_api_key"]
api = shodan.Shodan(SHODAN_API_KEY)

app = Flask(__name__)

def check_http_access(ip, port):
    try:
        url = f"http://{ip}:{port}"
        if "/#/" in url:
            return {'url': url, 'accessible': False, 'auth_required': True}

        response = requests.get(url, timeout=4)

        if response.status_code == 401:
            return {'url': url, 'accessible': False, 'auth_required': True}

        elif response.status_code == 200:
            html = response.text.lower()
            patrones_login = [
                "login.asp", "login.html", "user", "password",
                "signin", "form-login", "/#/login", "/#/", "doc/page/login.asp"
            ]
            if any(p in html for p in patrones_login):
                return {'url': url, 'accessible': False, 'auth_required': True}
            else:
                return {'url': url, 'accessible': True, 'auth_required': False}
        else:
            return {'url': url, 'accessible': False, 'auth_required': False}

    except:
        return {'url': f"http://{ip}:{port}", 'accessible': False, 'auth_required': False}

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    error = None
    stats = {
        'total': 0,
        'con_pais': 0,
        'http_accessibles': 0,
        'requieren_login': 0
    }

    if request.method == 'POST':
        query = request.form.get('query')
        try:
            shodan_results = api.search(query, limit=50)
            raw_results = []

            for result in shodan_results['matches']:
                ip = result['ip_str']
                port = result['port']
                org = result.get('org', 'N/A')
                location = result.get('location', {})
                country = location.get('country_name', 'Desconocido')
                city = location.get('city', 'Desconocido')
                lat = location.get('latitude')
                lon = location.get('longitude')

                raw_results.append({
                    'ip': ip,
                    'port': port,
                    'org': org,
                    'country': country,
                    'city': city,
                    'lat': lat,
                    'lon': lon
                })

            with ThreadPoolExecutor(max_workers=10) as executor:
                statuses = list(executor.map(lambda r: check_http_access(r['ip'], r['port']), raw_results))

            for i, result in enumerate(raw_results):
                status = statuses[i]
                result['url'] = status['url']
                result['accessible'] = status['accessible']
                result['auth_required'] = status['auth_required']
                results.append(result)

            stats['total'] = len(results)
            stats['con_pais'] = sum(1 for r in results if r['country'] != 'Desconocido')
            stats['http_accessibles'] = sum(1 for r in results if r['accessible'])
            stats['requieren_login'] = sum(1 for r in results if r['auth_required'])

        except shodan.APIError as e:
            error = f"Error con la API de Shodan: {e}"

    return render_template('index.html', results=results, stats=stats, error=error)

if __name__ == '__main__':
    local_ip = socket.gethostbyname(socket.gethostname())
    print(f"\n✅ CyCamaraViewer iniciado con éxito.")
    print(f"🌐 Acceso local:       http://127.0.0.1")
    print(f"📡 Acceso LAN (IP):    http://{local_ip}\n")
    app.run(host='0.0.0.0', port=80, debug=True)
