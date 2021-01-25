from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def root():
    return "Hello Two Guys!"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112))
    app.run(port=port)