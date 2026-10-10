<div align="center">

# 🔐 Password Security Toolkit

### SecureCheck — Password Strength Analyzer

A modern, dark-themed Flask web app that evaluates a **sample password** and explains its strength with a clear, easy-to-read security report.

**Developed by Deepender Kumar**  
*B.Tech (Cyber-Security) · 7th Semester*

[🌐 **Live Demo**](https://password-security-toolkit-pcf2.onrender.com/) · [💻 GitHub Repository](https://github.com/deependerk789/Password-Security-Toolkit)

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Security Analysis](https://img.shields.io/badge/Analysis-zxcvbn-55E6D0?labelColor=101A2B)](https://github.com/dropbox/zxcvbn)
[![License](https://img.shields.io/badge/Project-Educational%20Demo-6C8EFF)](#-security--privacy-first)

</div>

---

## ✨ Overview

SecureCheck is an educational password-security project built with **Python, Flask, HTML, CSS, and JavaScript**. It uses the open-source **zxcvbn** estimator to assess how predictable a sample password may be and turns the result into a visual report.

The project has a two-page flow: enter demo details on the first page, then review the submitted details and password-strength report on the second page. A password visibility toggle lets users show or hide the password in the interface.

> ⚠️ **Demo only:** Do not enter a real password or credentials you use anywhere else. This is not an authentication system or a password manager.

## 🖥️ Screenshots

### 1. Welcome & sample-password form

The first page introduces SecureCheck and collects demo details before analysis.

![SecureCheck home page](screenshots/home.png)

### 2. Password analysis report

The results page displays the strength estimate, guessability estimate, checklist, and practical recommendations. The sample password is masked by default and can be toggled with the eye icon.

![SecureCheck analysis results page](screenshots/results.png)

*Screenshots are illustrative previews of the interface. Use made-up sample data when running the app.*

## 🚀 Features

- **Password strength estimate** — score from 0 to 4 with a readable strength label.
- **Guessability estimate** — shows the model's estimated number of guesses on a logarithmic scale.
- **Security checklist** — reviews length, character variety, and resistance to common patterns.
- **Actionable feedback** — provides suggestions based on the zxcvbn analysis.
- **Two-page interface** — separate input and results screens.
- **Show/hide password control** — password fields are masked by default in the interface.
- **Responsive dark UI** — modern styling designed for desktop and smaller screens.
- **Basic defensive controls** — input validation, request-size limit, security-related response headers, and a health endpoint.
- **Automated tests** — basic route and validation tests are included.

## 🧰 Tech stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Web framework and routes |
| zxcvbn | Password guessability and strength estimation |
| HTML & CSS | Page structure and dark responsive interface |
| JavaScript | Password visibility and small UI interactions |
| pytest | Basic automated tests |
| Gunicorn | Production WSGI server for deployment |

## 📁 Project structure

```text
SecureCheck_Two_Page_Updated/
├── app.py
├── requirements.txt
├── Procfile
├── render.yaml
├── .gitignore
├── README.md
├── templates/
│   ├── index.html
│   └── results.html
├── static/
│   ├── style.css
│   ├── login.js
│   └── result.js
├── screenshots/
│   ├── home.png
│   └── results.png
└── tests/
    └── test_app.py
```

## ⚙️ Run locally on Windows

### Prerequisites

- Python 3.12 or newer (use a currently supported stable release)
- Git
- VS Code or another code editor

### 1. Clone the repository

```powershell
git clone https://github.com/deependerk789/Password-Security-Toolkit.git
cd Password-Security-Toolkit
```

If you already have the project folder, open that folder in VS Code and use its terminal instead.

### 2. Create a virtual environment

```powershell
python -m venv venv
```

Activate it in PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks script activation, you can use this workaround for the **current terminal session only**:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

Alternatively, skip activation and run the virtual environment's Python directly:

```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe app.py
```

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Start the app

```powershell
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

### 5. Run the tests

```powershell
python -m pytest -q
```

## 🔌 API endpoints

### `POST /api/analyze`

Accepts a JSON body containing a sample password and returns a strength estimate, checks, feedback, and a disclaimer. The API response does not include the password itself.

Example request:

```json
{
  "password": "Example-Only-Password-938!"
}
```

Example with `curl`:

```bash
curl -X POST http://127.0.0.1:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"password":"Example-Only-Password-938!"}'
```

### `GET /health`

Returns a simple health status for local checks and hosting health checks.

## ☁️ Deployment

The repository includes `Procfile` and `render.yaml` for a Render deployment setup.

1. Push the project to GitHub.
2. Sign in to [Render](https://render.com/) and create a **Web Service** from this repository.
3. Review the build command: `pip install -r requirements.txt`.
4. Review the start command: `gunicorn app:app --workers 2 --threads 4 --timeout 30`.
5. Deploy and test the generated HTTPS URL using made-up sample passwords only.

Free hosting plans and their limits can change; check the provider's current documentation before deployment. Do not expose Flask's development server or enable debug mode in production.

## 🛡️ Security & privacy first

This project is a learning demo—not a guarantee of security, a breach checker, a password manager, or a real login system.

- **Use sample passwords only.** Never enter a password used for email, banking, social media, work, or any real account.
- The form sends the sample password to the Flask server for analysis. The results page also includes the submitted value in its HTML so the demo can show it with masking. A masked field is not a security boundary.
- The application does not intentionally save submitted details to a database, but hosting infrastructure may process request contents. Review host logging and retention policies before publishing.
- The strength score is an estimate. It cannot protect against phishing, malware, password reuse, account recovery attacks, or a compromised service.
- For a real product, prefer client-side analysis if the password must never leave the browser, add appropriate rate limiting and security testing, and review the full deployment architecture.

## 🗺️ Possible future improvements

- Perform strength analysis entirely in the browser.
- Add accessibility and mobile-device testing.
- Add stronger automated tests and continuous integration.
- Improve deployment hardening and rate limiting.
- Add a privacy-preserving breached-password lookup only if designed and reviewed carefully.

## 👨‍💻 Developer

**Deepender Kumar**  
B.Tech (Cyber-Security), 7th Semester

---

<div align="center">

Built as an educational cybersecurity project. **Learn. Check. Protect.**

</div>
