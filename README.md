# 📄 PDF Q&A Bot - Smart Document Chatbot

An interactive, web-based AI application that allows users to upload any PDF document and ask questions directly based on its content. Built using Python, Streamlit, `pypdf`, and powered by Groq Cloud's ultra-fast Llama 3.3 model.

## 🚀 Features

* **PDF Text Extraction:** Seamlessly reads and parses text from uploaded PDF files instantly using `pypdf`.
* **Context-Aware Responses:** System-prompted to stick strictly to the PDF content, ensuring accurate answers without hallucination.
* **Minimalist UI:** Clean and responsive chat interface built entirely with Streamlit.
* **High-Speed Processing:** Integrated with Groq Cloud's `llama-3.3-70b-versatile` for blazing-fast inference.

## 🛠️ Tech Stack & Prerequisites

* **Frontend & UI:** Streamlit
* **LLM Provider:** Groq Cloud API (Llama 3.3)
* **PDF Parser:** `pypdf`
* **Language:** Python 3.x
* **Libraries:** `streamlit`, `groq`, `pypdf`, `python-dotenv`

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/shayankhan3/pdf_chat_bot_groq.git](https://github.com/shayankhan3/pdf_chat_bot_groq.git)
   cd pdf_chat_bot_groq
