from flask import Flask, render_template, redirect, url_for, request
import AlphaBot
import sqlite3 as sql
import time
import random

app = Flask(__name__)
alpha = AlphaBot.AlphaBot()

#Login

"""def generatore_token():
    token = ""
    options = ["carattere", "numero"]
    while True:
        choice = random.choice(options)

        random_value = random.randint(0, 256)
        if (random_value >= 48 and random_value <= 57) or (random_value >= 97 and random_value <= 122):
            if choice == "carattere":
                char = chr(random_value)
            else:
                char = random_value
            token += str(char)
        else:
            continue
            
        if len(token) == 50:
            break
    return token"""

#token = generatore_token()

def validate(username, password):
    completion = False
    con = sql.connect('./db.db')
    #with sqlite3.connect('static/db.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM USERS")
    rows = cur.fetchall()

    cur.close()
    con.close()

    for row in rows:
        dbUser = row[0]
        dbPass = row[1]
        if dbUser==username:
            completion=check_password(dbPass, password)
    return completion

def check_password(hashed_password, user_password):
    # user_password = psw da hashare
    return hashed_password == user_password

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion ==False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    elif request.method == 'GET':
        return render_template('login.html', error=error)

    return render_template('login.html', error=error)


#Index
COMMAND = ["RS", "SQ", "TA"]
commandDict = {"B": alpha.backward, "F": alpha.forward, "L" : alpha.left, "R" : alpha.right, "S" : alpha.stop}

def db_interrogation(sh):

    print(sh)

    conn = sql.connect("./movements.db")
    cursor = conn.cursor()

    cursor.execute(f"SELECT Mov_sequence FROM Movements WHERE Shortcut = '{sh}'")

    res = cursor.fetchall()

    cursor.close()
    conn.close()

    for comand in res[0][0].split("-"):
        commandDict[comand.split(";")[0]]()
        time.sleep(float(comand.split(";")[1]))
        alpha.stop()


@app.route(f"/secret", methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        if request.form.get('F') == 'Forward':
            print(">>Forward")
            alpha.forward()

        elif  request.form.get('B') == 'Backward':
            print(">>Backward")
            alpha.backward()

        elif  request.form.get('S') == 'Stop':
            print(">>Stop")
            alpha.stop()

        elif  request.form.get('R') == 'Right':
            print(">>Right")
            alpha.right()

        elif  request.form.get('L') == 'Left':
            print(">>Left")
            alpha.left()

        elif request.form.get("rs") == "RS":
            db_interrogation("RS")

        elif request.form.get("ta") == "TA":
            db_interrogation("TA")

        elif request.form.get("sq") == "SQ":
            db_interrogation("SQ")

        else:
            print("Unknown")

    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')