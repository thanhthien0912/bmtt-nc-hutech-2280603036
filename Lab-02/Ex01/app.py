from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.railfence import RailFenceCipher
from cipher.vigenere import VigenereCipher
from cipher.transposition import TranspositionCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

# @app.route("/caesar")
# def caesar():
#     return render_template('caesar.html')

# @app.route("/encrypt", methods=['POST'])
# def caesar_encrypt():
#     text = request.form['inputPlainText']
#     key = int(request.form['inputKeyPlain'])
#     caesar = CaesarCipher()
#     encrypted_text = caesar.encrypt_text(text, key)
#     return f"Text: {text}<br/>Key: {key}<br/>Encrypt Text: {encrypted_text}"

# @app.route("/decrypt", methods=['POST'])
# def caesar_decrypt():
#     text = request.form['inputCipherText']
#     key = int(request.form['inputKeyCipher'])
#     caesar = CaesarCipher()
#     decrypted_text = caesar.decrypt_text(text, key)
#     return f"Text: {text}<br/>Key: {key}<br/>Encrypt Text: {decrypted_text}"

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    vigenere = VigenereCipher()
    encrypted_text = vigenere.vigenere_encrypt(text, key)
    return f"Text: {text}<br/>Key: {key}<br/>Vigenere Text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    vigenere = VigenereCipher()
    decrypted_text = vigenere.vigenere_decrypt(text, key)
    return f"Text: {text}<br/>Key: {key}<br/>Vigenere Text: {decrypted_text}"

# @app.route("/railfence")
# def railfence():
#     return render_template('railfence.html')

# @app.route("/encrypt", methods=['POST'])
# def railfence_encrypt():
#     text = request.form['inputPlainText']
#     key = int(request.form['inputKeyPlain'])
#     railfence = RailFenceCipher()
#     encrypted_text = railfence.rail_fence_encrypt(text, key)
#     return f"Text: {text}<br/>Key: {key}<br/>Railfence Text: {encrypted_text}"

# @app.route("/decrypt", methods=['POST'])
# def railfence_decrypt():
#     text = request.form['inputCipherText']
#     key = int(request.form['inputKeyCipher'])
#     railfence = RailFenceCipher()
#     decrypted_text = railfence.rail_fence_decrypt(text, key)
#     return f"Text: {text}<br/>Key: {key}<br/>Railfence Text: {decrypted_text}"

# @app.route("/playfair")
# def playfair():
#     return render_template('playfair.html')

# @app.route("/encrypt", methods=['POST'])
# def playfair_encrypt():
#     text = request.form['inputPlainText']
#     key = request.form['inputKeyPlain']
#     Playfair = PlayFairCipher()
#     encrypted_text = Playfair.playfair_encrypt(text, key)
#     return f"Text: {text}<br/>Key: {key}<br/>Playfair Text: {encrypted_text}"

# @app.route("/decrypt", methods=['POST'])
# def playfair_decrypt():
#     text = request.form['inputCipherText']
#     key = request.form['inputKeyCipher']
#     playfair = PlayFairCipher()
#     decrypted_text = playfair.playfair_decrypt(text, key)
#     return f"Text: {text}<br/>Key: {key}<br/>Playfair Text: {decrypted_text}"

# @app.route("/transposition")
# def transposition():
#     return render_template('transposition.html')

# @app.route("/encrypt", methods=['POST'])
# def transposition_encrypt():
#     text = request.form['inputPlainText']
#     key = int(request.form['inputKeyPlain'])
#     transposition = TranspositionCipher()
#     encrypted_text = transposition.encrypt(text, key)
#     return f"Text: {text}<br/>Key: {key}<br/>Transposition Text: {encrypted_text}"

# @app.route("/decrypt", methods=['POST'])
# def transposition_decrypt():
#     text = request.form['inputCipherText']
#     key = int(request.form['inputKeyCipher'])
#     transposition = TranspositionCipher()
#     decrypted_text = transposition.decrypt(text, key)
#     return f"Text: {text}<br/>Key: {key}<br/>Transposition Text: {decrypted_text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
