from flask import Flask, render_template, request, send_file
import classic.vignere, classic.playfair, classic.extvignere, classic.util
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './processed-files'


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
    msg = classic.util.alphabetify(request.form["message"])
    key = classic.util.alphabetify(request.form["key"])

    if request.form["act"] == "enc":
        result = classic.vignere.encrypt(msg, key)
    else:
        result = classic.vignere.decrypt(msg, key)
    
    if request.form["format"] == "block":
            result = classic.util.blockify(result)
    
    return render_template("vignere.html", result=result, inputtext=msg, key=key)

@app.route('/extvignere', methods=['POST'])
def view_extvignere_result():
    key = request.form["key"].upper()
    
    if request.form["type-inp"] == "txt":
        msg = request.form["message"].upper()

        if request.form["act"] == "enc":
            result = classic.extvignere.encrypt(msg, key)
        else:
            result = classic.extvignere.decrypt(msg, key)
        
        if request.form["format"] == "block":
            result = classic.util.blockify(result)
        
        return render_template("extvignere.html", result=result, inputtext=msg, key=key)

    else:
        # Save File
        f = request.files["file"]
        f_loc = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
        f.save(f_loc)

        if request.form["act"] == "enc":
            res_loc = classic.extvignere.encrypt(f_loc, key, True)
        else:
            res_loc = classic.extvignere.decrypt(f_loc, key, True)
        
        return send_file(res_loc, as_attachment=True)



# Entry point
if __name__ == '__main__':
    app.run()