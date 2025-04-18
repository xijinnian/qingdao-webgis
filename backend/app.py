from flask import Flask
from models import db
from routes.poi import poi_bp  # 新增导入
from models import User, POI  # 确保所有模型被加载

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///poi.db'
    app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # 新增JWT配置
    db.init_app(app)
    
    app.register_blueprint(poi_bp)  # 注册蓝图
    
    return app

app = create_app()


# app.py
from models import User, POI  # 明确导入所有模型

def create_app():
    app = Flask(__name__)
    # ...其他配置...
    db.init_app(app)
    
    with app.app_context():  # 确保在上下文中操作
        db.create_all()
    
    return app



# app.py
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    
    # JWT配置
    app.config['JWT_SECRET_KEY'] = 'your-super-secret-key'  # 生产环境应使用复杂密钥
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
    
    # 初始化JWT
    jwt = JWTManager(app)
    
    return app




# backend/app.py
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)  # 允许所有跨域请求
    # ...其他配置...