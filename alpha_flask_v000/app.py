from flask import Flask, render_template, request
import AlphaBot

app = Flask(__name__)
alpha = AlphaBot.AlphaBot()

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

        else:
            print("Unknown")
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')