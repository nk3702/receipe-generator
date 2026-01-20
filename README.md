# Recipe Generator – Generative AI Agent Application

A full-stack web application that lets users input available ingredients and generates a personalized, healthy recipe using a Generative AI agent.  
Built for the **Haveloc selection process** assignment using **Pydantic AI** for reliable agent orchestration and structured outputs.

## Features
- User-friendly interface to enter comma-separated ingredients
- AI-powered recipe generation (title, step-by-step instructions, tips)
- Real-time loading states and error handling
- Responsive, modern UI with Tailwind CSS
- Robust backend with input validation, logging, and CORS support
- Live deployed on Vercel

## Tech Stack
- **Frontend**: React + Vite + Tailwind CSS + Axios
- **Backend**: Python + FastAPI + Pydantic AI
- **AI Model**: OpenRouter (free tier, e.g., meta-llama/llama-3.1-8b-instruct:free)
- **Deployment**: Vercel (full-stack)
- **Environment Management**: python-dotenv

## Project Structure
```
my-ai-agent-app/
├── agent.py               # Pydantic AI agent definition and logic
├── main.py                # FastAPI backend application
├── .env                   # API keys (not committed!)
├── frontend/              # React + Vite frontend
│   ├── src/
│   │   └── App.jsx        # Main frontend component
│   ├── package.json
│   └── vite.config.js
├── README.md
└── requirements.txt       # Python dependencies (optional)
```

## Setup & Run Locally

### Prerequisites
- Python 3.10+
- Node.js 18+
- Git
- OpenRouter account (free API key)

### Backend Setup
1. Create & activate virtual environment:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install fastapi uvicorn pydantic-ai python-dotenv
   ```

3. Create `.env` file in root with your key:
   ```
   OPENROUTER_API_KEY=sk-or-v1-your-key-here
   ```

4. Run the backend:
   ```bash
   uvicorn main:app --reload --port 8000
   ```
   → Test at: http://127.0.0.1:8000/docs

### Frontend Setup
1. Go to frontend folder:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the frontend:
   ```bash
   npm run dev
   ```
   → Open: http://localhost:5173

### Full Flow
1. Start backend in one terminal
2. Start frontend in another terminal
3. Visit http://localhost:5173 → enter ingredients → generate recipe

## Deployment (Vercel)
1. Push code to a **public GitHub repository** (do **not** commit `.env`)
2. Go to https://vercel.com → New Project → Import GitHub repo
3. Configure:
   - Root directory: `/` (or `/frontend` if separate)
   - Environment Variables: Add `OPENROUTER_API_KEY` with your value
4. Deploy → Get live URL (e.g., https://recipe-generator.vercel.app)

## How Pydantic AI is Used
- Structured input/output with Pydantic models (`Input`, `Output`)
- Type-safe agent orchestration
- Automatic validation & error handling
- Reliable calls to OpenRouter free models
```

