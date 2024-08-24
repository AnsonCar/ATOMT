from atomt import *


# ChatBox (GPT)
@app.route("/atomt/chatbox")
def ChatBox():
    return check_session(render_template("chatBox.html"))
