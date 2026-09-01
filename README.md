# AniBot - AI Anime Assistant | آني بوت 🤖✨
[العربية](#-اللغة-العربية) | [English](#-english-version)

---

## 🇪🇬 اللغة العربية

### نظرة عامة
آني بوت (AniBot) هو مساعد ذكي متطور مدعوم بالذكاء الاصطناعي، تم تصميمه خصيصاً ليكون المرجع الأول لعشاق الأنمي والمانجا. بفضل اعتماده على نموذج Gemini، يقدم البوت تجربة تفاعلية غنية تجمع بين دقة المعلومات وشخصية الخبير المتعمق في الثقافة اليابانية.

### المميزات الرئيسية
*   **دعم اللغات الذكي:** التعرف التلقائي على اللغة والاستجابة بالعربية أو الإنجليزية بطلاقة.
*   **خبير الأنمي والمانجا:** تقديم ملخصات دقيقة، حقائق مثيرة، وتحليلات عميقة للأعمال.
*   **نظام توصيات مخصص:** يقترح عليك أعمالاً فنية بناءً على ذوقك الشخصي وتفضيلاتك.
*   **قاموس المصطلحات:** شرح مفصل للمصطلحات الخاصة بالأنمي (مثل: Shonen, Seinen, Isekai).
*   **تتبع الجلسة:** ميزة فريدة تتيح لك معرفة عدد الأسئلة التي طرحتها في الجلسة الحالية.

### التقنيات المستخدمة
*   **الخلفية (Backend):** Python, Flask.
*   **محرك الذكاء الاصطناعي:** Google Gemini 2.5 Flash API.
*   **الواجهة (Frontend):** HTML5, CSS3, JavaScript.

### آلية العمل
يعتمد النظام على منطق برمجى يدمج بين إطار عمل Flask وسجل المحادثة المستمر `chat.history`. يتم توجيه النموذج عبر تعليمات نظام (System Instructions) صارمة لضمان تقمص شخصية "خبير الأنمي" طوال الوقت، مع معالجة خاصة للطلبات الإحصائية داخل الجلسة.

### التعليمات
1.  **تثبيت المكتبات:** `pip install flask google-generativeai`
2.  **إعداد المفتاح:** ضع مفتاح الـ API الخاص بك من Google AI Studio في ملف `app.py`.
3.  **تشغيل المشروع:** `python app.py`
4.  **افتح الرابط:** [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🇺🇸 English Version

### Overview
AniBot is a sophisticated AI-powered companion tailored for anime and manga enthusiasts. Leveraging Google's Gemini engine, it serves as a digital sensei capable of providing deep insights and personalized interactions within the realm of Japanese pop culture.

### Key Features
*   **Language Fluidity:** Seamlessly detects and responds in the user's preferred language.
*   **Anime Encyclopedia:** Delivers detailed summaries, trivia, and cultural context for thousands of titles.
*   **Smart Recommendations:** Analyzes user preferences to suggest tailored anime and manga picks.
*   **Terminology Guide:** Simplifies complex anime tropes and genres (e.g., Tsundere, Slice of Life).
*   **Contextual Memory:** Maintains a continuous conversation flow and tracks user interaction stats.

### Tech Stack
*   **Backend:** Python, Flask.
*   **AI Engine:** Google Generative AI (Gemini 2.5 Flash).
*   **Frontend:** HTML5, CSS3, JavaScript.

### How It Works
The application utilizes Flask to bridge the gap between the user and the Gemini API.
*   **Persona Prompting:** Uses specialized system instructions to maintain the "AniBot" character.
*   **Session Management:** Implements `chat.history` for multi-turn dialogue.
*   **Logic Interception:** Custom Python logic calculates the question count manually from the session stream.

### Quick Start
1.  **Install dependencies:** `pip install flask google-generativeai`
2.  **API Config:** Insert your API key from Google AI Studio into `app.py`.
3.  **Run the app:** `python app.py`
4.  **Access:** [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

**Developed by: Osama Al-ghory (اسامة الجهوري)**
