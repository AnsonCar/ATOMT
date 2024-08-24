from models.model import *


# User 模型，用於定義用戶數據庫
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String)


# 定義添加用戶、刪除用戶和修改用戶的函數
def add_user(user_name, user_password, user_email):
    with app.app_context():
        # 將密碼用 bcrypt 加密
        user_password = bcrypt.generate_password_hash(password=user_password)
        # 檢查用戶名是否已經存在
        if db.session.query(User).filter_by(username=user_name).first():
            pass
        else:
            # 如果用戶名不存在，則添加新用戶
            user = User(
                username=user_name,
                password=user_password,
                email=user_email,
            )
            db.session.add(user)
            db.session.commit()
            
add_user("admin","admin","admin")

def delete_user(user_name):
    with app.app_context():
        # 查找要刪除的用戶
        user = User.query.filter_by(username=user_name).first()
        if user:
            # 如果用戶存在，則刪除用戶
            db.session.delete(user)
            db.session.commit()


def edit_user(user_id, user_name, user_email):
    with app.app_context():
        # 查找要修改的用戶
        user = User.query.filter_by(id=user_id).first()
        if user:
            # 如果用戶存在，則修改用戶名和郵箱
            user.username = user_name
            user.email = user_email
            db.session.commit()
