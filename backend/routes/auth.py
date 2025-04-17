from flask import request, jsonify
from flask_jwt_extended import create_access_token
from models import User
from . import auth_bp  # 假设蓝图已在文件顶部定义

@auth_bp.route('/login', methods=['POST'])
def login():
    # 获取请求数据
    data = request.get_json()
    
    # 验证必填字段
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "必须提供用户名和密码"}), 400
    
    # 查询用户
    user = User.query.filter_by(username=data['username']).first()
    
    # 验证用户存在且密码正确
    if not user or not user.check_password(data['password']):
        return jsonify({"error": "用户名或密码错误"}), 401
    
    # 构造JWT声明
    additional_claims = {
        "is_admin": user.is_admin,
        "user_id": user.id
    }
    
    # 生成访问令牌
    access_token = create_access_token(
        identity=user.username,
        additional_claims=additional_claims
    )
    
    return jsonify({
        "access_token": access_token,
        "is_admin": user.is_admin
    }), 200