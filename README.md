
# Streamlit SaaS Dashboard (Excel + Gmail)

This full-stack SaaS dashboard supports:
- User login via `streamlit-authenticator`
- Excel file upload, filtering, export
- Emailing filtered data via Gmail
- PostgreSQL-ready backend (optional)
- Dockerized deployment
- Light custom UI theme

## 🚀 Features
- Secure login system
- Upload `.xlsx`, filter columns
- Download filtered data as Excel
- Email attachment via Gmail (App Passwords)
- CI-ready via GitHub Actions

---

## 🖥️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🐳 Docker Usage

```bash
docker build -t streamlit-saas .
docker run -p 8501:8501 streamlit-saas
```

---

## 🌐 GitHub Pages / DOM Cloud / Fly.io

1. Upload repo to GitHub
2. For DOM Cloud: configure Python project and paste run command
3. For Fly.io:
   ```bash
   flyctl launch
   flyctl deploy
   ```

---

## ✉️ Gmail Integration

Generate App Password from: https://myaccount.google.com/apppasswords  
Use that password in the app for Gmail login.

---

## 🎨 UI Custom Theme

Edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#3466af"
backgroundColor = "#f7f9fc"
secondaryBackgroundColor = "#e3eaf2"
textColor = "#262730"
```
