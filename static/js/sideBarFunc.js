function accOpen(id) {
    const item = document.getElementById(id);
    if (item.className.indexOf("w3-show") == -1) {
        item.className += " w3-show";
    } else {
        item.className = item.className.replace(" w3-show", "");
    }
}

function side_open() {
    document.getElementById("main").style.marginLeft = "256px";
    document.getElementById("sideBar").style.display = "block";
    document.getElementById("topBar_btn").onclick = side_close;
}

function side_close() {
    document.getElementById("main").style.marginLeft = "0";
    document.getElementById("sideBar").style.display = "none";
    document.getElementById("topBar_btn").onclick = side_open;
}