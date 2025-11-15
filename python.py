from flask import Flask, request, jsonify
import requests
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

app = Flask(__name__)

NEW_API_URL = "https://mengtopup.shop/api/check_payment?md5={md5}"


@app.get("/check!payment")
def check_payment():
    target_url = f"{NEW_API_URL}"

    try:
        response = requests.get(target_url)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.get("/dev")
def dev():
    return jsonify({"dev": "made@by@panha"})


@app.get("/infor")
def infor():
    return jsonify({"infor": "trueid26"})


# Vercel requires `app` to be named `app`
# This line exposes Flask app to Vercel serverless
app = app
