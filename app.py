import os

import redis
from flask import Flask, jsonify

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "unknown")
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))


def get_redis():
    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, socket_connect_timeout=2)


@app.route("/")
def index():
    try:
        hits = get_redis().incr("hits")
        return jsonify(app=APP_NAME, hits=int(hits))
    except redis.exceptions.RedisError:
        return jsonify(app=APP_NAME, error="redis not reachable"), 503


@app.route("/health")
def health():
    return jsonify(status="ok", app=APP_NAME)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
