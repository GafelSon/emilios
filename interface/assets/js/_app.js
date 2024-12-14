const asciiArt = `
███████╗███╗░░░███╗██╗██╗░░░░░██╗░█████╗░░██████╗
██╔════╝████╗░████║██║██║░░░░░██║██╔══██╗██╔════╝
█████╗░░██╔████╔██║██║██║░░░░░██║██║░░██║╚█████╗░
██╔══╝░░██║╚██╔╝██║██║██║░░░░░██║██║░░██║░╚═══██╗
███████╗██║░╚═╝░██║██║███████╗██║╚█████╔╝██████╔╝
╚══════╝╚═╝░░░░░╚═╝╚═╝╚══════╝╚═╝░╚════╝░╚═════╝░
    `;
console.log(asciiArt);

function msgAlert(message) {
    function remover() {
        alertDiv.remove();
        if (messagesContainer.children.length === 0) {
            messagesContainer.remove();
        }
    }
    const alertDiv = document.createElement("div");
    alertDiv.className = "messages";
    alertDiv.innerHTML = `
        <button class='close-alert'>x</button>
        <div>
            <h5>⚠︎ Message</h5>
            <div class="msg-content">${message}</div>
        </div>
    `;

    const closeButton = alertDiv.querySelector(".close-alert");
    closeButton.addEventListener("click", remover);

    let messagesContainer = document.querySelector(".messages-container");
    if (!messagesContainer) {
        messagesContainer = document.createElement("div");
        messagesContainer.className = "messages-container";
        document.body.appendChild(messagesContainer);
    }
    messagesContainer.appendChild(alertDiv);
    setTimeout(() => {
        alertDiv.classList.add("animation");
        setTimeout(() => {
            remover();
        }, 500);
    }, 4000);
}

class LoadingPage extends HTMLElement {
    connectedCallback() {
        this.fontFamily = "none";
        this.style.position = "fixed";
        this.style.top = "0";
        this.style.left = "0";
        this.style.width = "100%";
        this.style.margin = "auto";
        this.style.height = "100%";
        this.style.backgroundColor = "rgba(0, 0, 0)";
        this.style.display = "flex";
        this.style.justifyContent = "center";
        this.style.alignItems = "center";
        this.style.zIndex = "102";
    }
}
customElements.define("loading-page", LoadingPage);

function loading() {
    window.requestAnimationFrame(() => {
        const dynamicLoad = document.createElement("loading-page");
        const preLoad = document.createElement("pre");
        preLoad.style.textAlign = "center";
        preLoad.textContent = asciiArt + "Loading...";
        document.body.appendChild(dynamicLoad);
        dynamicLoad.appendChild(preLoad);

        setTimeout(() => {
            preLoad.classList.add("glitch");
        }, 2000);

        setTimeout(() => {
            document.body.removeChild(dynamicLoad);
        }, 2500);
    });
}

document.addEventListener("DOMContentLoaded", loading);

document.addEventListener("DOMContentLoaded", () => {
    const container = document.getElementById("ascii");
    const preElement = document.createElement("pre");
    const toggleSwitch = document.getElementById("toggleSwitch");
    const statusText = document.getElementById("status");
    const alertBox = document.getElementById("alert");
    const rangeInput = document.getElementById("vol");
    const rangeLabel = document.getElementById("rangeLabel");
    const logsContainer = document.getElementById("logs");
    const closeButton = document.getElementById("close");
    const openButton = document.getElementById("open");
    const loggingDiv = document.querySelector(".logging");
    const loggingContent = document.querySelector(".log-content");
    const form = document.querySelector("form");
    const phoneInput = form.querySelector('input[placeholder="CellPhone"]');
    const timeElement = document.getElementById("time");
    const infoButton = document.querySelector('icon')

    function updateClock() {
        if (!timeElement) {
            console.error("Element with ID 'time' not found.");
            return;
        }
        const now = new Date();
        const options = {
            year: "numeric",
            month: "long",
            day: "numeric",
            hour: "numeric",
            minute: "numeric",
            second: "numeric",
        };
        const formattedTime = now.toLocaleString("en-US", options);

        timeElement.textContent = "~ " + formattedTime + " ~";
    }
    updateClock();
    setInterval(updateClock, 1000);

    preElement.style.fontFamily = "none";
    preElement.textContent = asciiArt;
    container.appendChild(preElement);

    // Toggle offline/online mode
    toggleSwitch.addEventListener("change", () => {
        msgAlert(toggleSwitch.checked ?
            'You are in ONLINE mode'
            :
            "You are in OFFLINE mode");
        statusText.textContent = toggleSwitch.checked ? "ONLINE" : "OFFLINE";
        statusText.textContent = toggleSwitch.checked ? "ONLINE" : "OFFLINE";
        document.body.style.color = toggleSwitch.checked
            ? "#20C20E"
            : "var(--cr-color-forground)";
        statusText.style.color = toggleSwitch.checked
            ? "red"
            : "var(--cr-color-forground)";
        alertBox.style.display = toggleSwitch.checked ? "unset" : "none";
        preElement.classList = toggleSwitch.checked ? "glitch" : " "
    });

    rangeInput.addEventListener("input", () => {
        rangeLabel.textContent = `Number of SMS P/service (Attempts: ${rangeInput.value})`;
    });

    function toggleLogs(isOpen) {
        logsContainer.classList.remove("opened", "closed");
        logsContainer.classList.add(isOpen ? "opened" : "closed");
    }
    closeButton.addEventListener("click", () => toggleLogs(false));
    openButton.addEventListener("click", (event) => {
        event.stopPropagation();
        toggleLogs(true);
    });
    function isOpen() {
        return logsContainer.classList.contains("opened");
    }
    function handleOutsideClick(event) {
        if (isOpen() && !logsContainer.contains(event.target)) {
            toggleLogs(false);
        }
    }
    document.addEventListener("click", handleOutsideClick);

    function checkAndAddPlaceholder() {
        if (!loggingDiv.innerHTML.trim()) {
            loggingDiv.innerHTML = `<div class="emp-log">
            𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃
            <p>No logs available</p>
            </div>`;
        }
    }
    checkAndAddPlaceholder();

    msgAlert("Welcome to Emilios hacking tool!");
    infoButton.addEventListener("click", () => msgAlert(
        toggleSwitch.checked ?
            `
        </br>
        ───────────────▄▄───▐█<br/>
        ───▄▄▄───▄██▄──█▀───█─▄<br/>
        ─▄██▀█▌─██▄▄──▐█▀▄─▐█▀<br/>
        ▐█▀▀▌───▄▀▌─▌─█─▌──▌─▌<br/>
        ▌▀▄─▐──▀▄─▐▄─▐▄▐▄─▐▄─▐▄<br/>
        <br/>
        I'm nobody!!!
        <br/>
        <br/>
        `
            :
            `
        </br>
        ──▄──▄────▄▀<br/>
        ───▀▄─█─▄▀▄▄▄<br/>
        ▄██▄████▄██▄▀█▄<br/>
        ─▀▀─█▀█▀▄▀███▀<br/>
        ──▄▄▀─█──▀▄▄<br/>
        <br/>
        [!] Soheil Fouladvandi<br/>
        [!] @gafelson<br/>
        <br/>
        This is made with ❤️ for Emi 🧑🏼‍🎨
        <br/>
        <br/>
        `
    )
    );

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        loggingDiv.innerHTML = "";
        const formData = {
            phone_number: phoneInput.value,
            attempts: parseInt(rangeInput.value),
            offline: !toggleSwitch.checked,
        };

        try {
            msgAlert("Starting SMS Against...!");
            const response = await fetch("/send-sms", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(formData),
            });

            const result = await response.json();
            console.log(result);
            msgAlert("Mission passed!");
            console.log("Mission passed!");
            toggleLogs(true);

            if (result.success) {
                // Log details
                result.details.forEach((detail) => {
                    const detailLog = document.createElement("p");
                    detailLog.textContent = `[*] ${detail.url}:${detail.status}`;
                    detailLog.classList.add("detail-log");
                    loggingDiv.appendChild(detailLog);

                    // Log success
                    const successLog = document.createElement("p");
                    successLog.classList.add("success-log");
                    successLog.textContent = `[+] Success: ${result.message}`;
                    loggingDiv.appendChild(successLog);
                });


            } else {
                // Log error
                const errorLog = document.createElement("p");
                errorLog.classList.add("error-log");
                errorLog.textContent = `[!] Error: ${result.message}`;
                loggingDiv.appendChild(errorLog);
            }

            loggingDiv.style.display = "block";
        } catch (error) {
            // Log network error
            const networkErrorLog = document.createElement("p");
            networkErrorLog.classList.add("error-log");
            networkErrorLog.textContent = `[!] Network Error: ${error.message}`;
            loggingDiv.appendChild(networkErrorLog);
            loggingDiv.style.display = "block";
        }
    });
});
