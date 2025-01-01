# file: add_model.py

from flask import jsonify, request
from models import db, Competition, TeachInfo, User, Video

def add_item(model_name):
    model_map = {
        'competitions': Competition,
        'teachinfos': TeachInfo,
        'users': User,
        'videos': Video
    }
    model = model_map.get(model_name)
    if not model:
        return jsonify({'message': 'Model not found'}), 404

    data = request.json
    if not data:
        return jsonify({'message': 'Data not found'}), 400

    try:
        new_item = model(**data)
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Item added', 'item': new_item.to_dict()}), 201
    except Exception as e:
        return jsonify({'message': 'Error adding item', 'error': str(e)}), 500