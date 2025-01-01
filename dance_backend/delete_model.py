# file: delete_model.py

from flask import jsonify
from models import db, Competition, TeachInfo, User, Video

def delete_item(model_name, item_id):
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

    try:
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Item deleted', 'item': item.to_dict()}), 200
    except Exception as e:
        return jsonify({'message': 'Error deleting item', 'error': str(e)}), 500