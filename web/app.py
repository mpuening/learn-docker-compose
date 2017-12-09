#
# This app uses redis (key/value pair data store) to keep track
# of how many times ths web page has been visited.
#
from flask import Flask
from redis import Redis

app = Flask(__name__)

#
# In the Docker Compose environment, redis is the hostname
#
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello World from Docker Compose! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

