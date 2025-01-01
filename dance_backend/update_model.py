from flask import jsonify, request
from models import db, Competition, TeachInfo, User, Video

def update_item(model_name, item_id):
    model_map = {
        'competitions': Competition,
        'teachinfos': TeachInfo,
        'users': User,
        'videos': Video
    }
    model = model_map.get(model_name)
    if not model:
        return jsonify({'message': 'Model not found'}), 404

    item = model.query.get(item_id)
    if not item:
        return jsonify({'message': 'Item not found'}), 404

    data = request.json
    if not data:
        return jsonify({'message': 'Data not found'}), 400

    try:
        for key, value in data.items():
            setattr(item, key, value)
        db.session.commit()
        return jsonify({'message': 'Item updated', 'item': item.to_dict()}), 200
    except Exception as e:
        return jsonify({'message': 'Error updating item', 'error': str(e)}), 500