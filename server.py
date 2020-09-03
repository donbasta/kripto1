from flask import Flask, render_template, request

app = Flask(__name__)


# Routes
@app.route('/')
def landing():
    return render_template("index.html", message="Henlo!")

@app.route('/<cipher>')
def view_cipher_page(cipher):
    return render_template(cipher+".html", message=cipher)
    
# Post routes fill here


# Entry point
if __name__ == '__main__':
    app.run()