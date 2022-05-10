import boto3
from flask import Flask, render_template, jsonify, request, session, url_for, redirect, abort
import datetime
import json
import jwt
import os
import uuid
from werkzeug.utils import secure_filename

from pymongo import MongoClient

if os.environ['env'] == 'prod':
    from configs import config_prod as config

    client = MongoClient(f'{config.host}', 27017, username=f'{config.user}', password=f'{config.password}')
else:
    from configs import config_local as config

    client = MongoClient(f'{config.host}', 27017)

db = client.developITdb

SECRET_KEY = config.security


# 게시물을 등록하는 API
def board_write():
    token = request.cookies.get('token')
    if token is None:
        abort(404, '토큰 정보가 존재하지 않습니다.')
    try:
        # 유저 정보 식별
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_info = db.developIT.find_one({"uuid": payload["uuid"]})
        if user_info is None:
            abort(404, '회원 정보가 존재하지 않습니다.')

        board = []
        if user_info.get('boards') is not None:
            board = user_info['boards']
        now = datetime.datetime.now()
        time = now.strftime('%Y-%m-%d %H:%M:%S')

        board_uuid = str(uuid.uuid4())

        # 유저로부터 받은 데이터
        title = request.form["title"]
        content = request.form["content"]
        cost = request.form["cost"]
        doc = {
            "uuid": board_uuid,
            "title": title,
            "content": content,
            "cost": cost,
            "created_at": time,
        }

        if 'image' in request.files:
            file = request.files["image"]
            filename = secure_filename(file.filename)
            extension = filename.split(".")[-1]
            file_path = f"{time}.{extension}"
            doc["image_url"] = file_path

            s3 = boto3.client('s3', aws_access_key_id=config.aws_access_key, aws_secret_access_key=config.aws_secret_key)
            s3.put_object(
                ACL="public-read",
                Bucket="devit-bucket",
                Body=file,
                Key=file_path,
                ContentType=file.content_type)

        board.append(doc)

        db.developIT.update_one({'user.uuid': str(user_info['uuid'])}, {'$set': {'boards': board}})

        return {"result": "success", "status_code": 201}
    except jwt.ExpiredSignatureError:
        return {"result": "success", "status_code": 400, "error_message": 'EXPIRED_TOKEN'}
    except jwt.exceptions.DecodeError:
        return {"result": "success", "status_code": 400, "error_message": 'INVALID_TOKEN'}
