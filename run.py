# 從 app.py 中導入 Flask 應用程序對象 app
from app import *

# 從各個路由文件中導入相應的路由函數
from route.login_out import *
from route.dashboard import *
from route.chatbox import *
from route.user import *
from route.report import *

# 程式的入口點
if __name__ == "__main__":
    # 啟動 Flask 應用程序
    app.run(debug=True, host="0.0.0.0", port=5004)
