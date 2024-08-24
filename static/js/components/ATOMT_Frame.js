// 註冊到文檔中
customElements.define('atomt-frame',
    class ATOMT_Frame extends HTMLElement {
        constructor() {
            super();
        }

        // 首次被插入文档 DOM
        connectedCallback() {
            let ATOMT_Tilte = this.getAttribute("title")
            let ATOMT_Hover = this.getAttribute("hover")
            let SideBar_Id = ATOMT_Tilte.replace(" ", "");

            document.title = `ATOMT ${ATOMT_Tilte}`

            const template = document.createElement("template");
            // Sibe Bar
            template.innerHTML = `
                <div id="sideBar" class="w3-sidebar w3-bar-block w3-card-4 w3-large  w3-animate-left w3-theme-l1">
                    <a id="sideBar_btn" class="w3-button  w3-large w3-right ${ATOMT_Hover}" onclick="side_close()">
                        ×
                        <!-- w3-hide-large -->
                    </a>
                    
                    <a id="Dashboard" href="/atomt/dashboard" class="w3-bar-item w3-button ${ATOMT_Hover}">
                        <i class="fa fa-tachometer w3-xlarge"></i>
                        Dashboard
                    </a>
                    
                    <a id="ChatBox" href="/atomt/chatbox" class="w3-bar-item w3-button ${ATOMT_Hover}">
                        <i class='fa fa-comment w3-xlarge'></i>
                        ChatBox
                    </a>

                    <button class="w3-bar-item w3-button ${ATOMT_Hover}"
                        onclick="accOpen('DSA')">
                        <i class='fa fa-pie-chart w3-xlarge'></i>
                        DSA
                        <i class="fa fa-caret-down"></i>
                    </button>
                    <div id="DSA" class="w3-hide w3-show">
                        
                        <a href="DataCleaning" class="w3-bar-item w3-button ${ATOMT_Hover}">
                            <i class='fa fa-industry w3-xlarge' style="padding-left: 20px;"></i>
                            Data Cleaning
                        </a>
                        
                        <a id="DataAnalysis" href="#" class="w3-bar-item w3-button ${ATOMT_Hover}">
                            <i class='fa fa-bar-chart w3-xlarge' style="padding-left: 20px;"></i>
                            Data Analysis
                        </a>
                        
                        <a id="MachineLearning" href="#" class="w3-bar-item w3-button ${ATOMT_Hover}">
                            <i class='fa fa-graduation-cap w3-xlarge' style="padding-left: 20px;"></i>
                            Machine Learning
                        </a>
                        
                        <a id="Report" href="/atomt/report" class="w3-bar-item w3-button ${ATOMT_Hover}">
                            <i class='fa fa-book w3-xlarge' style="padding-left: 20px;"></i>
                            Report
                        </a>

                    </div>

                    <button class="w3-bar-item w3-button ${ATOMT_Hover}"
                        onclick="accOpen('Setting')">
                        <i class='fa fa-cog w3-xlarge'></i>
                        Setting
                        <i class="fa fa-caret-down"></i>
                    </button>
                    <div id="Setting" class="w3-hide w3-show">

                        <a href="/atomt/user" class="w3-bar-item w3-button ${ATOMT_Hover}">
                            <i class='fa fa-address-card-o w3-xlarge' style="padding-left: 20px;"></i>
                            Personal Info
                        </a>

                        <a id="UserManagement" href="/atomt/user" class="w3-bar-item w3-button ${ATOMT_Hover}">
                        <!-- w3-theme -->
                            <i class='fa fa-address-card w3-xlarge' style="padding-left: 20px;"></i>
                            User Management
                        </a>

                    </div>

                    <!-- Logout -->
                    <a id="Logout" href="/atomt/logout" class="w3-bar-item w3-button ${ATOMT_Hover} w3-display-bottommiddle">
                        <i class='fa fa-sign-out w3-xlarge'></i>
                        Logout
                    </a>
                </div>
            `;
            // Topbar & Main
            template.innerHTML += `
                <div class="w3-main" id="main">
                    <!-- topbar -->
                    <div id="topBar" class="w3-top w3-container w3-theme-l2 w3-card w3-xlarge w3-padding ">
                        <button id="topBar_btn" class="w3-button w3-round w3-small ${ATOMT_Hover}" onclick="side_open()" id="open">
                            <i class="fa fa-bars w3-large"></i>
                        </button>
                        ${ATOMT_Tilte}
                    </div>

                    <!-- main -->
                    <div id="ATOMT_Main" class="w3-container w3-main"  style="padding-top: 65px;">
                
                    </div>
                </div>
            `;

            this.appendChild(template.content.cloneNode(true));
            this.querySelector("#ATOMT_Main").appendChild(document.querySelector(".main"))

            // check  window szie to open sibebar
            const width = window.innerWidth;
            let sideBarBtn = this.querySelector("#sideBar_btn");
            let topBarBtn = this.querySelector("#topBar_btn");
            if (width > 1280) {
                topBarBtn.click();
            }
            try {
                this.querySelector(`#${SideBar_Id}`).className += " w3-theme";
            } catch (error) {

            }
        }

        // 从文档 DOM 中删除时
        disconnectedCallback() {

        }

        // 被移动到新的文档时 (一般是 iframe)
        adoptedCallback() {

        }

        // 增加、删除、修改自身属性时
        attributeChangedCallback() {

        }
    }
);