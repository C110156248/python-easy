from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from update_model import update_item  
from delete_model import delete_item 
from query_model import query_model
from add_model import add_item
from models import db, Competition, TeachInfo, User, Video

# 載入環境變數
load_dotenv()

app = Flask(__name__)
CORS(app)  # 啟用 CORS

# 設定資料庫 URI
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_username}:{db_password}@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # 初始化資料庫
migrate = Migrate(app, db)  # 初始化 Flask-Migrate

@app.route('/')
def serve():
    return render_template('index.html')

@app.route('/manage')
def manage():
    return render_template('manage.html')

# 查詢資料庫
@app.route('/query/<model_name>', methods=['GET'])
@app.route('/query/<model_name>/<int:item_id>', methods=['GET'])
def get_items(model_name, item_id=None):
    model_map = {
        'competitions': Competition,
        'teachinfos': TeachInfo,
        'users': User,
        'videos': Video
    }
    model = model_map.get(model_name)
    if not model:
        return jsonify({'message': 'Model not found'}), 404
    return query_model(model, item_id)

# 新增資料
@app.route('/add/<model_name>', methods=['POST'])
def add_item_route(model_name):
    return add_item(model_name)

# 更新資料
@app.route('/update/<model_name>/<int:item_id>', methods=['PUT'])
def update_item_route(model_name, item_id):
    return update_item(model_name, item_id)

# 刪除資料
@app.route('/delete/<model_name>/<int:item_id>', methods=['DELETE'])
def delete_item_route(model_name, item_id):
    return delete_item(model_name, item_id)

# 錯誤處理器
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'message': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'message': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)