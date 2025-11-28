# week03_task2_flask_server.py

from flask import Flask, request, jsonify

app = Flask(__name__)

# Store the latest command
latest_command = {"direction": "stop", "speed": 0}

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "alive"})

@app.route("/move", methods=["POST"])
def move():
    """Streamlit frontend posts a command here"""
    global latest_command
    data = request.get_json()

    direction = data.get("direction", "stop")
    speed = int(data.get("speed", 0))

    # Constrain speed (0–255)
    speed = max(0, min(speed, 255))

    latest_command = {"direction": direction, "speed": speed}
    print(f"[Backend] Received command: {latest_command}")

    return jsonify({"status": "ok", "sent": latest_command})

@app.route("/get_command", methods=["GET"])
def get_command():
    """Arduino polls this every 5 seconds"""
    return jsonify(latest_command)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

