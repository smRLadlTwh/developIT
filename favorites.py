from flask import Flask, render_template, jsonify, request, session, url_for, redirect, abort
import datetime
import json
import jwt
import os
import uuid

from pymongo import MongoClient

if os.environ['env'] == 'prod':
    from configs import config_prod as config

    client = MongoClient(f'{config.host}', 27017, username=f'{config.user}', password=f'{config.password}')
else:
    from configs import config_local as config

    client = MongoClient(f'{config.host}', 27017)

db = client.developITdb

SECRET_KEY = config.security


# 즐겨찾기 목록 불러오는 API
def write_favorite(par):
    token = request.cookies.get('token')
    if token is None:
        abort(404, '토큰 정보가 존재하지 않습니다.')

    try:
        # 유저 정보 식별
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"user.uuid": payload["uuid"]})

        # 게시글 아이디 받아옴
        board_uuid = str(par)

        # 게시글 정보들 받아옴 -> 즐겨찾기에 등록하기 위함
        board = db.board.find_one({"board.uuid": board_uuid})
        print("board : ", board)

        # 즐겨찾기에 들어갈 정보들
        favorite_uuid = str(uuid.uuid4())
        image_url = board['board']['image_url']
        title = board['board']['title']
        cost = board['board']['cost']
        writer_name = board['user']['name']
        now = datetime.datetime.now()
        create_at = now.strftime('%Y-%m-%d %H:%M:%S')

        doc = {
            "uuid": favorite_uuid,
            "board_uuid": board_uuid,
            "image_url": image_url,
            "title": title,
            "cost": cost,
            "writer_name": writer_name,
            "create_at": create_at,
        }

        favorite = []
        if user_info.get('favorites') is not None:
            favorite = user_info['favorites']

        favorite.append(doc)

        print("favorite :", favorite)

        db.user.update_one({'user.uuid': str(payload["uuid"])}, {'$set': {'favorites': favorite}})

        return {"result": "success", "status_code": 201}
    except jwt.ExpiredSignatureError:
        return {"result": "success", "status_code": 400, "error_message": 'EXPIRED_TOKEN'}


# 즐겨찾기 목록 불러오는 API
def show_favorite():
    token = request.cookies.get('token')
    if token is None:
        abort(404, '토큰 정보가 존재하지 않습니다.')

    try:
        # 유저 정보 식별
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"user.uuid": payload["uuid"]})

        print(user_info)

        if user_info.get('favorites') is None:
            return {"result": "success", 'data': ''}
        else :
            favorite_board = []
            favorite_board = user_info['favorites']

        response = {
            "result": "success",
            "data": favorite_board,
        }

        print(response)

    finally:
        return response
