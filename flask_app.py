from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    msg = request.args.get('msg','')
    if msg == '':
        f = open("file.txt", "r")
        return "<form>Message <input name='msg'></form>" + f.read()
    else:
        f = open("file.txt", "a")
        f.write(msg + '<br>')
        f.close()
        f = open("file.txt", "r")
        return "<form>Message <input name='msg'></form>" + f.read()
