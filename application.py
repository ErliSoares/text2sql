from flask import Flask, request

from app.t5 import generate_sql


def create_app():
    app = Flask(__name__)

    @app.route('/ai/text2sql', methods=['POST'])
    def question():
        req_json = request.get_json()
        return generate_sql(req_json['tables'], req_json['query'])

    return app
