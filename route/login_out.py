from atomt import *


# 設置登入和登出路由
@app.route("/atomt/login", methods=["GET", "POST"])
def login():
    warning = False
    username = " "
    if request.method == "POST":
        # 從前端表單中獲取用戶名和密碼
        username = request.form["username"]
        password = request.form["password"]
        # 在數據庫中查找是否有該用戶
        user = User.query.filter_by(username=username).first()
        # 如果該用戶存在，且密碼正確，則將用戶名保存到 session 中
        if user and bcrypt.check_password_hash(user.password, password):
            session["username"] = username
        else:
            warning = True
    # 如果用戶已經登入，則跳轉到儀表盤頁面
    if session.get("username"):
        return redirect("/atomt/dashboard")
    else:
        # 否則顯示登入頁面
        return render_template(
            "./login.html", warning=warning, username=username, version=atomt_version
        )


@app.route("/atomt/logout")
def logout():
    # 從 session 中刪除用戶名
    session.pop("username", None)
    # 跳轉到登入頁面
    return redirect("/atomt/login")
