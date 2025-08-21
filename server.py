from flask import Flask
import threading
import bot  # import your bot.py

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running on Render 🚀"

# Start Telegram bot in background thread
threading.Thread(target=bot.main, daemon=True).start()
