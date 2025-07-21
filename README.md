
# 📊 WhatsApp Chat Analyzer

A powerful web-based tool built using **Streamlit** and **Python** for analyzing WhatsApp chat data. Upload your exported `.txt` chat file and get deep insights into message trends, user activity, word usage, emojis, and more.

## 🔗 Live Demo

[Click here to view the live project](https://whatsapp-analyzer-7wso.onrender.com/)
> ⚠️ To use the app, please upload an exported **WhatsApp chat** file (.txt format).

## 🚀 Features

* 📈 **Top-Level Statistics**

  * Total messages, words, media shared, and links.

* 🗓️ **Timelines & Trends**

  * Monthly & daily messaging trends.

* 📅 **Activity Heatmap**

  * Analyze activity patterns across days and hours.

* 🧑‍🤝‍🧑 **User Statistics**

  * Most active users (group chats only), with detailed breakdowns.

* ☁️ **Word Cloud**

  * Visualize the most commonly used words.

* 📊 **Most Common Words**

  * Bar chart of top-used words (excluding stopwords).

* 😄 **Emoji Analysis**

  * Emoji frequency and distribution.

---

### Clone the repository

```bash
git clone https://github.com/your-username/whatsapp_analyzer.git
cd whatsapp_analyzer
```

### Install dependencies

```bash
pip install -r requirements.txt
```

Make sure you have the following in your environment:

* Python 3.7+
* Streamlit
* pandas
* matplotlib
* seaborn
* wordcloud
* emoji
* urlextract

You can manually install missing packages using:

```bash
pip install streamlit pandas matplotlib seaborn wordcloud emoji urlextract
```

---

## 📂 File Structure

```
.
├── app.py                 # Main Streamlit app
├── helper.py              # Helper functions for analysis
├── preprocessor.py        # Preprocessing logic for raw text
├── stop_words.txt         # Custom stop words list
├── main_code.ipynb        # (Optional) Notebook version for development
├── README.md              # This file
```

---

## ▶️ Usage

1. **Export WhatsApp chat** as `.txt` file from your phone (without media).
2. **Run the app**:

```bash
streamlit run app.py
```

3. **Upload your chat file** in the sidebar.
4. **Select a user** or "Overall" to analyze full chat.
5. Click **"Show Analysis"** and explore visual insights.

---

## 📝 Preprocessing Logic

The `preprocessor.py` file:

* Extracts date, time, and user info from messages.
* Structures the data into a clean DataFrame for analysis.
* Adds columns like `Year`, `Month`, `Day`, `Hour`, etc.

---

## 📌 Notes

* Currently supports **English chat exports** with timestamps in format:
  `DD/MM/YY, HH:MM AM/PM - User: Message`
* Stopwords are read from `stop_words.txt`. You can customize this list.
* Group notifications are excluded from most analyses.

---


## 👤 Author

**Khyati Singh**
[GitHub](https://github.com/Khyatiiiiiii) | [LinkedIn](https://www.linkedin.com/in/khyati-singh-a65aba269/)

