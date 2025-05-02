---
title: Exa Research Agent
emoji: 🔍
colorFrom: blue
colorTo: purple
sdk: gradio
app_file: app.py
pinned: false
license: mit
sdk_version: 5.29.0
---
# 🔎 Exa Research Agent

A lightweight, real-time research assistant powered by [Exa.ai](https://exa.ai) and built using [Phidata](https://github.com/agno-agi/phidata).  
It lets you search for the **latest academic papers, research articles, and PDFs** without using OpenAI or any LLM backend.

> 📚 Ideal for students, researchers, and curious minds looking for cutting-edge science — instantly.

---

## ⚙️ How It Works

1. Type your research query in the input box (natural language or keyword-style).
2. The agent sends it to Exa.ai — a search engine built for research.
3. You get back up to 5 research-oriented results with titles, links, and short previews (if available).

---

## ✍️ Example Queries to Try

🔬 **AI & Science**
- `graph neural networks applications in chemistry`
- `neural-symbolic reasoning 2024 site:arxiv.org`

🌍 **Climate & Environment**
- `climate change models site:nature.com`

🧬 **Biotech**
- `CRISPR gene editing filetype:pdf`

💡 You can use modifiers like:
- `filetype:pdf` — for PDF papers only  
- `site:arxiv.org` — for arXiv-specific results  
- `2024` — to bias toward recent results  

---

## 🧠 Tech Stack

- **Exa.ai** — for real-time research search  
- **Phidata** — agentic framework (without LLMs)  
- **Gradio** — fast and beautiful web UI  
- **Python** — the glue that brings it all together

---

## 🔐 No OpenAI Required

This app does not use OpenAI or any LLM — just a powerful tool agent that queries Exa.ai and formats results.

---

## 🧪 Development & Deployment

You can run it locally with:

```bash
pip install -r requirements.txt
python app.py
```

## 📬 Contact

Built with ❤️ by [Rahul Thakur](https://huggingface.co/Raahulthakur)