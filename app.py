from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Resource, Api, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Sample API Documentation', description='A sample API')  # <- タイトルなどを変更

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/my_schema?charset=utf8mb4'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


resource_fields = api.model(User, {
    "username": fields.String,
    "email": fields.String,
})


# @api.route('/user')
# @api.doc(params={'username': 'ユーザー名', 'email': 'E-mailです'})
# class UserApi(Resource):
#     def get(self, name, email):
#         return {
#             "name": name,
#             "email": email
#         }
#
#     @api.doc(body=resource_fields)
#     @api.doc(responses={400: '無効なBody'})  # <- HTTPコード, 補足を追加
#     def post(self, name, email):
#         body = request.json
#
#         # 追加 -------------------
#         if not body:
#             api.abort(400)
#         # -----------------------
#
#         return {
#             "name": name,
#             "email": email,
#             "body": body,
#         }
