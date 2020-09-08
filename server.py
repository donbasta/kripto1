from flask import Flask, render_template, request, send_file
import classic.vigenere, classic.fullvigenere, classic.rkvigenere, classic.extvigenere, classic.playfair, classic.util
import classic.affine, classic.enigma, classic.hill, classic.superenc
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './processed-files'


'''
Notes:
1. Untuk semua module, import classic.<nama>
2. Sebelum olah akses input dari user, jangan lupa olah menggunakan classic.util
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
@app.route('/vigenere', methods=['POST'])
def view_vigenere_result():
    msg = classic.util.alphabetify(request.form["message"])
    key = classic.util.alphabetify(request.form["key"])

    if request.form["act"] == "enc":
        result = classic.vigenere.encrypt(msg, key)
    else:
        result = classic.vigenere.decrypt(msg, key)
    
    if request.form["format"] == "block":
            result = classic.util.blockify(result)
    
    if request.form["type-out"] == "file":
        f_path = app.config['UPLOAD_FOLDER'] + "/" + request.form["act"] + ".txt"
        f = open(f_path, "w")
        f.write(result)
        f.close()
        return send_file(f_path, as_attachment=True)
    
    return render_template("vigenere.html", result=result, inputtext=msg, key=key)


@app.route('/fullvigenere', methods=['POST'])
def view_fullvigenere_result():
    msg = classic.util.alphabetify(request.form["message"])
    key = classic.util.alphabetify(request.form["key"])

    if request.form["act"] == "enc":
        result = classic.fullvigenere.encrypt(msg, key)
    else:
        result = classic.fullvigenere.decrypt(msg, key)
    
    if request.form["format"] == "block":
            result = classic.util.blockify(result)
    
    if request.form["type-out"] == "file":
        f_path = app.config['UPLOAD_FOLDER'] + "/" + request.form["act"] + ".txt"
        f = open(f_path, "w")
        f.write(result)
        f.close()
        return send_file(f_path, as_attachment=True)
    
    return render_template("fullvigenere.html", result=result, inputtext=msg, key=key)


@app.route('/rkvigenere', methods=['POST'])
def view_rkvigenere_result():
    msg = classic.util.alphabetify(request.form["message"])
    key = classic.util.alphabetify(request.form["key"])

    if request.form["act"] == "enc":
        result = classic.rkvigenere.encrypt(msg, key)
    else:
        result = classic.rkvigenere.decrypt(msg, key)
    
    if request.form["format"] == "block":
            result = classic.util.blockify(result)
    
    if request.form["type-out"] == "file":
        f_path = app.config['UPLOAD_FOLDER'] + "/" + request.form["act"] + ".txt"
        f = open(f_path, "w")
        f.write(result)
        f.close()
        return send_file(f_path, as_attachment=True)
    
    return render_template("rkvigenere.html", result=result, inputtext=msg, key=key)


@app.route('/extvigenere', methods=['POST'])
def view_extvigenere_result():
    key = request.form["key"]
    
    if request.form["type-inp"] == "txt":
        msg = request.form["message"]

        if request.form["act"] == "enc":
            result = classic.extvigenere.encrypt(msg, key)
        else:
            result = classic.extvigenere.decrypt(msg, key)
        
        if request.form["format"] == "block":
            result = classic.util.blockify(result)
        
        if request.form["type-out"] == "file":
            f_path = app.config['UPLOAD_FOLDER'] + "/" + request.form["act"] + ".txt"
            f = open(f_path, "w")
            f.write(result)
            f.close()
            return send_file(f_path, as_attachment=True)
        
        return render_template("extvigenere.html", result=result, inputtext=msg, key=key)

    else:
        # Save File
        f = request.files["file"]
        f_loc = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
        f.save(f_loc)

        if request.form["act"] == "enc":
            res_loc = classic.extvigenere.encrypt(f_loc, key, True)
        else:
            res_loc = classic.extvigenere.decrypt(f_loc, key, True)
        
        return send_file(res_loc, as_attachment=True)


@app.route('/playfair', methods=['POST'])
def view_playfair_result():
    msg = classic.util.alphabetify(request.form["message"])
    key = classic.util.alphabetify(request.form["key"])

    if request.form["act"] == "enc":
        result = classic.playfair.encrypt(msg, key)
    else:
        result = classic.playfair.decrypt(msg, key)
    
    if request.form["format"] == "block":
            result = classic.util.blockify(result)
    
    if request.form["type-out"] == "file":
        f_path = app.config['UPLOAD_FOLDER'] + "/" + request.form["act"] + ".txt"
        f = open(f_path, "w")
        f.write(result)
        f.close()
        return send_file(f_path, as_attachment=True)
    
    return render_template("playfair.html", result=result, inputtext=msg, key=key)


@app.route('/superenc', methods=['POST'])
def view_superenc_result():
    #TODO
    msg = classic.util.alphabetify(request.form["message"])
    key_vigenere = classic.util.alphabetify(request.form["key_vigenere"])
    key_transposition = int(request.form["key_transposition"])

    if request.form["act"] == "enc":
        result = classic.superenc.encrypt(msg, key_transposition, key_vigenere)
    else:
        result = classic.superenc.decrypt(msg, key_transposition, key_vigenere)
    
    if request.form["format"] == "block":
        result = classic.util.blockify(result)
    
    if request.form["type-out"] == "file":
        f_path = app.config['UPLOAD_FOLDER'] + "/" + request.form["act"] + ".txt"
        f = open(f_path, "w")
        f.write(result)
        f.close()
        return send_file(f_path, as_attachment=True)

    return render_template("superenc.html", result=result, inputtext=msg, key_transposition=key_transposition, key_vigenere=key_vigenere)


@app.route('/affine', methods=['POST'])
def view_affine_result():
    msg = classic.util.alphabetify(request.form["message"])
    key_m = int(request.form["key_m"])
    key_b = int(request.form["key_b"])

    if request.form["act"] == "enc":
        result = classic.affine.encrypt(msg, key_m, key_b)
    else:
        result = classic.affine.decrypt(msg, key_m, key_b)
    
    if request.form["format"] == "block":
        result = classic.util.blockify(result)
    
    if request.form["type-out"] == "file":
        f_path = app.config['UPLOAD_FOLDER'] + "/" + request.form["act"] + ".txt"
        f = open(f_path, "w")
        f.write(result)
        f.close()
        return send_file(f_path, as_attachment=True)

    return render_template("affine.html", result=result, inputtext=msg, key_m=key_m, key_b=key_b)

@app.route('/hill', methods=['POST'])
def view_hill_result():
    msg = classic.util.alphabetify(request.form["message"])
    key_0 = request.form["key_0"]
    key_1 = request.form["key_1"]
    key_2 = request.form["key_2"]
    key_matrix = [list(map(int, request.form[f"key_{i}"].split(','))) for i in range(3)]
    print(key_matrix)

    if request.form["act"] == "enc":
        result = classic.hill.encrypt(msg, key_matrix)
    else:
        result = classic.hill.decrypt(msg, key_matrix)
    
    if request.form["format"] == "block":
        result = classic.util.blockify(result)
    
    if request.form["type-out"] == "file":
        f_path = app.config['UPLOAD_FOLDER'] + "/" + request.form["act"] + ".txt"
        f = open(f_path, "w")
        f.write(result)
        f.close()
        return send_file(f_path, as_attachment=True)

    return render_template("hill.html", result=result, inputtext=msg, key_0=key_0, key_1=key_1, key_2=key_2)

@app.route('/enigma', methods=['POST'])
def view_enigma_result():
    #TODO
    print(request.form["rotor-1"], "debug")
    pass


# Entry point
if __name__ == '__main__':
    app.run()