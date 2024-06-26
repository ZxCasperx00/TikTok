from flask import Flask, request, render_template
import requests
import random
from getuseragent import UserAgent

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/boost', methods=['POST'])
def boost():
    ua = UserAgent("ios").Random()
    user = request.form['username']
    link = request.form['link']
    email = f"whisper{random.randint(100000, 999999)}@gmail.com"
    headers = {
        "Host": "api.likesjet.com",
        "content-length": "137",
        "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "user-agent": ua,
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://likesjet.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://likesjet.com/",
        "accept-language": "en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5"
    }
    res = requests.post('https://api.likesjet.com/freeboost/3', json={"link": link, "tiktok_username": user, "email": email}, headers=headers).json()
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    