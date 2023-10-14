//alert("Js is link !");  

function launchBatchFile() {
    console.log("launchBatchFile");
    // Use ActiveXObject for IE
    try {
        const objShell = new ActiveXObject("WScript.Shell");
        console.log("Launching batch file...");
        objShell.Run("start_server.bat", 1, false);
    } catch (e) {
        console.error("Error launching batch file:", e);
    }
}

function updateDateTime() {
    const currentDateElement = document.getElementById('current-date');
    const currentTimeElement = document.getElementById('current-time');

    const currentDate = new Date().toLocaleDateString('fr-FR', {
        day: 'numeric',
        month: 'long',
        year: 'numeric'
    });
    const currentTime = new Date().toLocaleTimeString('fr-FR', {
        hour: '2-digit',
        minute: '2-digit'
    });

    currentDateElement.innerText = currentDate;
    currentTimeElement.innerText = currentTime;
}

// Mettre à jour l'heure et la date initialement
updateDateTime();

// Mettre à jour l'heure et la date toutes les secondes
setInterval(updateDateTime, 1000);

launchBatchFile();