from flask import Flask, render_template, request
import classic.vignere, classic.playfair

app = Flask(__name__)

'''
Notes:
1. Untuk semua module, import classic.<nama>
2. Sebelum olah akses input dari user, jangan lupa dikapitalkan dulu dengan .upper()
3. Akses input teks dari user di request.form["message"]
'''


# Routes
@app.route('/')
def landing():
    return render_template("index.html", message="Henlo!")

@app.route('/<cipher>')
def view_cipher_page(cipher):
    return render_template(cipher+".html", message=cipher)


# Post routes fill here
@app.route('/vignere', methods=['POST'])
def view_vignere_result():
    msg = request.form["message"].upper()
    key = request.form["key"].upper()

    if request.form["act"] == "enc":
        result = classic.vignere.encrypt(msg, key)
    else:
        result = classic.vignere.decrypt(msg, key)
    return render_template("vignere.html", result=result, inputtext=msg)



# Entry point
if __name__ == '__main__':
    app.run()