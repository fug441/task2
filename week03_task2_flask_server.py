from flask import Flask, request, jsonify

app = Flask(__name__)

VALID_DIRECTIONS = {"forward", "backward", "left", "right", "stop"}

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "alive"}), 200


@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON received"}), 400

    direction = data.get("direction")
    speed = data.get("speed")

    # Validate direction
    if direction not in VALID_DIRECTIONS:
        return jsonify({"error": "Invalid direction"}), 400

    # Validate speed
    try:
        speed = int(speed)
    except:
        return jsonify({"error": "Speed must be an integer"}), 400

    if speed < 0 or speed > 255:
        return jsonify({"error": "Speed must be between 0 and 10"}), 400

    # Print to console (simulates sending commands to hardware)
    print(f"[MOVE] Direction: {direction}, Speed: {speed}")

    return jsonify({
        "status": "ok",
        "direction": direction,
        "speed": speed
    }), 200


if __name__ == "__main__":
    # Accessible on local network, helpful for mobile testing
    app.run(host="0.0.0.0", port=5000, debug=True)
