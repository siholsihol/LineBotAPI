from flask import FLASK
app = Flask(__name__)

@app.route('/')
def index():
  return 'hello, world'
