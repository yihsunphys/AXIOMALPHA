# ![Python](https://img.shields.io/badge/python-3.10+-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green) ![Streamlit](https://img.shields.io/badge/Streamlit-1.20-orange) AARN — Approximation Algorithm Research Navigator

A research assistant tool for **searching, analyzing, and verifying approximation algorithm papers**. Combines a **FastAPI backend**, **SQLite database**, and **Streamlit admin UI**.

---

## ⚡ Quick Start

### 1️⃣ Backend

Go to the backend folder:  
cd backend

Create a virtual environment and install dependencies:  
python -m venv .venv  
.venv\Scripts\activate # Windows

# source .venv/bin/activate # Mac/Linux

pip install -r requirements.txt

Set environment variables (`.env`) if needed:  
DATABASE_URL=sqlite:///./app.db  
S2_API_KEY=your_semantic_scholar_api_key  
OPENAI_API_KEY=your_openai_api_key  
OPENAI_MODEL=gpt-3.5-turbo

Run the backend:  
uvicorn app.main:app --reload --port 8000

Backend API will be available at: http://localhost:8000

---

### 2️⃣ Streamlit Admin UI

Go to admin UI folder:  
cd ../admin-ui

Install dependencies:  
python -m venv .venv  
.venv\Scripts\activate # Windows  
pip install -r requirements.txt

Run the Streamlit app:  
streamlit run streamlit_app.py

Open in browser: http://localhost:8501

**Pages / Features**:

- Search: query papers via backend
- Paper Detail: view abstract, algorithm, ratio, summary
- Admin Queue: review suggestions and verify papers

---

### Frontend (Next.js + TailwindCSS)

The frontend is built with:

- **Next.js 14**
- **React**
- **TailwindCSS**
- **Axios** (for calling backend API)

### Install & Run

```bash
cd frontend
npm install
npm run dev
Open the app at:
http://localhost:3000
```

Folder Structure
```
src/
 ├── app/
 │    ├── page.tsx            # Home
 │    ├── search/page.tsx     # Search UI
 │    └── paper/[id]/page.tsx # Paper detail
 ├── lib/api.ts               # Axios API client
 ├── components/              # UI components
 └── types/                   # TypeScript types
```

---


### 🔹 Notes

- Make sure the **backend is running** before using the Streamlit UI.
- `.gitignore` excludes `.env`, `.db`, `.venv`, and other sensitive files.
- Optional: deploy backend to **Railway** and admin UI to **Streamlit Cloud** or **Vercel**.

---

### 📌 Deployment Tips

Backend:

- Use Railway for quick deployment
- Set environment variables in Railway dashboard
- Procfile is ready for deployment if needed

Admin UI:

- Deploy on Streamlit Cloud for a quick demo
- Ensure `BACKEND_BASE` points to your deployed backend

---

### 📌 Git Workflow

Initialize repo:  
git init  
git add .  
git commit -m "Initial commit"

Add remote and push:  
git remote add origin https://github.com/yourusername/aarn.git  
git branch -M main  
git push -u origin main

---

### 📌 License

MIT License (or your preferred license)


### setup aPI key(powershell)

setx S2_API_KEY "your key"

or 
$env:S2_API_KEY="your key"

than echo $env:S2_API_KEY

to see if set properly
