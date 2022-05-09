from flask import Flask, render_template, jsonify, request, redirect, url_for
from pymongo import MongoClient
import hashlib
import os
import board

app = Flask(__name__)

if os.environ['env'] == 'prod':
    from configs import config_prod as config

    client = MongoClient(f'{config.host}', 27017, username=f'{config.user}', password=f'{config.password}')
else:
    from configs import config_local as config

    client = MongoClient(f'{config.host}', 27017)

db = client.developITdb


# 게시글 페이지 띄우기
@app.route("/board")
def board_page():
    return render_template('board.html')


@app.route("/api/board/write", methods=['POST'])
def board_write():
    response = board.board_write()
    return jsonify(response)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
