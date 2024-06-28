from flask import Flask, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
import os
import string
import random

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:admin@localhost/urlshortener'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512), nullable=False)
    short_url = db.Column(db.String(512), unique=True, nullable=False)

    def __init__(self, original_url, short_url):
        self.original_url = original_url
        self.short_url = short_url

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(characters, k=5))
    link = URL.query.filter_by(short_url=short_url).first()
    if link:
        return generate_short_url()
    return short_url

class URLShortener(Resource):
    def post(self):
        data = request.get_json()
        original_url = data.get('original_url')
        short_url = generate_short_url()
        new_link = URL(original_url=original_url, short_url=short_url)
        db.session.add(new_link)
        db.session.commit()
        return jsonify({'short_url': request.host_url + short_url})
    pass

class URLRedirect(Resource):
    def get(self, short_url):
        link = URL.query.filter_by(short_url=short_url).first_or_404()
        return redirect(link.original_url)
    pass

api.add_resource(URLShortener, '/api/shorten')
api.add_resource(URLRedirect, '/<string:short_url>')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
