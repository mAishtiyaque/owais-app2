from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to owais web world  !!!</h1>"
if __name__ == '__main__':
    app.run(threaded=True,port=5004)