from flask import jsonify
from models import Competition, TeachInfo, User, Video

def query_model(model, item_id=None):
    if item_id:
        item = model.query.get(item_id)
        if not item:
            return jsonify({'message': 'Item not found'}), 404
        if model == Competition:
            return jsonify({
                'cId': item.cId,
                'cName': item.cName,
                'cTime': item.cTime.strftime('%Y-%m-%d %H:%M:%S'),
                'cType': item.cType,
                'Place': item.Place
            })
        elif model == TeachInfo:
            return jsonify({
                'tId': item.tId,
                'tName': item.tName,
                'tType': item.tType,
                'tContact': item.tContact,
                'tResume': item.tResume
            })
        elif model == User:
            return jsonify({
                'Id': item.Id,
                'Name': item.Name,
                'Password': item.Password,
                'Account': item.Account,
                'Level': item.Level,
                'Mail': item.Mail,
                'Phone': item.Phone,
                'Age': item.Age,
                'Gender': item.Gender,
                'Birthday': item.Birthday,
                'Dance_age': item.Dance_age
            })
        elif model == Video:
            return jsonify({
                'vId': item.vId,
                'Score': str(item.Score),
                'vTime': str(item.vTime),
                'Style': item.Style,
                'Introduction': item.Introduction
            })
    else:
        items = model.query.all()
        if model == Competition:
            return jsonify([{
                'cId': item.cId,
                'cName': item.cName,
                'cTime': item.cTime.strftime('%Y-%m-%d %H:%M:%S'),
                'cType': item.cType,
                'Place': item.Place
            } for item in items])
        elif model == TeachInfo:
            return jsonify([{
                'tId': item.tId,
                'tName': item.tName,
                'tType': item.tType,
                'tContact': item.tContact,
                'tResume': item.tResume
            } for item in items])
        elif model == User:
            return jsonify([{
                'Id': item.Id,
                'Name': item.Name,
                'Password': item.Password,
                'Account': item.Account,
                'Level': item.Level,
                'Mail': item.Mail,
                'Phone': item.Phone,
                'Age': item.Age,
                'Gender': item.Gender,
                'Birthday': item.Birthday,
                'Dance_age': item.Dance_age
            } for item in items])
        elif model == Video:
            return jsonify([{
                'vId': item.vId,
                'Score': str(item.Score),
                'vTime': str(item.vTime),
                'Style': item.Style,
                'Introduction': item.Introduction
            } for item in items])
    return jsonify([])
