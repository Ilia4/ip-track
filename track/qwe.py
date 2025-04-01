from flask import Flask, request

app = Flask(__name__)

@app.route('/track')
def track():
    ip = request.remote_addr
    print("IP посетителя:", ip)
    return "Спасибо за посещение!"

app.run(host='0.0.0.0', port=80)