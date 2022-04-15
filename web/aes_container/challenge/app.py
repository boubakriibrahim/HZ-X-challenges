from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
import binascii
from flask import Flask
from flask import request
from flask import render_template

app = Flask(
    __name__,
    template_folder="templates", static_folder="static", static_url_path=''
)


key = get_random_bytes(16)
iv = get_random_bytes(16)
flag= "HZxCTF{3V3N_A3S_!S_NOT_SAFE}"

def encrypt(str1):
    obj = AES.new(key, AES.MODE_CBC, iv)
    str1=str1.encode('utf-8')
    str1 = pad(str1,16)
    ciphertext = obj.encrypt(str1)
    return ciphertext

def decrypt(str2):
    obj=AES.new(key, AES.MODE_CBC, iv)
    plaintext=obj.decrypt(str2)
    plaintext=unpad(plaintext,16)
    return plaintext


@app.route("/" , methods= ["POST" , "GET"])
def hello():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        combined_txt = f"username={username}&password={password}"
        if "username=csiadmin&password=ctfchallenge2022" in combined_txt:
            # testing :
            enc=encrypt(combined_txt)
            hexstring=binascii.hexlify(enc)
            hexstring=str(binascii.hexlify(iv))[2:-1]+str(hexstring)[2:-1]
            print(hexstring)
            #############
            return render_template("home.html", msg = "Your server has been hacked. next time make sure to take precautionary measures\nbest regards: xX_SLAYER_Xx")
        else :
            
            enc=encrypt(combined_txt)
            hexstring=binascii.hexlify(enc)
            hexstring=str(binascii.hexlify(iv))[2:-1]+str(hexstring)[2:-1]
            return render_template("home.html" , enc = hexstring)
            
            

@app.route("/home" , methods = ["GET" , "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    
    elif request.method == "POST":
        try :
            hex_string = request.form.get("hex")
            hex_string.encode('utf-8')
            input_str = binascii.unhexlify(hex_string)
            decrypted = str(decrypt(input_str))[2:-1]
            if "username=csiadmin&password=ctfchallenge2022" in decrypted :
                return render_template("home.html" , msg = f"flag : {flag}")
            else:
                return render_template("home.html" ,enc = " ", msg = "Wrong hex, you don't have access")
        except :
            return render_template("home.html" , msg = "ERROR: wrong hex format")
