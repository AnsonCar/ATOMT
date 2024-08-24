# 數據分析系統ATOMT。
## 需求： 

### dashbard
### ChatBox
- [ ] 連接GPT (open ai api)
- [ ] 存放對話紀錄 (save the data for user)
- [ ] 分清用戶 (chatbox have only id)
- [ ] 上下文連接

### 進度管理
#### 時間管理 Time Management 
- [ ] 時間表 TimeTable
- [ ] 目標 Target
    - [ ] day
    - [ ] week 
    - [ ] month 
    - [ ] yaer

### 設定
#### 個人設定
- [ ] 更改個人資料
- [ ] 補充個人資料

#### 用戶管理
- [x] 登入功能
- [x] 登出功能
- [ ] 權限
- [x] 新增用戶
- [x] 刪除用戶
- [x] 查看用戶
- [x] 更新資料



### 數據分析
- [ ] 數據文件上存 （flask）
- [ ] 數據文件下載 （flask）
- [ ] 數據清洗（table）
- [ ] 數據分析（GPT pandasAi）
- [ ] 機器學習（scikit-learn）
- [ ] 制作報告（main）
    - [x] 睇報告
    - [x] 新，刪，查，改
    - [x] report_ifo
    - [x] report_show
    - [ ] 上載圖片功能

## real website
- [x] 打包Dcoker
- [x] 送上Server 5008:5008
- [x] 連接domain (atomt.top)

先用flask同sqlite開發，將功能再模組化。
遲下轉為django同mysql。

新增功能：
1. 用ajax作交換數據。
2. atomt-frame轉換主題顏色
3. 下載db or sql file
4. 完善用戶設定
5. 完善報告功能
6. 文件上載功能
7. 電腦信息監測
8. 網頁命令行終端