from flask import Flask, request, render_template, jsonify
import requests
import time
import os
from dotenv import load_dotenv
from functools import wraps

load_dotenv()

QUOTE_URL = os.getenv("QUOTE_URL","www.google.com")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL","https://discord.com/api/webhooks/123456789/qweasdzxc")

CACHE_TTL=5
API_KEYS = ["qwe","asd"]

_last_quote=None
_last_quote_time=0

app = Flask(__name__)   

def check_api_key(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = request.headers.get("X-API-Key")
        
        if not key or key not in API_KEYS:
            return jsonify({"erro":"Unauthorized: Invalid or missing api key"}),401
        
        return func(*args, **kwargs)
    return wrapper

@app.route("/quote",methods=["GET"])
@check_api_key
def index():  

    global _last_quote, _last_quote_time

    # checa se deveriamos usar o cache
    if _last_quote and (time.time()-_last_quote_time) < CACHE_TTL:
        app.logger.info(f"Returning cached quote")
        return render_template( "quote.html", quote=_last_quote)

    try:
        response = requests.get(f"{QUOTE_URL}/random", verify=False, timeout=5)
        
        if response.status_code == 200:
            quote_data = response.json()
            _last_quote = quote_data
            _last_quote_time = time.time()
            return render_template( "quote.html",quote=quote_data)
        else:
            return jsonify({"error":"The API is not working"}),503
        
    except requests.exceptions.RequestException as e:
        app.logger.info(f"Request failed : {e}")
        if _last_quote:
            app.logger.info("Using last quote")
            return render_template( "quote.html",quote=_last_quote)
        else:
            app.logger.info("Couldn't find any quotes")
            return render_template("quote.html",quote={"author":"Nobody","content":"Trust the process"})

@app.route("/notify",methods=["POST"])
@check_api_key
def notify():
    data = request.get_json()
    
    if not data and "content" not in data:
        return f"There is no content in the message"
    
    content = data.get("content")
    user = "codigo python"

    new_data = {
        "content": content,
        "user": user
    }

    try:
        resp = requests.post(DISCORD_WEBHOOK_URL,new_data,timeout=5)

        if resp.status_code == 204:
            return jsonify({"status":"message was sent to dicord"}),200
        else:
            app.logger.error(f"Discord error: {resp.status_code}, {resp.text}")
            return jsonify({"error":"failed to send messsage to discord"}),502

    except requests.exceptions.RequestException as e:
        app.logger.error(f"Request Failed: {e}")
        return jsonify({"error": "network error"}),503

@app.route("/helthy")
def healthy():
    return jsonify({"Status":"The server is running healthy"}),200

if __name__=="__main__":
    app.run(port=5050, debug=True)