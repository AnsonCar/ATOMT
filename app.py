# 引入必要的模塊
import os  # 與操作系統相關的模塊
import json  # 讀取json
from dotenv import load_dotenv  # 讀取 .env 文件的模塊

from flask import Flask  # Flask 框架的主要模塊
from flask import send_from_directory # 用作下載文件
from flask_sqlalchemy import SQLAlchemy  # Flask 中的 ORM 模塊
from flask_bcrypt import Bcrypt  # 實現密碼加密和解密的模塊

# 創建 Flask 應用程序
app = Flask(__name__)

# 獲取相對路徑和絕對路徑
__file__ = "."
basedir = os.path.abspath(os.path.dirname(__file__))

# 設置 SQLite 數據庫的位置
DATABASE = "sqlite:///" + os.path.join(basedir, "data/project.db")

# 配置數據庫相關參數
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # 禁止 Flask- SQLAlchemy 的修改跟蹤
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE  # 設置數據庫 URI

# 相片
app.config["ALLOWED_EXTENSIONS"] = {
    "txt",
    "pdf",
    "png",
    "jpg",
    "jpeg",
    "gif",
}  # 设置允许上传的文件类型

# 讀取 .env 文件中的環境變量
load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")  # 設置會話秘密鑰

# 創建 SQLAlchemy 實例
db = SQLAlchemy()

# 初始化 Flask 應用程序與 SQLAlchemy 實例
db.init_app(app)

# 創建 Bcrypt 實例，用於密碼加密
bcrypt = Bcrypt()
