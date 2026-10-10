import logging, os
from flask import Flask, render_template, request, jsonify
from zxcvbn import zxcvbn

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024
logging.getLogger("werkzeug").setLevel(logging.WARNING)

@app.after_request
def headers(r):
    r.headers.update({
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",
        "Referrer-Policy": "no-referrer",
        "Cache-Control": "no-store",
        "Content-Security-Policy": "default-src 'self'; style-src 'self'; script-src 'self'; base-uri 'self'; form-action 'self'; frame-ancestors 'none'"
    })
    return r

def analyze(password):
    z = zxcvbn(password)
    score = z["score"]
    fb = z.get("feedback", {})
    tips = list(fb.get("suggestions") or [])
    if fb.get("warning"):
        tips.insert(0, fb["warning"])
    checks = [
        {"label": "At least 12 characters", "passed": len(password) >= 12},
        {"label": "At least 16 characters (recommended)", "passed": len(password) >= 16},
        {"label": "Uppercase and lowercase letters", "passed": any(c.isupper() for c in password) and any(c.islower() for c in password)},
        {"label": "Contains a number", "passed": any(c.isdigit() for c in password)},
        {"label": "Contains a symbol", "passed": any(not c.isalnum() and not c.isspace() for c in password)},
        {"label": "Resists common or easily guessed patterns", "passed": score >= 3},
    ]
    return {
        "score": score,
        "label": ["Very weak", "Weak", "Fair", "Strong", "Very strong"][score],
        "guesses_log10": round(float(z.get("guesses_log10", 0)), 2),
        "feedback": tips[:6],
        "checks": checks,
        "passed_count": sum(c["passed"] for c in checks),
        "disclaimer": "This is an estimate, not a guarantee. Use unique passwords, a password manager, and multi-factor authentication."
    }

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/analyze")
def analyze_form():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")
    error = None
    if not name or len(name) > 80:
        error = "Please enter your name (up to 80 characters)."
    elif not email or len(email) > 254 or "@" not in email:
        error = "Please enter a valid email address."
    elif not password:
        error = "Enter a sample password to analyze."
    elif len(password) > 256:
        error = "Password must be 256 characters or fewer."
    if error:
        return render_template("index.html", error=error), 400

    # Demo only: no real authentication or persistence. Password is passed to the
    # result template solely because this demo explicitly displays it with masking.
    return render_template("results.html", name=name, email=email, password=password, result=analyze(password))

@app.post("/api/analyze")
def analyze_api():
    if not request.is_json:
        return jsonify(error="Send a JSON request."), 415
    data = request.get_json(silent=True)
    password = data.get("password") if isinstance(data, dict) else None
    if not isinstance(password, str) or not password:
        return jsonify(error="Password must be a non-empty string."), 400
    if len(password) > 256:
        return jsonify(error="Password must be 256 characters or fewer."), 400
    return jsonify(analyze(password))

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.errorhandler(413)
def too_large(_):
    return jsonify(error="Request is too large."), 413

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", 5000)), debug=False)
