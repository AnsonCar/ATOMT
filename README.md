# ATOMT System

## 項目介紹
> 學生時期的功課

本項目需要使用pytho flask 建造一個網站。
同時線上項目，成為real website（不只是localhost）。  
本項目為一個數據分析系統，名叫ATOMT SYSTEM，是五位成員名字的首字母。

## 基本設定
### 安裝python虛擬環境
```shell 
pytohn3 -m venv .venv
source ./.venv/bin/activate
```

### 安裝依賴庫
```shell
pip install --upgrade pip
pip install python-dotenv
pip install flask_sqlalchemy
pip install flask-bcrypt
pip install psutil
```

### 運行flask server
```shell
python3 run.py
```

## 項目結構
```
.
├── .env                    隱藏文件（存放敏感資料）
├── .dockerignore           生成docker不加入的文件
├── Dockerfile              生成Dcoker容器文件
├── README.md               簡介       
├── app.py                  基本flask及其他庫引入
├── atomt.py                ATOMT路由（main）
├── run.py                  運行flask server
├── templates               動態文件（html模版）
├── test                    測試和舊版本文件
├── toDocker.sh
├── data                    存在數據相關文件
├── doc                     存放資料文件
├── models                  存在數據庫
├── nginx.conf
├── route
└── static                  靜態文件
    ├── css                 css文件
    ├── font-awesome-4.7.0  圖標icon
    ├── image               圖片
    └── js                  javascript文件
```