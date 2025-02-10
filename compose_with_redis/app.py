from flask import Flask
import os
import redis

app = Flask(__name__)

redis_host = os.environ.get('REDIS_HOST', 'localhost')
r = redis.Redis(host=redis_host, port=6379)

@app.route('/')
def hello():
    r.set('message', 'Hello, World!')
    message = r.get('message').decode()
    return f"Redis: {message}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
