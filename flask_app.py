from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def msg():
    return render_template('msg.html')

@app.route('/read')
def read():
    msg = request.args.get('msg', '')
    if msg != '':
        f = open("file.txt", "a")
        f.write(msg + '<br>')
        f.close()
    f = open("file.txt", "r")
    return f.read()
