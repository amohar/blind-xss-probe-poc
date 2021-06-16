from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

IP_ADDRESS = 'IP_ADDRESS'

@app.route("/store/<value>")
def hello_world(value):
    try:
        with open('results.txt', 'a') as fp:
            now = datetime.now()
            fp.write(f"[{now.strftime('%d.%m.%Y. %H:%M:%S')}][{request.remote_addr}] {value}\n")
            return { 'result': 'ok' }
    except:
        return { 'result': 'error' }
if __name__ == '__main__':
    app.run(host=IP_ADDRESS)
