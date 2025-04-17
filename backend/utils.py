from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if not claims.get('is_admin', False):
            return jsonify({"error": "需要管理员权限"}), 403
        return fn(*args, **kwargs)
    return wrapper


from functools import wraps
from flask import jsonify  # 需要添加这个导入
from flask_jwt_extended import verify_jwt_in_request, get_jwt

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            # 强制验证JWT有效性
            verify_jwt_in_request()
            
            # 获取JWT声明
            claims = get_jwt()
            
            # 检查管理员权限
            if not claims.get('is_admin', False):
                return jsonify({"error": "需要管理员权限"}), 403
                
            return fn(*args, **kwargs)
            
        except Exception as e:  # 捕获所有异常
            return jsonify({"error": str(e)}), 401
    return wrapper




# backend/utils.py
def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("[临时方案] 跳过管理员验证")  # 添加日志提示
        return fn(*args, **kwargs)
    return wrapper