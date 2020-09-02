// MODULE VIGNERE CIPHER

// Function trim: trimming whitespaces between message
function trim (msg) {
    var trimmed = "";
    for (var i = 0; i < msg.length; i++) {
        if (msg.charAt(i) != ' ') {
            trimmed += msg.charAt(i);
        }
    }

    return trimmed;
}

// Function encrypt: encrypting using standard Vignere Cipher
function encrypt (plainText, key) {
    var cipherText = "";
    for (var i = 0; i < plainText.length; i++) {
        var ord = (plainText.charCodeAt(i) - 65) + (key.charCodeAt(i % (key.length)) - 65);
        cipherText += ord.fromCharCode(0);

        // for each 5 characters, get spaced
        if (i % 5 == 0) {
            cipherText += " ";
        }
    }

    return cipherText;
}

// Function decrypt: decrypting using standard Vignere Cipher
function decrypt (cipherText, key) {
    var ctext = trim(cipherText);
    var plainText = "";
    for (var i = 0; i < ctext.length; i++) {
        var ord = (ctext.charCodeAt(i) - 65) - (key.charCodeAt(i % (key.length)) - 65);
        plainText += ord.fromCharCode(0);
    }

    return plainText;
}

module.exports.encrypt = encrypt;
module.exports.decrypt = decrypt;