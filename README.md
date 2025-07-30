![GitHub release downloads](https://img.shields.io/github/downloads/CyberiusCompany/Cyberius-Unzip-Cracker/latest/total)
![Versión](https://img.shields.io/badge/versión-1.0.0-blue)
![Sistema](https://img.shields.io/badge/windows-x64-green)
![Sistema](https://img.shields.io/badge/linux-x64-green)
![Licencia](https://img.shields.io/badge/licencia-Privada-red)
![Uso](https://img.shields.io/badge/uso-solo%20legal-important)
![Python](https://img.shields.io/badge/python-3.7%2B-yellow)
![Tested on](https://img.shields.io/badge/tested%20on-Windows%2010%2F11%20%7C%20Ubuntu%2022.04-blue)

<p align="center">
  <img src="https://flagcdn.com/w40/es.png" alt="Español" title="Español">
  <strong>Español</strong>
  &nbsp;|&nbsp;
  <a href="README.en.md">
    <img src="https://flagcdn.com/w40/us.png" alt="English" title="English">
    <strong>English</strong>
  </a>
  &nbsp;|&nbsp;
  <a href="https://www.youtube.com/watch?v=xvFZjo5PgG0&list=RDxvFZjo5PgG0&start_radio=1&pp=ygUTcmljayByb2xsaW5nIG5vIGFkc6AHAQ%3D%3D">
    <img src="https://flagcdn.com/w40/jp.png" alt="日本語" title="Japanese">
    <strong>日本語</strong>
  </a>
</p>


# CyCamaraViewer

Este es una herramienta web desarrollada en Python con Flask que permite buscar y clasificar cámaras IP conectadas a Internet usando la API de Shodan. Proporciona filtros avanzados por marca, tecnología, país, tipo de dispositivo, puerto y más. El objetivo es facilitar la auditoría, investigación o visualización de dispositivos accesibles públicamente.

🚨 **IMPORTANTE:** 🚨 Importante poner tu API propia de www.shodan.io.
---

<p align="center">
  <img src="icono.png" alt="Banner" width="500"/>
</p

---

## 🎥 Demostración

<p align="center">
  <img src="demo.gif" width="1200" alt="Demostración de CyberiusUnzipCracker">
</p>

---

## Fotos de Herramienta

<h2 align="center">Index principal de la Web</h2>
<p align="center">
  <img src="Index de la plataforma.png" alt="Foto 1" width="500"/>
</p>

<h2 align="center">Realizando una busqueda de camara</h2>
<p align="center">
  <img src="Busqueda Realizada.png" alt="Foto 2" width="500"/>
</p>

<h2 align="center">Resultado de la busqueda realizada</h2>
<p align="center">
  <img src="Resultado de Busqueda.png" alt="Foto 3" width="500"/>
</p>

---

## 🎯 Características

- 🛠 Filtros avanzados por marca, tecnología, puerto, país, tipo de dispositivo, autenticación y UI.
- 📄 Generación automática de consultas en lenguaje natural y para la API de Shodan.
- 📊 Estadísticas en tiempo real: total de dispositivos, accesibles, con login, etc.
- 🌐 Clasificación por accesibilidad: accesibles, requieren login, no accesibles.
- ⚡ Análisis rápido gracias a paralelización con `ThreadPoolExecutor`.
- 🎨 Interfaz moderna con diseño oscuro personalizable (`estilo.css`).
- 📁 Estructura de proyecto limpia, portable y lista para producción.

## 🧰 Tecnologías utilizadas

- 🐍 Python 3 – Lenguaje base del backend.
- 🔥 Flask – Framework ligero para aplicaciones web.
- 🧠 Shodan API – Para búsqueda de dispositivos expuestos en Internet.
- 🎨 HTML5 + CSS3 (estilo.css) – Diseño responsive y visual moderno.
- ⚡ JavaScript (Vanilla) – Lógica para generación dinámica de queries.
- 🔐 Jinja2 – Motor de plantillas para renderizar HTML desde Flask.

## 📁 Estructura del proyecto

```bash
CyCamaraViewer/
├── .github/             # Flujos de trabajo para GitHub Actions
│   └── workflows/
├── static/              # Recursos estáticos (CSS, íconos)
│   ├── cyberius.ico
│   └── estilo.css
├── templates/           # Plantillas HTML (Jinja2)
│   └── index.html
├── app.py               # Lógica principal de Flask
├── config.json          # Archivo de configuración con API Key
├── requirements.txt     # Dependencias del proyecto
├── README.md            # Este archivo
├── LICENCE              # Licencia MIT
└── docs/                # Capturas y documentación adicional
    ├── Busqueda Realizada.png
    ├── Resultado de Busqueda.png
    ├── Index de la plataforma.png
```
---

## 📄 Documentación adicional

- [🤝 Código de Conducta](.github/CODE_OF_CONDUCT.md)
- [📬 Cómo contribuir](.github/CONTRIBUTING.md)
- [🔐 Seguridad](.github/SECURITY.md)
- [⚠️Aviso legal](DISCLAIMER.md)
- [📜 Licencia](LICENSE)
- [📢 Soporte](.github/SUPPORT.md)


---

## ⚙️ 1.1 Instalación básica con clonado 🪟 Windows

```bash
git clone https://github.com/cyberiuscompany/CyCamaraViewer.git
cd CyCamaraViewer
python -m venv venv (No es obligatorio este comando)
.\venv\Scripts\activate (No es obligatorio este comando)
pip install -r requirements.txt
python app.py
```

## ⚙️ 1.2 Instalación básica con clonado 🐧 Linux / macOS

```bash
git clone https://github.com/cyberiuscompany/CyCamaraViewer.git
cd CyCamaraViewer
python3 -m venv venv (No es obligatorio este comando)
source venv/bin/activate (No es obligatorio este comando)
pip install -r requirements.txt
python3 app.py
```

## ⚙️ 2.1 Instalación en un túnel sobre Unix 🪟 (Para que este público en internet)

```bash
# En una primera consola lo siguiente:
git clone https://github.com/cyberiuscompany/CyCamaraViewer.git
cd CyCamaraViewer
python -m venv venv (No es obligatorio este comando)
.\venv\Scripts\activate (No es obligatorio este comando)
pip install -r requirements.txt
python3 app.py

# En una segunda consola lo siguiente:
Descarga: https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe 
Renombralo como:  cloudflared.exe
cloudflared.exe --version
cloudflared.exe tunnel --url http://localhost:80
```

## ⚙️ 2.1 Instalación en un túnel sobre Unix 🐧 (Para que este público en internet)

```bash
# En una primera consola lo siguiente:
git clone https://github.com/cyberiuscompany/CyCamaraViewer.git
cd CyCamaraViewer
python3 -m venv venv (No es obligatorio este comando)
source venv/bin/activate (No es obligatorio este comando)
pip install -r requirements.txt
python3 app.py

# En una segunda consola lo siguiente:
Descarga: wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 
Renombralo como:  cloudflared
cloudflared --version
cloudflared tunnel --url http://localhost:80
```
