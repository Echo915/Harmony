let password = "";


// Obtains generated password from json link
async function fetchPassword() {
    try {
        const response = await fetch("http://127.0.0.1:8000/schedules/schedules.random_password/");
        const json_response = await response.json();
        password = json_response["random_password"];

        // Inserts random_password into the password field
        document.querySelector("input[name='password']").value = password;
        
    } catch(error) {
        console.log("Error: ", error);
    }
}


function copyText(text) {
    // Creates a temporary textarea element
    var textarea = document.createElement('textarea');
    textarea.value = text;

    // Sets the textarea to be non-editable to prevent unwanted interactions
    textarea.setAttribute("readonly", "");

    // Adds textarea to the DOM
    document.body.appendChild(textarea);

    // Selects the text in the textarea
    textarea.select();

    // Copies the selected text to the clipboard
    document.execCommand("copy");

    // Removes the temmporary textarea from the DOM
    document.body.removeChild(textarea);
}


// Copies password to clipboard
function copyPassword() {
    if (password !== "") {
        copyText(password);
    }
}


function openCurtain(curtain) {
    document.getElementById(`${curtain}`).style.width = "100%";
}


function closeCurtain(curtain) {
    document.getElementById(`${curtain}`).style.width = "0%";
}


function run_timer(container_id) {
    let current_time = new Date();
    const options = {weekday: "long", year: "numeric", month: "long", day: "numeric",
        hour: "numeric", minute: "numeric", second: "numeric", hour12: false,
    };

    const pseudo_now = current_time.toLocaleString('en-US', options).split(" at ");
    var now = `${pseudo_now[1]}   ${pseudo_now[0]}`;

    document.getElementById(container_id).innerHTML = now;
}


function get_random_color(diminish=1) {
    var red = Math.floor(Math.random() * 256); // Random red
    var green = Math.floor(Math.random() * 256); // Random green
    var blue = Math.floor(Math.random() * 256); // Random blue

    var random_color = `rgba(${red}, ${green}, ${blue}, ${diminish})`;
    return random_color;
}


function switchText(element, newText) {
    if (element.innerHTML != newText) {
        element.innerHTML = newText;
    }
}


setInterval(() => {
    run_timer("current-time");
}, 1000);


// Listens for checkbox to display pass seals
const padlocks_check_box = document.getElementById("pass-seal-op");
var padlock_container = document.getElementById("padlocks");

document.addEventListener("change", () => {
    if (padlocks_check_box.checked) {
        padlock_container.style.display = "block";
    } else {
        padlock_container.style.display = "none";
    }
});


var task_divs = document.querySelectorAll(".task-item"); // This is a list item
var padlocks = document.querySelectorAll(".padlock-body");

// Applies a random color to the background of each item in task_divs list
task_divs.forEach((task) => {
    let random_color = get_random_color(0.4);
    task.style.backgroundColor = random_color;
})

padlocks.forEach((padlock) => {
    let random_color = get_random_color(0.5);
    padlock.style.backgroundColor = random_color;
})
