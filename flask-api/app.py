from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})


@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    return jsonify({"message": f"Hello, {name}!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
