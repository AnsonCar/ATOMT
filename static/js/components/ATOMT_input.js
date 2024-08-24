// 註冊到文檔中
customElements.define('atomt-input',
    class ATOMT_INPUT extends HTMLElement {
        constructor() {
            super();
        }

        // 首次被插入文档 DOM
        connectedCallback() {
            const type = this.getAttribute("type")
            const value = this.getAttribute("value") !== NaN ? this.getAttribute("value") : "1234";
            const id = this.getAttribute("id")

            const template = document.createElement("template");
            template.innerHTML += `<div style="width: 100%;" class="w3-large">${type}</div>`
            template.innerHTML += `<div class="w3-col" id="self">`

            if (type === "chapter") {
                template.innerHTML += `
                    <div class="w3-rest w3-round">
                        <input required class="w3-input w3-border w3-round" type="text" value="${value}" >
                    </div>
                `;
            } else if (type === "second_title" || type === "title" || type === "content") {
                template.innerHTML += `
                    <div class="w3-col w3-round w3-right  w3-margin-left" style="width:48px">
                        <div class="w3-button w3-round w3-right w3-red w3-hover-text-red"
                            style="width:48px" onclick="moveInput('${id}')">
                            <i class="fa fa-times"></i>
                        </div>
                    </div>
                    <div class="w3-rest w3-round">
                        <input required class="w3-input w3-border w3-round" type="text" value="${value}">
                    </div>
                `;
            } else if (type === "content" ) {
                template.innerHTML += `
                    <div class="w3-col w3-round w3-right  w3-margin-left" style="width:48px">
                        <div class="w3-button w3-round w3-right w3-red w3-hover-text-red" style="width:48px" onclick="moveInput('${id}')">
                            <i class="fa fa-times"></i>
                        </div>
                    </div>

                    <div class="w3-rest w3-round">
                        <textarea class="w3-input w3-border w3-round" rows="1" style="resize:none">${value}</textarea>
                    </div>
                `;
            } else {
                template.innerHTML += `
                    <div class="w3-col w3-round w3-right  w3-margin-left" style="width:48px">
                        <div class="w3-button w3-round w3-right w3-red w3-hover-text-red" style="width:48px">
                        <!-- onclick="moveInput('${id}')" -->
                            <i class="fa fa-times"></i>
                        </div>
                    </div>
                    <div class="w3-col w3-round w3-right  w3-margin-left" style="width:48px">
                        <div class="w3-button w3-round w3-right w3-theme-l1 w3-hover-deep-purple"
                            style="width:48px" onclick="accOpen('{{key}}_{{box[1]}}')">
                            <i class="fa fa-eye"></i>
                        </div>
                    </div>
                    <div class="w3-rest w3-round">
                        <input class="w3-input w3-border w3-round" type="file" name="file">
                    </div>
                `
            }

            template.innerHTML += `<br></div>`

            try {
                this.appendChild(template.content.cloneNode(true));

                let textarea = this.querySelector('textarea');
                textarea.addEventListener('input', (e) => {
                    textarea.style.height = '40.5px';
                    textarea.style.height = e.target.scrollHeight + 'px';
                });
                let input = this.querySelector('input');
                input.addEventListener('input', (e) => {
                    input.style.height = '40.5px';
                    input.style.height = e.target.scrollHeight + 'px';
                });
            } catch (error) {
            }

            const text = this.querySelector(".w3-input.w3-border.w3-round");
            text.addEventListener('input', (event) => {
                document.querySelector(`#${id}`).setAttribute("value", text.value)
            })
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