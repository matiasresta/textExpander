# USER GUIDE
"""
Modules:
- pynput (pip install)
- flask (pip install)
- os (pre-install)
- json (pre-install)
- threading (pre-install)

Features:
- With CMD execute "flask run" while in the same directory as app.py
- Add a 3 letters "Key" in order to expand it into a full text
- Edit, remove and add as many keys you want

How it Works?
- With Pynput receives keyword inputs
- It creates a list of inputs and checks for the last 3 inputs received
- If the last 3 inputs are keys in the "keys.json" file then it expands into the desired text
- In case of force exiting the program the "qqq" key is hardcoded into exiting (AVOID USING THIS KEY)

Future Improvements:
- Keys do not work if they contain numbers or special characters
- Basic Code optimization
- Basic GUI improvements
- Automatic Server implementation
- Web-Application instead of local app
- There is a slight chance of bugging if turned on/off too quickly because of file interference (os module)
"""

from flask import Flask, render_template, request, redirect
import json
import textExpander
import threading


app = Flask(__name__)
database = json.load(open('keys.json', encoding='utf8'))
textExpander = textExpander.TextExpander()

@app.route('/', methods=['POST', 'GET'])
def index():
    database = json.load(open('keys.json', encoding='utf8'))
    return render_template("index.html", database=database, active=textExpander.active)

@app.route('/remove/<string:key>')
def remove(key):
    del database[key]
    with open("keys.json", "w", encoding='utf8') as write_file:
        json.dump(database, write_file, ensure_ascii=False, sort_keys=True)
    write_file.close()
    textExpander.active = False
    return redirect('/')

@app.route('/edit/<string:key>', methods=['POST', 'GET'])
def edit(key):
    text = database[key]
    if request.method == 'POST':
        del database[key]
        new_key = request.form['inputCode']
        new_text = request.form['inputText']
        database[new_key] = new_text
        with open("keys.json", "w", encoding='utf8') as write_file:
            json.dump(database, write_file, ensure_ascii=False, sort_keys=True)
        write_file.close()
        textExpander.active = False
        return redirect('/')
    else:
        return render_template("edit.html", key=key, text=text)

@app.route('/newkey', methods=['POST', 'GET'])
def newkey():
    if request.method == 'POST':
        new_key = request.form['inputCode']
        new_text = request.form['inputText']
        database[new_key] = new_text
        with open("keys.json", "w", encoding='utf8') as write_file:
            json.dump(database, write_file, ensure_ascii=False, sort_keys=True)
        write_file.close()
        textExpander.active = False
        return redirect('/')
    else:
        return render_template("newkey.html")

@app.route('/run/')
def run():
    textExpander.active = not textExpander.active
    expand = threading.Thread(target=textExpander.textExpand, args=(database,))
    expand.start()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)


