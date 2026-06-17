# AI Voice News Assistant

An AI-powered Voice News Assistant that fetches the latest news from the internet, generates concise summaries using Large Language Models, and allows users to interact with news articles through natural language conversations.

The system combines News Retrieval, Article Processing, Speech Recognition, Conversational AI, and Memory Management to create an intelligent news assistant capable of answering follow-up questions about current events.

---

## Project Demo

🎥 Demo Video


**Demo Link:** https://www.linkedin.com/posts/mehtab-ansari-ba4486266_artificialintelligence-generativeai-aiengineer-activity-7472985524690006016-5B8M



---

## Features

### Real-Time News Retrieval

* Fetches latest news headlines from BBC RSS feeds.
* Automatically retrieves current news whenever the system is refreshed.
* Processes multiple articles in real time.

### Article Extraction

* Extracts full article content from news URLs.
* Cleans and prepares article text for downstream AI processing.

### AI News Summarization

* Generates concise article summaries using Llama 3.2 via Ollama.
* Converts lengthy news articles into easy-to-read bullet-point summaries.

### Conversational News Question Answering

* Users can ask questions about current news.
* Supports contextual follow-up questions.
* Maintains conversation continuity across interactions.

### Voice Interaction

* Speech-to-Text powered by OpenAI Whisper.
* Enables voice-based news exploration and question answering.

### Article Memory

* Remembers the currently selected article.
* Supports commands such as:

  * "Tell me about article number 3"
  * "What happened next?"
  * "Why did that happen?"

### Conversation Memory

* Stores previous conversations.
* Uses historical interactions to provide context-aware responses.

### Local AI Deployment

* Runs entirely on local infrastructure using Ollama.
* No external LLM API required.

---

## System Architecture

User Voice/Text Input
↓
Whisper Speech Recognition
↓
Intent Detection
↓
Article Retrieval
↓
Llama 3.2 Processing
↓
Context & Memory Management
↓
AI Response Generation

---

## Project Structure

```text
voice_news_agent/
│
├── ai/
│   ├── briefing_selector.py
│   ├── intent_classifier.py
│   ├── news_briefing.py
│   ├── news_qa.py
│   └── retriever.py
│
├── config/
│   └── settings.py
│
├── memory/
│   ├── article_memory.py
│   ├── briefing_memory.py
│   ├── conversation_memory.py
│   └── database.py
│
├── models/
│   └── llm.py
│
├── news/
│   ├── fetch_news.py
│   ├── extract_article.py
│   ├── process_news.py
│   └── summarize_news.py
│
├── speech/
│   ├── audio_recorder.py
│   ├── speech_to_text.py
│   └── text_to_speech.py
│
├── voice/
│   └── voice_news_qa.py
│
├
├── voice_news_assistant.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

### Artificial Intelligence

* Llama 3.2
* Ollama
* OpenAI Whisper

### Backend

* Python
* SQLite

### Data Processing

* Feedparser
* Newspaper4k



### Speech Processing

* SoundDevice
* SoundFile
* Whisper

---

## Installation

### Clone Repository

```bash
git clone https://github.com/mehtab-ansari350/voice_news_agent.git

cd voice_news_agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download Ollama:

https://ollama.com

Pull Llama 3.2:

```bash
ollama pull llama3.2:3b
```

Verify Installation:

```bash
ollama list
```

---

## Run News Processing

Fetch and summarize latest news:

```bash
python -m news.process_news
```

---

## Run Voice Assistant

```bash
python voice_news_assistant.py
```

---


```

---

## Example Queries

* Give me today's news.
* Tell me about article number 2.
* What happened next?
* Why did that happen?
* Who was involved?
* Summarize article 4.
* What are the latest developments?

---

## Future Enhancements

* Multi-source news aggregation.
* RAG-based document retrieval.
* Vector database integration.
* Agentic AI workflows.
* Real-time speech conversation.
* Personalized news recommendations.
* Multi-language support.

---

## Skills Demonstrated

* Generative AI
* Large Language Models (LLMs)
* Prompt Engineering
* Retrieval-Augmented Generation Concepts
* Speech Recognition
* NLP
* Conversational AI
* Python Development
* Database Design
* AI Application Development

---

## Author

Mehtab Ansari

GitHub:
https://github.com/mehtab-ansari350

LinkedIn:
https://www.linkedin.com/in/mehtab-ansari-ba4486266/

Email:
mehtaban321@gmail.com

---

## License

This project is intended for educational, research, and portfolio purposes.
