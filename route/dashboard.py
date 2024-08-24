from atomt import *
import psutil

# Dashboard
@app.route("/atomt/dashboard")
def dashboard():
    return check_session(render_template("dashboard.html", pc_info=pc_info()))

@app.route("/atomt/pc_info",methods=["POST"])
def getPcInfo():
    # CPU的使用情况
    cpu_percent = psutil.cpu_percent()
    # interval=1
    # 内存使用情况
    mem_info = psutil.virtual_memory()
    # 磁盘的使用情况
    disk_usage = psutil.disk_usage('/')
    return {
        "CPU": cpu_percent,
        "Memory": mem_info.percent,
        # "Dick": disk_usage.percent
    }

def pc_info():
    # CPU的使用情况
    cpu_percent = psutil.cpu_percent()
    # interval=1
    # 内存使用情况
    mem_info = psutil.virtual_memory()
    # 磁盘的使用情况
    disk_usage = psutil.disk_usage('/')
    return {
        "CPU_usage":f'{cpu_percent}',
        "Memory":{
            "Total_memory": f"{mem_info.total / (1024**3):.2f}",
            "Used_memory": f"{mem_info.used / (1024**3):.2f}",
            "Memory_usage":  mem_info.percent
        },
        "Dick":{
            "Total_disk_space": f"{disk_usage.total / (1024**3):.2f}",
            "Used_disk_space": f"{disk_usage.used / (1024**3):.2f}",
            "Disk_usage": f"{disk_usage.percent}"
        }
    }
    
