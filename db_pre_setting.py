import os

from flask import Flask, render_template, jsonify, request, redirect, session, abort, url_for
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "secret_key"

if os.environ['env'] == 'prod':
    client = MongoClient(f'{os.environ["host"]}', 27017, username=f'{os.environ["user"]}',
                         password=f'{os.environ["password"]}', authSource="admin")
    CLIENT_ID = os.environ['CLIENT_ID']
    REDIRECT_URI = os.environ['REDIRECT_URI']
    host = os.environ['host']
    SECRET_KEY = os.environ["security"]
    SIGNOUT_REDIRECT_URI = os.environ['SIGNOUT_REDIRECT_URI']
else:
    from configs import config_local as config

    client = MongoClient(f'{config.host}', 27017)
    CLIENT_ID = config.CLIENT_ID
    REDIRECT_URI = config.REDIRECT_URI
    host = config.host
    SECRET_KEY = config.security
    SIGNOUT_REDIRECT_URI = config.SIGNOUT_REDIRECT_URI

db = client.developITdb

if __name__ == '__main__':
    doc = {
        'user': {
            "uuid": 'a51x1f3d-813f-40fe-93c1-75ec1ea26711',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-08 12:15:57',
        },
        'board': {
            "uuid": 'a70e128a-7f61-4ad7-a41a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-08 14:15:57',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a21x1f3d-813f-40fe-93c1-75ec1ea26711',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-08 13:15:57',
        },
        'board': {
            "uuid": 'a70e128a-7f41-4ad7-a41a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-08 14:15:57',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    # 5월8일자 2개

    doc = {
        'user': {
            "uuid": 'a51x1f3d-813f-40fe-93c1-65ec1ea26911',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-09 02:15:57',
        },
        'board': {
            "uuid": 'a70e128a-7f31-4ad7-a41a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-09 14:15:57',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a51x1f3d-813f-40fe-93c1-25ec1ea26911',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-09 03:15:57',
        },
        'board': {
            "uuid": 'a70e828a-7f31-4ad7-a41a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-09 14:45:52',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a51x1f3d-813f-40fe-93c1-35ec1ea26911',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-09 03:13:57',
        },
        'board': {
            "uuid": 'a77e128a-7f31-4ad7-a41a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-09 18:15:57',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a51x1f3d-813f-40fe-73c1-65ec1ea26911',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-09 05:12:57',
        },
        'board': {
            "uuid": 'a70e328a-7f31-4ad7-a41a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-09 14:15:57',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a51x1f3d-813f-40fe-93c1-65ec1ea26901',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-09 06:15:57',
        },
        'board': {
            "uuid": 'a70e128a-7f51-4ad7-a41a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-09 14:12:51',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    # 5월 9일자 5개

    doc = {
        'user': {
            "uuid": 'a51x1f3d-813f-40fe-53c1-64ec1ea26911',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-10 11:25:57',
        },
        'board': {
            "uuid": 'a72e128a-7f31-4ad7-a41a-d9613a2a4a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-10 16:25:57',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a51x1f3d-823f-40fe-93c1-55ec1ea26911',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-10 11:15:57',
        },
        'board': {
            "uuid": 'a71e828a-7f31-4ad7-a41a-d7613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-10 15:45:52',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a51x1f3d-813f-40fe-93c1-35ec1ea22971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-10 02:23:57',
        },
        'board': {
            "uuid": 'a47e128a-2f31-4ad7-a41a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-10 19:13:57',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a55x1f3d-813f-40fe-73c1-65ec1ea26911',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-10 05:12:57',
        },
        'board': {
            "uuid": 'a70e328a-7f31-9ad7-a41a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-10 14:15:52',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a51x1f3d-813f-40fe-93c1-35ec1ea26901',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-10 16:15:57',
        },
        'board': {
            "uuid": 'a70e138a-7f51-4ad7-a41a-d8613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-10 18:12:51',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a51x1f3d-813f-40fe-93c1-65ec1ea26101',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-10 03:25:57',
        },
        'board': {
            "uuid": 'a70e128a-7f51-1ad7-a41a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-10 14:12:59',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a51x1f3d-883f-40fe-93c1-65ec1ea26901',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-10 02:15:57',
        },
        'board': {
            "uuid": 'a70e188a-7f51-4ad7-a41a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-10 14:12:51',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    # 5월 10일자 7개

    doc = {
        'user': {
            "uuid": 'a51x2f5d-813f-40fe-93c1-35ec1ea22971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-11 03:43:27',
        },
        'board': {
            "uuid": 'a47e128a-2f51-6ad7-a91a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-11 20:23:37',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a51x4f3d-873f-50fe-92c1-35ec1ea22971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-11 03:43:52',
        },
        'board': {
            "uuid": 'a42e328a-4f31-5ad7-a61a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-11 07:23:37',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a51x1f3d-213f-32fe-33c1-45ec5ea62771',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-11 03:43:56',
        },
        'board': {
            "uuid": 'a23e428a-5f31-4ad7-a41a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-11 20:33:47',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a51x1f3d-813f-39fe-23c1-35ec4ea22971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-11 05:23:17',
        },
        'board': {
            "uuid": 'a47e128a-2f31-4ad7-a41a-d9623a4a5a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-11 12:33:47',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a51x1f3d-812f-30fe-43c2-35ec1ea22971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-11 03:23:57',
        },
        'board': {
            "uuid": 'a47e128a-2f31-4ad7-a41a-d9623a3a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-11 15:23:47',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a51x6f5d-833f-20fe-93c1-35ec1ea22971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-11 09:25:27',
        },
        'board': {
            "uuid": 'a42e328a-5f61-4ad7-a41a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-11 12:33:27',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a51x1f5d-933f-20fe-96c1-55ec1ea22971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-11 14:45:27',
        },
        'board': {
            "uuid": 'a47e826a-2f81-4ad7-a41a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-11 17:23:47',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a11x2f3d-853f-40fe-93c1-35ec1ea22971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-11 10:23:37',
        },
        'board': {
            "uuid": 'a47e108a-1f31-4ad7-a27a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-11 20:23:47',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a51x1f3d-813f-14fe-23c1-55ec1ea88971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-11 17:47:37',
        },
        'board': {
            "uuid": 'a47e128a-2f31-4ad7-a41a-d4855a3a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-11 19:31:43',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a15x3f4d-723f-40fe-93c1-35ec1ea22971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-11 04:13:27',
        },
        'board': {
            "uuid": 'a47e107a-2f36-5ad7-a41a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-11 20:23:47',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    # 5월 11일 10개

    doc = {
        'user': {
            "uuid": 'a15x3f4d-893f-20fe-33c1-35ec1ea22971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 02:03:27',
        },
        'board': {
            "uuid": 'a42e307a-6f36-1ad7-a41a-d9613a2a1a90',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-12 04:22:11',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a15x3f4d-723f-40fe-93c1-35ec1ea22971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 04:13:27',
        },
        'board': {
            "uuid": 'a47e107a-2f36-5ad7-a41a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-12 20:23:47',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a15x5f4d-223f-10fe-33c1-45ec2ea12971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 04:13:27',
        },
        'board': {
            "uuid": 'a47e107a-2f36-5ad7-a41a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-12 20:23:47',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a15x3f4d-723f-40fe-93c1-35ec1ea22971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 05:53:27',
        },
        'board': {
            "uuid": 'a42e307a-5f36-5ad7-a41a-d9513a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-12 15:13:17',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a23x4f5d-623f-40fe-93c1-35ec1ea22971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 05:23:17',
        },
        'board': {
            "uuid": 'a47e107a-1f36-5ad7-a41a-d8618a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-12 15:13:17',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a15x3f4d-769f-30fe-93c1-55ec1ea22971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 06:43:17',
        },
        'board': {
            "uuid": 'a09e277a-3f36-9ad7-a41a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-12 18:53:17',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a15x6f3d-223f-10fe-90c1-35ec1ea22971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 08:53:47',
        },
        'board': {
            "uuid": 'a47e107a-2f26-5ad8-a11a-d2365a5a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-12 17:13:27',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a15x3f4d-723f-32fe-43c1-39ec1ea02071',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 10:53:27',
        },
        'board': {
            "uuid": 'a41e167a-2f46-3ad7-a52a-d7613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-12 11:25:47',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a15x3f4d-723f-39fe-83c1-55ec4ea02971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 11:23:37',
        },
        'board': {
            "uuid": 'a47e107a-2f56-5ad8-a11a-d8512a1a4a81',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-12 22:13:27',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a15x3f4d-524f-10fe-23c1-35ec1ea61871',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 11:23:37',
        },
        'board': {
            "uuid": 'a48e907a-2f56-1ad2-a41a-d1643a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-12 22:43:57',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a15x2f1d-541f-40fe-93c1-35ec1ea22971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 10:57:14',
        },
        'board': {
            "uuid": 'a27e100a-2f36-5ad8-a46a-d5643a2a2a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-12 20:13:47',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a21x3f8d-643f-10fe-03c1-28ec1ea22971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 11:11:11',
        },
        'board': {
            "uuid": 'a47e107a-2f36-5ad7-a41a-d9613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-12 11:13:13',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a15x3f4d-222f-11fe-93c1-33ec3ea22971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 12:12:12',
        },
        'board': {
            "uuid": 'a47e107a-2f36-1ad1-a11a-d4613a2a1a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-12 12:13:13',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a22x2f2d-777f-00fe-33c1-35ec1ea22971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 12:14:14',
        },
        'board': {
            "uuid": 'a47e000a-3f36-5ad7-a41a-d9611a2a1a77',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-12 12:15:37',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a44x2f1d-423f-50fe-63c3-50ec1ea22971',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 12:16:17',
        },
        'board': {
            "uuid": 'a47e107a-2f36-6ad6-a66a-d9613a2a1a11',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-12 12:17:18',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a25x3f4d-526f-22fe-11c1-35ec5ea25551',
            "e_mail": '1234@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 13:33:11',
        },
        'board': {
            "uuid": 'a44e100a-3f36-6ad7-a91a-d9812a2a4a91',
            "title": 'dummy title data',
            "content": 'dummy content data',
            "cost": '300000',
            "created_at": '2022-05-12 15:16:37',
            'image_url': 'default_image.jpeg',
        }
    }

    db.board.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a53x1f3d-813f-40fe-93c1-75ec1ea26711',
            "e_mail": '12314@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-08 11:25:37',
        }
    }
    db.user.insert_one(doc)

    # 5/8  = 1명

    doc = {
        'user': {
            "uuid": 'a53x1f3d-813f-40fe-93c1-75ec1ea26711',
            "e_mail": '1a2314@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-09 11:15:37',
        }
    }

    db.user.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a53x1f3d-813f-40fe-93c1-75ec1ea26711',
            "e_mail": '1a142a314@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-09 11:25:37',
        }
    }

    db.user.insert_one(doc)

    # 5/9  = 2명

    doc = {
        'user': {
            "uuid": 'a53x1f3d-813f-40fe-93c1-75ec1ea26711',
            "e_mail": '1a2a2314@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-10 11:25:37',
        }
    }

    db.user.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a53x1f3d-813f-40fe-93c1-75ec1ea26711',
            "e_mail": '1a2b3a1a4@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-10 11:25:37',
        }
    }

    db.user.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a53x1f3d-813f-40fe-93c1-75ec1ea26711',
            "e_mail": '122a33x14@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-10 11:25:37',
        }
    }

    db.user.insert_one(doc)

    # 5/10 3명

    doc = {
        'user': {
            "uuid": 'a53x1f3d-813f-40fe-93c1-75ec1ea26711',
            "e_mail": '1b2l72a33x14@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-11 13:25:37',
        }
    }

    db.user.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a53x1f3d-813f-40fe-93c1-75ec1ea26711',
            "e_mail": '12n2a336x14@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-11 14:25:37',
        }
    }

    db.user.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a53x1f3d-813f-40fe-93c1-75ec1ea26711',
            "e_mail": '12s2a3x3x14@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-11 15:25:37',
        }
    }

    db.user.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a53x1f3d-813f-40fe-93c1-75ec1ea26711',
            "e_mail": '1axia33x14@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-11 16:25:37',
        }
    }

    # 5/11 4명

    db.user.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a53x1f3d-813f-40fe-93c1-75ec1ea26711',
            "e_mail": '2a3h3x1z4@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 11:03:27',
        }
    }

    db.user.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a53x1f3d-813f-40fe-93c1-75ec1ea26711',
            "e_mail": '122xa3x3x1z4@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 11:23:27',
        }
    }

    db.user.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a53x1f3d-813f-40fe-93c1-75ec1ea26711',
            "e_mail": '122a33x1zx4@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 11:33:27',
        }
    }

    db.user.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a53x1f3d-813f-40fe-93c1-75ec1ea26711',
            "e_mail": '12z2a33x1z4@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 11:43:27',
        }
    }

    db.user.insert_one(doc)

    doc = {
        'user': {
            "uuid": 'a53x1f3d-813f-40fe-93c1-75ec1ea26711',
            "e_mail": '12z2a33x1z4@naver.com',
            "password": '1234',
            "name": '김지호',
            "phone_number": '',
            "created_at": '2022-05-12 11:53:27',
        }
    }

    db.user.insert_one(doc)

    # 5/12 5명


