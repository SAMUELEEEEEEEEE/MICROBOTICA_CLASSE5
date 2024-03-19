from flask import Flask, request, jsonify, render_template
import AlphaBot

app = Flask(__name__)
alphabot = AlphaBot.AlphaBot()

@app.route("/api/v1/resources/sensors/left", methods = ["GET"])
def left():
    return jsonify({"l" : alphabot.get_sensor_values()["l"]})

@app.route("/api/v1/resources/sensors/right", methods = ["GET"])
def right():
    return jsonify({"r" : alphabot.get_sensor_values()["r"]})

result_dict = {"l" : left, "r" : right}

@app.route("/api/v1/resources/sensors/generic", methods = ["GET"])
def generic():
    """
    query string = side=l / side=r / side=b
    """
    if "side" in request.args:
        side = request.args["side"]
        
        if side == "b":
            return jsonify(alphabot.get_sensor_values())

        return result_dict[side]()

@app.route("/", methods = ["GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)