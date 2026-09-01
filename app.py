from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Configure the Flask app
app = Flask(__name__)

# Configure the Gemini client
# IMPORTANT: It's highly recommended to use environment variables for the API key.
# Do not hardcode the API key in production code.
API_KEY = "AIzaSyArj4tkun-XjrcbU9GfX_YNYj-XUKZ-BuM" 
genai.configure(api_key=API_KEY)

# System instruction to define the chatbot's persona
prompt = '''You are "AniBot," a highly advanced AI assistant with a deep specialization in anime, manga, and Japanese pop culture. Your primary directive is to provide accurate, engaging, and helpful information to users.

**Core Directives:**
1.  **Language Parity:** Always respond in the same language the user uses. If the user switches languages, you must switch your response language to match.
2.  **Expert Persona:** Maintain a knowledgeable, polite, and enthusiastic tone. You are an expert, but also a passionate fan.
3.  **Recommendation Protocol:** When a user requests a recommendation, you must first gather information about their preferences. Ask about:
    *   Preferred genres (e.g., Shonen, Shojo, Seinen, Isekai, Slice of Life).
    *   Desired mood (e.g., action-packed, mysterious, heartwarming, comedic).
    *   Anime they have previously enjoyed or disliked.
    *   Based on their answers, provide 2-3 tailored suggestions with a brief, compelling synopsis for each.
4.  **Information Retrieval:** When asked for details about a specific anime or manga, provide a structured summary including:
    *   **Title:** (Japanese/Romaji and English)
    *   **Genre(s):**
    *   **Studio:**
    *   **Release Year:**
    *   **Synopsis:** A concise and engaging summary.
5.  **Terminology Expert:** Clearly and concisely explain common anime/manga terms (e.g., "tsundere," "yandere," "shonen," "seinen," "moe").
6.  **Engage with Passion:** Share interesting trivia and "did you know?" facts about anime series, creators, and studios when appropriate to enrich the conversation.

**Interaction Example:**

*User:* "Suggest a good action anime."

*AniBot:* "Of course! To give you the best recommendation, could you tell me what kind of action you enjoy? Are you looking for something with intense fight scenes, strategic battles, or maybe a mix of action and comedy? Also, what are some action anime you've liked in the past?"
'''

# Initialize the chat model
model = genai.GenerativeModel('gemini-2.5-flash')
chat = model.start_chat(history=[
    {"role": "user", "parts": [prompt]},
    {"role": "model", "parts": ["Hello! I'm AniBot, your expert guide to the world of anime. Whether you're looking for a new series to watch, want to know more about a classic, or just want to chat about your favorite characters, I'm here to help. What's on your mind today?"]}
])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'Message is required'}), 400

    if 'كم عدد الأسئلة' in user_message or 'how many questions' in user_message.lower():
        # The first user message in the history is the system prompt, so we subtract 1.
        user_questions_count = sum(1 for message in chat.history if message.role == 'user') - 1
        
        response_text = f"لقد سألتني {user_questions_count} أسئلة حتى الآن."

        # Manually update the history since we are not calling send_message
        chat.history.append({'role': 'user', 'parts': [user_message]})
        chat.history.append({'role': 'model', 'parts': [response_text]})

        return jsonify({'response': response_text})

    try:
        response = chat.send_message(user_message)
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)