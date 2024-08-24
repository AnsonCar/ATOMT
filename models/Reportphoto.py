from models.model import *
from models.ReportDB import *

# Report photo 模型
class Reportphoto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reportid = db.Column(db.String(255), nullable=False)
    reportphoto = db.Column(db.String(255))


def add_report_photo(report_name, photo_filename):
    with app.app_context():
        # 檢查報告是否存在
        if not db.session.query(Report).filter_by(reportname=report_name).first():
            return False

        # 添加照片信息到 ReportPhoto 表中
        report_photo = Reportphoto(reportname=report_name, reportphoto=photo_filename)
        db.session.add(report_photo)
        db.session.commit()