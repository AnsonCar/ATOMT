from atomt import *


# Report
@app.route("/atomt/report", methods=["GET", "POST"])
def report():
    if request.method == "POST":
        way = request.form["way"]
        report_name = request.form["reportname"]
        report_about = request.form["reportabout"]
        if way == "add":
            add_report(report_name, report_about)
            file = os.path.join(basedir, f"data/report_data/{report_name}.json")
            # file2 = os.path.join(basedir, f"data/report_data/image/{report_name}")
            # if not os.path.exists(file2):
            #     os.mkdir(file2)
            with open(file, "w") as f:
                json.dump(add_json(report_name), f)
        elif way == "edit":
            report_id = request.form["reportid"]
            old_file = os.path.join(
                basedir, f"data/report_data/{find_report(report_id)}.json"
            )
            # old_file2 = os.path.join(basedir, f"data/report_data/image/{report_name}")
            edit_report(report_id, report_name, report_about)
            new_file = os.path.join(basedir, f"data/report_data/{report_name}.json")
            # new_file2 = os.path.join(basedir, f"data/report_data/image/{report_name}")
            os.rename(old_file, new_file)
            # os.rename(old_file2, new_file2)
            with open(new_file, "r") as f:
                j = json.load(f)
            j["Name"] = report_name
            with open(new_file, "w") as f:
                json.dump(j, f)
    with app.app_context():
        reports = Report.query.all()
    return check_session(render_template("./report/report.html", reports=reports))


@app.route("/atomt/delreport/<delname>")
def remove_report(delname):
    if session.get("username"):
        username = session.get("username")
        if username == "AnsonCar":
            delete_report(delname)
    return redirect("/atomt/report")


# Report_info
@app.route("/atomt/report_info/<reportId>")
def report_info(reportId):
    reportname = find_report(reportId)
    file = os.path.join(basedir, f"data/report_data/{reportname}.json")
    if os.path.exists(file):
        with open(file, "r") as f:
            datas = json.load(f)
    else:
        with open(file, "w") as f:
            json.dump(add_json(reportname), f)
        return redirect("/atomt/report")
    return check_session(
        render_template(
            "./report/report_info.html",
            datas=datas,
            # photo_path=url_for("static", filename="images/"),
            reportId=reportId,
        )
    )


# Report_show
@app.route("/atomt/report_show/<reportId>")
def report_show(reportId):
    reportname = find_report(reportId)
    file = os.path.join(basedir, f"data/report_data/{reportname}.json")

    image = os.path.join(basedir, f"data/report_data/image/{reportname}")

    if os.path.exists(file):
        with open(file, "r") as f:
            datas = json.load(f)
    else:
        with open(file, "w") as f:
            json.dump(add_json(reportname), f)
        return redirect("/atomt/report")
    return check_session(
        render_template(
            "./report/report_show.html", datas=datas, reportId=reportId, path=image
        )
    )


@app.route("/atomt/report_json/<reportId>", methods=["POST"])
def json_handler(reportId):
    data = json.loads(request.get_json())
    reportname = find_report(reportId)
    # image = os.path.join(basedir, f"data/report_data/image/{reportname}")
    file = os.path.join(basedir, f"data/report_data/{reportname}.json")

    # if not os.path.exists(image):
    #     os.makedirs(image)

    if os.path.exists(file):
        with open(file, "w") as f:
            json.dump(data, f)
    # try:
    #     files = request.files.getlist("file")
    # except:
    #     pass
    # for file in files:
    #     if file:
    #         filename = secure_filename(file.filename)
    #         file.save(os.path.join(image, filename))
    # return files
    return redirect("/atomt/report")


# json格式
def add_json(reportname):
    j = {
        "Name": reportname,
        "box1": [
            ["chapter", "", 0],
            ["title", "", 1],
            ["second_title", "", 2],
            ["content", "", 3]
            # ["image", "", 4]
        ],
        "box2": [
            ["chapter", "", 0],
            ["title", "", 1],
            ["content", "", 2]
            # ["image", "", 3]
        ],
    }
    return j


@app.route("/atomt/report_download/<reportId>")
def download_file(reportId):
    reportname = find_report(reportId)
    file = os.path.join(basedir, "data/report_data/")
    return send_from_directory(file, f"{reportname}.json", as_attachment=True)


@app.route("/atomt/DB_download")
def download_DB():
    file = os.path.join(basedir, "data/")
    return send_from_directory(file, "project.db", as_attachment=True)

