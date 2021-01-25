from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("main.j2")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112))
    app.run(port=port, debug=True)