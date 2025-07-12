[![YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@CyberiusCompany)
![GitHub release downloads](https://img.shields.io/github/downloads/CyberiusCompany/Cyberius-Unzip-Cracker/latest/total)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![System](https://img.shields.io/badge/windows-x64-green)
![System](https://img.shields.io/badge/linux-x64-green)
![License](https://img.shields.io/badge/license-Private-red)
![Usage](https://img.shields.io/badge/usage-legal%20only-important)
![Python](https://img.shields.io/badge/python-3.7%2B-yellow)

<p align="center">
  <a href="https://github.com/cyberiuscompany/CyCamaraViewer">
    <img src="https://flagcdn.com/w40/es.png" alt="Español" title="Español">
    <strong>Español</strong>
  </a>
  &nbsp;|&nbsp;
  <img src="https://flagcdn.com/w40/us.png" alt="English" title="English">
  <strong>English</strong>
  &nbsp;|&nbsp;
  <a href="https://www.youtube.com/watch?v=xvFZjo5PgG0&list=RDxvFZjo5PgG0&start_radio=1&pp=ygUTcmljayByb2xsaW5nIG5vIGFkc6AHAQ%3D%3D">
    <img src="https://flagcdn.com/w40/jp.png" alt="Japanese" title="Japanese">
    <strong>日本語</strong>
  </a>
</p>

# CyCamaraViewer

This is a web tool developed in Python with Flask that allows searching and classifying IP cameras connected to the Internet using the Shodan API. It provides advanced filters by brand, technology, country, device type, port, and more. The goal is to facilitate auditing, investigation, or visualization of publicly accessible devices.

---

<p align="center">
  <img src="icono.png" alt="Banner" width="500"/>
</p>

---

## 🎥 Demonstration

<p align="center">
  <img src="demo.gif" width="1200" alt="CyCamaraViewer Demonstration">
</p>

---

## Tool Screenshots

<h2 align="center">Main Index of the Web</h2>
<p align="center">
  <img src="Index de la plataforma.png" alt="Screenshot 1" width="500"/>
</p>

<h2 align="center">Performing a Camera Search</h2>
<p align="center">
  <img src="Busqueda Realizada.png" alt="Screenshot 2" width="500"/>
</p>

<h2 align="center">Search Result Display</h2>
<p align="center">
  <img src="Resultado de Busqueda.png" alt="Screenshot 3" width="500"/>
</p>

---

## 🎯 Features

- 🛠 Advanced filters by brand, technology, port, country, device type, authentication, and UI.
- 📄 Automatic generation of natural language and Shodan API queries.
- 📊 Real-time statistics: total devices, accessible, login required, etc.
- 🌐 Classification by accessibility: accessible, requires login, not accessible.
- ⚡ Fast analysis thanks to `ThreadPoolExecutor` parallelization.
- 🎨 Modern interface with customizable dark theme (`estilo.css`).
- 📁 Clean, portable, and production-ready project structure.

## 🧰 Technologies Used

- 🐍 Python 3 – Backend base language.
- 🔥 Flask – Lightweight web application framework.
- 🧠 Shodan API – For searching Internet-exposed devices.
- 🎨 HTML5 + CSS3 (estilo.css) – Responsive and modern design.
- ⚡ Vanilla JavaScript – Logic for dynamic query generation.
- 🔐 Jinja2 – Template engine for rendering HTML from Flask.

## 📁 Project Structure

```bash
CyCamaraViewer/
├── .github/             # GitHub Actions workflows
│   └── workflows/
├── static/              # Static resources (CSS, icons)
│   ├── cyberius.ico
│   └── estilo.css
├── templates/           # HTML templates (Jinja2)
│   └── index.html
├── app.py               # Main Flask logic
├── config.json          # Configuration file with API Key
├── requirements.txt     # Project dependencies
├── README.md            # This file
├── LICENCE              # MIT License
└── docs/                # Screenshots and additional documentation
    ├── Busqueda Realizada.png
    ├── Resultado de Busqueda.png
    ├── Index de la plataforma.png
```

---

## 📄 Additional Documentation

- [🤝 Code of Conduct](.github/CODE_OF_CONDUCT.md)
- [📬 How to Contribute](.github/CONTRIBUTING.md)
- [🔐 Security](.github/SECURITY.md)
- [⚠️ Legal Notice](DISCLAIMER.md)
- [📜 License](LICENSE)
- [📢 Support](.github/SUPPORT.md)

---

## ⚙️ 1.1 Basic Installation via Clone 🪟 Windows

```bash
git clone https://github.com/cyberiuscompany/CyCamaraViewer.git
cd CyCamaraViewer
python -m venv venv (Optional)
.env\Scriptsctivate (Optional)
pip install -r requirements.txt
python app.py
```

## ⚙️ 1.2 Basic Installation via Clone 🐧 Linux / macOS

```bash
git clone https://github.com/cyberiuscompany/CyCamaraViewer.git
cd CyCamaraViewer
python3 -m venv venv (Optional)
source venv/bin/activate (Optional)
pip install -r requirements.txt
python3 app.py
```

## ⚙️ 2.1 Public Tunnel Setup on 🪟 Windows

```bash
# In the first terminal:
git clone https://github.com/cyberiuscompany/CyCamaraViewer.git
cd CyCamaraViewer
python -m venv venv (Optional)
.\venv\Scripts\activate (Optional)
pip install -r requirements.txt
python3 app.py

# In a second terminal:
Download: https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe 
Rename to: cloudflared.exe
cloudflared.exe --version
cloudflared.exe tunnel --url http://localhost:80
```

## ⚙️ 2.1 Public Tunnel Setup on 🐧 Linux

```bash
# In the first terminal:
git clone https://github.com/cyberiuscompany/CyCamaraViewer.git
cd CyCamaraViewer
python3 -m venv venv (Optional)
source venv/bin/activate (Optional)
pip install -r requirements.txt
python3 app.py

# In a second terminal:
Download: wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 
Rename to: cloudflared
cloudflared --version
cloudflared tunnel --url http://localhost:80
```
