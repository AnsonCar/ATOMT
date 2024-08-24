# 導入一些用於操作文件和時間的模塊
import shutil
import datetime

# 從 app.py 中導入所有模塊
from app import *

# 創建數據庫表
with app.app_context():
    db.create_all()