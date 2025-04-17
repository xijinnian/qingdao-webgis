from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, POI
from utils import admin_required

poi_bp = Blueprint('poi', __name__, url_prefix='/api')

@poi_bp.route('/pois', methods=['POST'])
@jwt_required()
@admin_required
def create_poi():
    data = request.get_json()
    
    # 验证必填字段
    required_fields = ['name', 'lng', 'lat']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "缺少必填字段"}), 400
    
    # 创建新景点
    new_poi = POI(
        name=data['name'],
        lng=float(data['lng']),  # 强制转换为浮点数
        lat=float(data['lat']),
        description=data.get('description', ''),
        images=data.get('images', [])
    )
    
    db.session.add(new_poi)
    db.session.commit()
    
    return jsonify(new_poi.to_dict()), 201