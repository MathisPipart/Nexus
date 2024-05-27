window.onload = function() {
    if (activeDirectId !== null) {
        const messageContent = document.querySelector('.message-content-part');
        messageContent.scrollTop = messageContent.scrollHeight;

        function refreshMessages() {
            console.log('Refreshing messages...');
            fetch("/inbox/directs/" + activeDirectId)
                .then(response => response.text())
                .then(html => {
                    // const parser = new DOMParser();
                    // const doc = parser.parseFromString(html, 'text/html');
                    // const newMessages = doc.querySelector('.message-content-part').innerHTML;
                    // document.querySelector('.message-content-part').innerHTML = newMessages;
                    // messageContent.scrollTop = messageContent.scrollHeight;
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(html, 'text/html');
                    const newMessages = doc.querySelector('.message-content-part').innerHTML;
                    const previousScrollHeight = messageContent.scrollHeight;
                    document.querySelector('.message-content-part').innerHTML = newMessages;

                    // Vérifier si l'utilisateur est proche du bas de la conversation
                    const isNearBottom = messageContent.scrollTop + messageContent.clientHeight + 50 >= previousScrollHeight;

                    if (isNearBottom) {
                        messageContent.scrollTop = messageContent.scrollHeight;
                    }
                })
                .catch(error => console.error('Error refreshing messages:', error));
        }

        setInterval(refreshMessages, 1000);
    }
}