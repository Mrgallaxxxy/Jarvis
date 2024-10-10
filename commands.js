document.addEventListener("DOMContentLoaded", function () {
    const minimizeBtn = document.querySelector(".minimize");
    const maximizeBtn = document.querySelector(".maximize");
    const closeBtn = document.querySelector(".close");

    const MainMenu = document.querySelector("#main");
    const SettingsMenu = document.querySelector("#settings");
    const CommandsMenu = document.querySelector("#commands");

    const widthScreen = document.getElementById("width");
    const heightScreen = document.getElementById("height");
    const applyBtn = document.getElementById("apply-button");

    if (applyBtn) {
        applyBtn.addEventListener("click", () => {
            var widthS = widthScreen.value;
            var heightS = heightScreen.value;

            if (widthS < 400) {
                widthScreen.value = 400;
            } if (widthS > 2999) {
                widthS = 2999;
            }

            if (heightS < 400) {
                heightScreen.value = 400;
            } if (heightS > 2999) {
                heightScreen.value = 2999;
            }

            window.pywebview.api.save_screen_size(widthScreen.value, heightScreen.value)
        });
    }

    document.addEventListener("keydown", function (event) {
        if (event.key === "F5") {
            location.reload();
        }
    });



    // function loadHistoryFromFile() {
    //     fetch("./temp/chat_history.txt")
    //         .then(response => response.text())
    //         .then(data => {
    //             const historyPanel = document.querySelector(".history-panel");
    //             historyPanel.innerHTML = data;
    //         })
    //         .catch(error => console.error("Ошибка в загрузке истории:", error));
    // }

    MainMenu.addEventListener("click", () => {
        window.pywebview.api.load_html("index.html");
    });

    SettingsMenu.addEventListener("click", () => {
        window.pywebview.api.load_html("settings.html");
    });

    CommandsMenu.addEventListener("click", () => {
        window.pywebview.api.load_html("comscreen12.html");
    });
    
    // MainMenu.addEventListener("click", () => {
    //     window.pywebview.api.load_html("index.html");
    // });

    function add_assistant_message(message) {
        // var history_panel = document.querySelector('.history-panel');
        // var new_message = `<div class="message from-assistant">${message}</div>`;
        // history_panel.innerHTML += new_message;
        // window.pywebview.api.save_chat_history(`${history_panel.innerHTML}\n`);
    }

    function add_people_message(message) {
        // var history_panel = document.querySelector('.history-panel');
        // var new_message = `<div class="message from-user">${message}</div>`;
        // history_panel.innerHTML += new_message;
        // window.pywebview.api.save_chat_history(`${history_panel.innerHTML}\n`);
    }

    minimizeBtn.addEventListener("click", () => {
        window.pywebview.api.minimize();
    });

    maximizeBtn.addEventListener("click", () => {
        window.pywebview.api.maximize();
    });

    closeBtn.addEventListener("click", () => {
        window.pywebview.api.close();
    });

    loadHistoryFromFile();
});

function loadHistoryFromFile() {
    fetch("./temp/chat_history.txt")
        .then(response => response.text())
        .then(data => {
            const historyPanel = document.querySelector(".history-panel");
            historyPanel.innerHTML = data;
        })
        .catch(error => console.error("Ошибка в загрузке истории:", error));
}

function add_assistant_message(message) {
    // var history_panel = document.querySelector('.history-panel');
    // var new_message = `<div class="message from-assistant">${message}</div>`;
    // history_panel.innerHTML += new_message;
    // window.pywebview.api.save_chat_history(`${history_panel.innerHTML}\n`);
}

function add_people_message(message) {
    // var history_panel = document.querySelector('.history-panel');
    // var new_message = `<div class="message from-user">${message}</div>`;
    // history_panel.innerHTML += new_message;
    // window.pywebview.api.save_chat_history(`${history_panel.innerHTML}\n`);
}