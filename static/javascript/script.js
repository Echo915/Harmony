function crossMenu() {
    var icon = document.querySelector(".menu-icon");
    var sideBar = document.querySelector(".side-nav-panel");

    icon.classList.toggle("cross-menu-icon");
    sideBar.classList.toggle("side-nav-panel-switch");
}

function hideAll() {
    var all = document.querySelectorAll("*");
    console.log(all);
    all.forEach(element => {
        element.classList.remove("show");
    });
}

function openCurtain(content) {
    var overlay_content = document.getElementById("overlay-content");
    var mini_form = document.getElementById(`${content}`);
    //mini_form.style.display = "block";

    // Clones mini_form including its children
    var mini_form_clone = mini_form.cloneNode(true);
    mini_form_clone.style.display = "block"

    // Appends mini_form_clone into overlay content
    overlay_content.appendChild(mini_form_clone);

    document.getElementById("overlay").style.width = "100%";
    
}

function closeCurtain() {
    document.getElementById("overlay").style.width = "0%";
    var overlay_content = document.getElementById("overlay-content");
    overlay_content.innerHTML = "";
}

function toggle_show_item(item_id) {
    let display = document.getElementById(item_id).style.display;
    if (display === "block") {
        document.getElementById(item_id).style.display = "none";
    }
    else {
        document.getElementById(item_id).style.display = "block";
    }
}
