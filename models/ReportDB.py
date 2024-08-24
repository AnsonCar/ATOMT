from models.model import *

# Report 模型，用於定義報告數據庫
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reportname = db.Column(db.String(255), nullable=False)
    reportabout = db.Column(db.String(255))


# 定義添加報告、刪除報告和修改報告的函數
def add_report(report_name, report_about):
    with app.app_context():
        # 檢查報告名是否已經存在
        if db.session.query(Report).filter_by(reportname=report_name).first():
            pass
        else:
            # 如果報告名不存在，則添加新報告
            report = Report(reportname=report_name, reportabout=report_about)
            db.session.add(report)
            db.session.commit()


def delete_report(reportname):
    reportname = reportname.strip()
    with app.app_context():
        # 查找要刪除的報告
        report = Report.query.filter_by(reportname=reportname).first()
        if report:
            # 如果報告存在，則刪除報告，並將報告文件移動到 del 目錄中
            db.session.delete(report)
            db.session.commit()
            file = os.path.join(basedir, f"data/report_data/{reportname}.json")
            # file2 = os.path.join(basedir, f"data/report_data/image/{reportname}")
            now = datetime.datetime.now()
            formatted = now.strftime("%y%m%d_%H%M%S")
            del_path = os.path.join(
                basedir, f"data/report_data/del/{reportname}_time{formatted}.json"
            )
            # del_path2 = os.path.join(
            #     basedir, f"data/report_data/del/{reportname}_time{formatted}"
            # )
            shutil.move(file, del_path)
            # shutil.move(file2, del_path2)


def edit_report(report_id, report_name, report_about):
    with app.app_context():
        # 查找要修改的報告
        report = Report.query.filter_by(id=report_id).first()
        if report:
            # 如果報告存在，則修改報告名和報告描述
            report.reportname = report_name
            report.reportabout = report_about
            db.session.commit()


def find_report(report_id):
    with app.app_context():
        # 查找指定 ID 的報告
        report = Report.query.filter_by(id=report_id).first()
        if report:
            return report.reportname


