import streamlit as st
import requests

st.set_page_config(page_title="Robot Controller", page_icon="🤖")

st.title("🚗 Robot Control Panel")

# --- Speed Slider ---
speed = st.slider("Speed", 0, 255, 120)

st.write("### Direction Controls")

# Layout buttons in a grid
col1, col2, col3 = st.columns(3)

# Function to send commands
def send_command(direction, speed):
    url = "http://127.0.0.1:5000/move"   # Change to your Flask server URL if needed
    payload = {"direction": direction, "speed": speed}

    try:
        res = requests.post(url, json=payload, timeout=3)
        if res.status_code == 200:
            st.success(f"Sent: {direction} at speed {speed}")
        else:
            st.error(f"Error {res.status_code}: {res.text}")
    except Exception as e:
        st.error(f"Failed to send command: {e}")

# --- Buttons ---

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

# Stop button full width
st.write("---")
if st.button("🛑 STOP", use_container_width=True):
    send_command("stop", 0)
