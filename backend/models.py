from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class POI(db.Model):  # <-- 第3行类定义
    # 注意：以下所有类成员必须缩进！
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lng = db.Column(db.Float, nullable=False)  # 经度
    lat = db.Column(db.Float, nullable=False)  # 纬度
    description = db.Column(db.Text)
    images = db.Column(db.JSON)  # 存储图片路径数组
    
    def to_dict(self):  # 方法也需要缩进
        return {
            "id": self.id,
            "name": self.name,
            "lng": self.lng,
            "lat": self.lat,
            "description": self.description,
            "images": self.images or []
        }

from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)