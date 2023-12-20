from flask import Flask, render_template, request
import AlphaBot
import sqlite3 as sql
import time 

app = Flask(__name__)
alpha = AlphaBot.AlphaBot()

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


@app.route("/", methods=['GET', 'POST'])
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