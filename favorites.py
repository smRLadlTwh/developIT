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


#즐겨찾기 목록 불러오는 API
def board_favorite():
    return