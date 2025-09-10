# Rate-Limit Guard Chatbot

## Overview

A minimal CLI chatbot using LangChain and Google Gemini 2.0 Flash, enhanced with a token-bucket rate limiter. The chatbot remembers the last 4 user-assistant turns and enforces a strict limit of 10 requests per minute. If the limit is exceeded, a 429 error message is shown.

## Features
- **Conversational Memory:** Remembers the last 4 user-assistant turns.
- **Google Gemini 2.0 Flash:** Fast, modern LLM via LangChain.
- **Token-Bucket Rate Limiter:** Allows 10 requests per minute; returns 429 if exceeded.
- **Secure API Key Handling:** Uses a `.env` file for your API key.
- **Simple CLI Interface:** Chat in your terminal. Type `exit` to quit.

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/HarshRajj/06-rate-limiting-for-chatbot.git
    cd 06-rate-limiting-for-chatbot
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure your API key:**
    - Create a `.env` file in the project root:
      ```
      GOOGLE_API_KEY="YOUR_API_KEY_HERE"
      ```

4. **Run the chatbot:**
    ```bash
    python main.py
    ```

## Example Conversation
```
🤖 Chatbot is ready! Type 'exit' to end the conversation.
--------------------------------------------------
You: Hello!
AI: Hello! How can I assist you today?
...
429: Rate limit exceeded. Please wait.
```

## Demo

[**▶️ Run on Google Colab**](https://colab.research.google.com/drive/18okoV1fLmH5hFx4iDjG_1rmkWYLeFtaB?usp=sharing) 
