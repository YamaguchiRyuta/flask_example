from flask import Flask, request
from flask_restx import Resource, Api, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Sample API Documentation', description='A sample API')  # <- 追加

resource_fields = api.model("Json Bodyです", {
    "key1": fields.String,
    "key2": fields.Integer,
    "key3": fields.Boolean,
})


@api.route('/hello/<name>/<email>')
@api.doc(params={'name': '名前です', 'email': 'E-mailです'})  # <- 追加
class Hello(Resource):
    def get(self, name, email):
        return {
            "name": name,
            "email": email
        }

    @api.doc(body=resource_fields)
    @api.doc(responses={400: '無効なBody'})  # <- 追加
    def post(self, name, email):
        body = request.json

        # 追加 -------------------
        # Bodyが無効
        if not body:
            api.abort(400)
        # -----------------------

        return {
            "name": name,
            "email": email,
            "body": body,
        }


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()
