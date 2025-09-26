from flask import Blueprint, request, jsonify, session
from server.models import db, User, Recipe

bp = Blueprint('main', __name__)

@bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Invalid input'}), 422
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username exists'}), 422

    user = User(username=username)
    user.password = password
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id, 'username': user.username}), 201
