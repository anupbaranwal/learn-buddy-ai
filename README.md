📘Learn-Buddy-AI

A Multi-Agent Personalized Study Assistant for Students

Learn-Buddy-AI is a multi-agent generative AI system that helps students learn school topics through automatically generated summaries, flashcards, and quizzes.
The project is built as part of the Kaggle Agents Intensive Capstone Project.

The idea is simple:

👉 The student chooses a subject.

👉 The system fetches information for a topic in that subject.

👉 Multiple AI agents work in parallel to generate learning materials.

👉 Results are aggregated and presented as a learning package.

This project is designed especially to support underprivileged students who may not have access to structured tutoring or personalized learning.

🚀 Features (Current Status)

✔️ Implemented
- Multi-agent architecture
- Subject input from user
- Search agent to fetch topic information
- Summary generation agent
- Flashcard generation agent
- Quiz generation agent
- Aggregator agent to combine outputs
- Parallel execution of agents
- Modular structure for easy extension

❌ Not Yet Implemented
(Important for reviewers)
- No persistent user progress storage
- No personalized topic recommendations based on past weaknesses
- No database or session memory
- No adaptive learning path yet
These can be added in future versions.

🧠 System Overview

Learn-Buddy-AI uses a modular multi-agent design, where each agent specializes in one part of the learning workflow.
**Current Workflow:**
```
User → Choose Subject
          ↓
      Search Agent
          ↓
   ┌────────── parallel ───────────┐
   ↓               ↓             ↓        ↓
Summary Agent   Flashcard     Quiz     Weakness
                   Agent      Agent     Agent
   └─────────────── aggregate ───────────────→ Final Study Pack
```
Study Pack Includes:
- A simple student-friendly topic summary
- Flashcards for memorization
- A short quiz to test understanding

🎯 Goals

The primary goal of Learn-Buddy-AI is to provide:
- Simple and understandable learning content
- Auto-generated study material for any topic
- Parallel AI workflows for faster generation
- A foundation for future personalization
A future version will track user progress and recommend next topics based on weaknesses.

🏗️ Project Structure

```
learn-buddy-ai/
├── .gitignore
├── README.md
├── requirements.txt
│
└── src/
    ├── __init__.py
    └── capstone/
        ├── __init__.py
        ├── config/
        │   └── config.py
        └── agents/
            ├── aggregator_agent.py
            ├── chat_buddy_agent.py
            ├── controller_agent.py
            ├── flash_card_agent.py
            ├── parallel_agent.py
            ├── quiz_agent.py
            ├── root_agent.py
            └── summary_agent.py

```
⚙️ How It Works

1. User selects a topic (e.g., "Photosynthesis")
2. The system fetches the study material from internet
3. Run agents in sequence and parallel
   - Controller Agent
   - Summary Agent
   - Flashcard Agent
   - Quiz Agent

4. Combine results
AggregatorAgent merges outputs into a final structured response.

5. Display results to user
(terminal output for now)

🛠️ Running the Project

  1. Clone the repository
   `
   git clone https://github.com/anupbaranwal/learn-buddy-ai
   cd learn-buddy-ai`
  2. Install dependencies
  3. Set your API keys
   `Configure your key for the model you’re using (Gemini / OpenAI / etc.)`
  4. Run the app
   `python src/capstone/__init__.py`

❤️ Purpose

This project was built with a focus on helping underserved students who lack access to quality tutoring.
The long-term vision is to provide:
- Free personalized study material
- Adaptive learning paths
- Multi-language support
- Low-bandwidth / offline mode

🙌 Acknowledgements

Built as part of the **Kaggle Agents Intensive Course (2025).**
Inspired by the mission to make learning accessible for every student.
   
