# 從 app.py 中導入所有模塊
from app import *

# 從各個models.py文件中導入相應的數據庫
from models.UserDB import *
from models.ReportDB import *

# 導入flask各種組件
from flask import request, session, redirect, render_template, url_for

# 定義 ATOMT 的版本號
atomt_version = "v20230630v3.2.3"


# 檢查用戶是否已經登入
def check_session(fn):
    return fn if session.get("username") else redirect("/atomt/login")


# 設置路由，當網址為 "/" 或 "/atomt" 時，執行 home 函數
@app.route("/")
@app.route("/atomt")
def home():
    # 如果用戶已經登入，則跳轉到儀表盤頁面
    return check_session(redirect("/atomt/dashboard"))


@app.route("/test")
def test():
    return render_template("/test.html")


from werkzeug.utils import secure_filename


@app.route("/test/image", methods=["POST"])
def testimage():
    upload_dir = os.path.join(os.getcwd(), "data/report_data/image")
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    files = request.files.getlist("file")
    for file in files:
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(upload_dir, filename))
    return "Files uploaded successfully!"
