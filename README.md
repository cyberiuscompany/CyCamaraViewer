[![YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@CyberiusCompany)
![GitHub release downloads](https://img.shields.io/github/downloads/CyberiusCompany/Cyberius-Unzip-Cracker/latest/total)
![Versión](https://img.shields.io/badge/versión-1.0.0-blue)
![Sistema](https://img.shields.io/badge/windows-x64-green)
![Sistema](https://img.shields.io/badge/linux-x64-green)
![Licencia](https://img.shields.io/badge/licencia-Privada-red)
![Uso](https://img.shields.io/badge/uso-solo%20legal-important)
![Python](https://img.shields.io/badge/python-3.7%2B-yellow)

# CyCamaraViewer

Este es una herramienta web desarrollada en Python con Flask que permite buscar y clasificar cámaras IP conectadas a Internet usando la API de Shodan. Proporciona filtros avanzados por marca, tecnología, país, tipo de dispositivo, puerto y más. El objetivo es facilitar la auditoría, investigación o visualización de dispositivos accesibles públicamente.

---

<p align="center">
  <img src="icono.png" alt="Banner" width="500"/>
</p

---

## 🎥 Demostración

<p align="center">
  <img src="docs/Demo.gif" width="1200" alt="Demostración de CyberiusUnzipCracker">
</p>

---

## Fotos de Herramienta

<h2 align="center">Foto 1</h2>
<p align="center">
  <img src="Index de la plataforma.png" alt="Foto 1" width="500"/>
</p>

<h2 align="center">Foto 2</h2>
<p align="center">
  <img src="Busqueda Realizada.png" alt="Foto 2" width="500"/>
</p>

<h2 align="center">Foto 3</h2>
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
git clone..........
cd NOMBRE-HERRAMIENTA
python -m venv venv (No es obligatorio este comando)
.\venv\Scripts\activate (No es obligatorio este comando)
pip install -r requirements.txt
python NOMBRE-HERRAMIENTA
```

## ⚙️ 1.2 Instalación básica con clonado 🐧 Linux / macOS

```bash
git clone..........
cd NOMBRE-HERRAMIENTA
python3 -m venv venv (No es obligatorio este comando)
source venv/bin/activate (No es obligatorio este comando)
pip install -r requirements.txt
python3 NOMBRE-HERRAMIENTA
```

## ⚙️ 2 Instalación como si fuese paquete profesional

```bash
git clone..........
cd NOMBRE-HERRAMIENTA
python3 -m venv venv (No es obligatorio este comando)
source venv/bin/activate (No es obligatorio este comando)
pip install -r requirements.txt
pip install .
NOMBRE-HERRAMIENTA
```

