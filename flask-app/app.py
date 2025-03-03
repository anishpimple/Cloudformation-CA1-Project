from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>WELL DONEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE!!!!!!!!!!!!!!!!!!!!!!\n\n NEWWW</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

