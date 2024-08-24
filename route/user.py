from atomt import *


# User
@app.route("/atomt/user", methods=["GET", "POST"])
def user():
    if request.method == "POST":
        way = request.form["way"]
        user_name = request.form["username"]
        user_email = request.form["useremail"]
        if way == "add":
            password = request.form["pass_word"]
            add_user(user_name, password, user_email)
        elif way == "edit":
            user_id = request.form["userid"]
            edit_user(user_id, user_name, user_email)

    with app.app_context():
        users = User.query.all()

    return check_session(
        render_template(
            "userManagement.html",
            users=users,
            username=session.get("username"),
        )
    )


@app.route("/atomt/deluser/<delname>")
def remove_user(delname):
    if session.get("username"):
        username = session.get("username")
        if username == "AnsonCar":
            delete_user(delname)
    return redirect("/atomt/user")
