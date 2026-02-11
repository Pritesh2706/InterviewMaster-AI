##📘 InterviewMaster AI

AI-Powered Mock Interview Simulator with Evaluation, Score, and Reports

InterviewMaster AI is an intelligent interview preparation agent that simulates real interviews, evaluates responses, scores user performance, and tracks improvement over time.

It acts as your personal AI interview coach.


🚀 Features

✔ Mock Interview Simulation

Simulates HR + technical interviews using AI.

✔ Resume-Based Question Generation

Automatically generates questions from candidate resume.

✔ Answer Evaluation

Analyzes user's response using NLP and LLM.

✔ **Scoring System**

Provides score out of 100 with breakdown:

Communication

Technical relevance

Confidence

Clarity

Depth of knowledge


✔ Progress Tracker

Tracks performance across multiple interviews.

✔ Exportable Interview Report

Creates PDF/Markdown report of:

Questions asked

Answers given

AI feedback

Scorecard


✔ Multi-Agent Architecture

Uses planner agent, evaluator agent, and scoring agent.


🏗 System Architecture

User → Resume Parser → Question Generator → Interview Agent → Evaluation Engine → Scoring System → Report Generator → Output


🛠 Tech Stack

Python

FastAPI / Flask

Natural Language Processing

LLM (OpenAI/ChatGPT Local Interface)

MongoDB / JSON Storage

HTML/CSS for basic UI


📦 Installation

git clone https://github.com/<your-username>/interviewmaster-ai
cd interviewmaster-ai
pip install -r requirements.txt


▶ Run the App

python app/main.py


📊 API Endpoints

POST /start-interview

Starts mock interview.

POST /evaluate

Evaluates user’s answer.

POST /score

Generates score.

GET /report/{user_id}

Returns final interview report.


📄 License

MIT License.
