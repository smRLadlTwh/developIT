from flask import Flask, render_template, jsonify, request, session
import re
import datetime
import json
import app
import jwt
import os

from pymongo import MongoClient

if os.environ['env'] == 'prod':
    from configs import config_prod as config
else:
    from configs import config_local as config

client = MongoClient(f'{config.host}', 27017, username=f'{config.user}', password=f'{config.password}')
db = client.developITdb

SECRET_KEY = config.security

# 게시물을 등록하는 API
def board_write():
    token = request.cookies.get('access_token')
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})
        comment_receive = request.form["comment_give"]
        date_receive = request.form["date_give"]
        doc = {
            "username": user_info["username"],
            "profile_name": user_info["profile_name"],
            "profile_pic_real": user_info["profile_pic_real"],
            "comment": comment_receive,
            "date": date_receive
        }
        db.posts.insert_one(doc)
        # 포스팅하기
        return jsonify({"result": "success", 'msg': '포스팅 성공'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))

