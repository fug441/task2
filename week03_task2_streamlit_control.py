import streamlit as st
import requests

st.set_page_config(page_title="Remote Vehicle Control", page_icon="🚗")

st.title("🚗 Remote Vehicle Control Panel")

# --- Speed Slider (0–255 for PWM) ---
speed = st.slider("Speed (0–255)", 0, 255, 120)

# Flask server URL
SERVER_URL = "http://192.168.12.200:5000/move"  # Change if needed

# Function to send commands to Flask
def send_command(direction, speed):
    payload = {"direction": direction, "speed": speed}

    try:
        res = requests.post(SERVER_URL, json=payload, timeout=3)

        if res.status_code == 200:
            st.success(f"Sent → {direction.upper()} @ speed {speed}")
        else:
            st.error(f"Server error ({res.status_code}): {res.text}")

    except Exception as e:
        st.error(f"Failed to contact server: {e}")


# Layout the control buttons
st.write("### Movement Controls")
col1, col2, col3 = st.columns(3)

with col2:
    if st.button("⬆️ Forward"):
        send_command("forward", speed)

with col1:
    if st.button("⬅️ Left"):
        send_command("left", speed)

with col3:
    if st.button("➡️ Right"):
        send_command("right", speed)

with col2:
    if st.button("⬇️ Backward"):
        send_command("backward", speed)

# STOP button (full width)
st.write("---")
if st.button("🛑 STOP", use_container_width=True):
    send_command("stop", 0)

