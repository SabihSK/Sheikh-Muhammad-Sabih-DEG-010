import json
import logging
import os
import sys

from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
)

TODO_FILE_NAME = "todo.json"
TODO_ITEMS = []

if os.path.exists(TODO_FILE_NAME):
    with open(TODO_FILE_NAME) as f:
        TODO_ITEMS = json.load(f)


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        content = request.form.get("content")
        if content:
            TODO_ITEMS.append(content)
            save_todo_items()

    return render_template("index.html", todo_items=TODO_ITEMS)


def save_todo_items():
    with open(TODO_FILE_NAME, "w") as f:
        json.dump(TODO_ITEMS, f)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
