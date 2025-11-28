from flask import Flask, request, jsonify

app = Flask(__name__)

# Allowed movement directions
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

    # Validate speed range (0–10)
    try:
        speed = int(speed)
    except:
        return jsonify({"error": "Speed must be an integer"}), 400

    if speed < 0 or speed > 255:
        return jsonify({"error": "Speed must be between 0 and 10"}), 400

    # Print received command to server console
    print(f"[COMMAND] Direction: {direction}, Speed: {speed}")

    return jsonify({
        "status": "ok",
        "direction": direction,
        "speed": speed
    }), 200


if __name__ == "__main__":
    # Allows testing via local network (optional)
    app.run(host="0.0.0.0", port=5000, debug=True)
