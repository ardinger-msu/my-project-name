from flask import Flask, jsonify, request
from bot import BuilderBot
import json

app = Flask(__name__)

BOT_INSTANCE = None  # global bot instance


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/spawn_bot")
def spawn_bot():
    global BOT_INSTANCE
    username = request.args.get("username")

    if BOT_INSTANCE is None:
        BOT_INSTANCE = BuilderBot(username)

        return jsonify({"status": "started"})
    return jsonify({"status": "already_running"})


if __name__ == "__main__":
    app.run()
