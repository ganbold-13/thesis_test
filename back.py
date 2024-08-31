from flask import Flask, request, render_template_string, redirect, url_for, jsonify
from flask_cors import CORS
from utils import hackernews, db_fetch
app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})

@app.route('/')
def index():
    return jsonify(hackernews())

@app.route('/news', methods=['GET', 'POST'])
def news():
    return db_fetch()


if __name__ == '__main__':
    app.run(host='192.168.96.136', debug=True)
