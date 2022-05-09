from flask import Flask, render_template, jsonify, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime, timedelta
import hashlib

app = Flask(__name__)

client = MongoClient('127.0.0.1', 27017, username="test", password="test")
db = client.developITdb

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
