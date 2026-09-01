document.addEventListener('DOMContentLoaded', () => {
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    const chatWindow = document.getElementById('chat-window');
    const historyList = document.getElementById('history-list');

    // Function to detect Arabic characters
    function isArabic(text) {
        const arabicRegex = /[\u0600-\u06FF]/;
        return arabicRegex.test(text);
    }

    // Function to add a message to the chat window with a streaming effect for the bot
    function addMessage(message, sender) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', `${sender}-message`);

        // Set language attribute for directionality
        if (isArabic(message)) {
            messageElement.lang = 'ar';
        } else {
            messageElement.lang = 'en';
        }

        chatWindow.appendChild(messageElement);

        if (sender === 'bot') {
            messageElement.textContent = ''; // Start with an empty message
            const words = message.split(' ');
            let i = 0;
            const streamingInterval = setInterval(() => {
                if (i < words.length) {
                    messageElement.textContent += words[i] + ' ';
                    i++;
                    chatWindow.scrollTop = chatWindow.scrollHeight; // Keep scrolling
                } else {
                    clearInterval(streamingInterval);
                }
            }, 100); // Adjust streaming speed here (in milliseconds)
        } else {
            messageElement.textContent = message;
        }
        
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    // Function to add a question to the history sidebar
    function addToHistory(question) {
        const historyItem = document.createElement('li');
        historyItem.textContent = question;
        historyList.appendChild(historyItem);
    }

    // Function to handle sending a message
    async function sendMessage() {
        const message = userInput.value.trim();
        if (message === '') return;

        addMessage(message, 'user');
        addToHistory(message);
        userInput.value = '';

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            addMessage(data.response, 'bot');

        } catch (error) {
            console.error('Error sending message:', error);
            addMessage('Sorry, something went wrong. Please try again.', 'bot');
        }
    }

    // Event Listeners
    sendButton.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Add a welcome message from the bot
    addMessage("Hello! I'm AniBot, your expert guide to the world of anime. What's on your mind today?", 'bot');
});
