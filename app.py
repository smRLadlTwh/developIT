from flask import Flask, render_template, jsonify, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime, timedelta
import hashlib

app = Flask(__name__)

client = MongoClient('127.0.0.1', 27017, username="test", password="test")
db = client.developITdb

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

# 게시글 페이지 띄우기
@app.route("/board")
def board():
    return render_template('board.html')

