# AI Code Assessment Platform

An AI-powered code assessment and review platform designed to help mentors, educators, academies, universities, and learning platforms evaluate programming submissions automatically and consistently.

The platform combines **automated code execution, objective test results, static/code analysis, customizable rubrics, and AI-powered evaluation** to provide meaningful scores and actionable feedback.

---

## 🎯 Vision

Build a standalone **Code Assessment as a Service** platform that can be used directly by educators and students, while providing APIs and integration capabilities for educational platforms in the future.

The long-term goal is to enable learning platforms, universities, academies, and coding programs to integrate automated code assessment and AI code review directly into their existing systems.

---

## ✨ Core Features

### For Mentors

- Create and manage programming tasks
- Define task requirements
- Create customizable evaluation rubrics
- Assign tasks to students
- Review student submissions
- Review and override AI-generated evaluations
- Monitor student performance

### For Students

- View assigned programming tasks
- Read requirements and evaluation criteria
- Write and submit code
- Run code against test cases
- Receive automated evaluation
- View score and detailed AI feedback
- Resubmit improved solutions
- Track previous submissions

### AI-Powered Evaluation

The AI evaluation engine analyzes submissions using multiple signals:

- Automated test results
- Task requirements
- Evaluation rubric
- Code structure
- Code quality
- Potential issues
- Maintainability
- Overall implementation quality

The AI is **not used as the sole source of truth**. Objective execution and testing are combined with AI-based qualitative evaluation.

---

## 🏗️ Architecture

The project follows a modular monorepo architecture:

```text
ai-code-reviewer/
│
├── apps/
│   ├── web/                  # Web application
│   └── api/                  # Main backend API
│
├── services/
│   ├── ai-engine/            # AI evaluation service
│   └── executor/             # Isolated code execution service
│
├── packages/
│   └── contracts/            # Shared data contracts
│
├── deploy/                   # Docker & deployment configuration
│
├── assets/                   # Project assets
│
├── .github/
│   └── workflows/            # CI/CD workflows
│
├── .env.example
├── .gitignore
├── README.md
└── LICENSE
```



### System Flow

```text
                        Web Application
                              │
                   ┌──────────┴──────────┐
                   ▼                     ▼
                Mentor                Student
                   │                     │
            Create Task &             View Task
             Set Rubric             Submit Code
                   │                     │
                   └──────────┬──────────┘
                              ▼
                         Backend API
                              │
                     ┌────────┴────────┐
                     ▼                 ▼
                  Executor         AI Engine
                     │                 │
                     ▼                 ▼
                Test Results     Score + Feedback
                     │                 │
                     └────────┬────────┘
                              ▼
                         Evaluation
                              │
                   ┌──────────┴──────────┐
                   ▼                     ▼
                Student               Mentor
              View Result          Review / Override
                   │
                   ▼
              Resubmit Code
```

The backend acts as the main orchestrator between the web application, code executor, AI engine, and database.

---

## 🧩 Project Components

### Web Application

The frontend application provides the user-facing experience for mentors and students.

**Planned stack:**

- React
- TypeScript
- Vite
- Tailwind CSS
- React Router
- Axios
- Monaco Editor

---

### Backend API

The main application backend responsible for:

- Authentication and authorization
- Users and roles
- Tasks
- Rubrics
- Submissions
- Evaluations
- Mentor reviews
- Database operations
- Service orchestration
- External integrations

**Planned stack:**

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- JWT

---

### AI Engine

An independent internal service responsible for AI-powered code evaluation.

Responsibilities include:

- Prompt management
- LLM communication
- Requirement evaluation
- Rubric-based scoring
- Code analysis
- AST analysis
- Static analysis
- Feedback generation
- AI output validation

The AI Engine does not communicate directly with the frontend or database.

---

## 🔐 Security Principles

Because the platform executes untrusted user code, security is a core architectural requirement.

Submitted code must **never be executed directly by the main API process**.

The execution layer is isolated from the main application and should enforce:

- Process isolation
- Resource limits
- Execution timeouts
- Memory limits
- Restricted filesystem access
- Restricted network access
- Controlled dependencies

Additional security controls will be added as the platform evolves.

---

## 🔌 Future Integrations

The platform is designed to operate independently while remaining integration-ready.

Future educational-platform integrations may include:

- REST API
- API Keys
- OAuth / SSO
- Webhooks
- JavaScript SDK
- Embeddable assessment components

This will allow external learning platforms, universities, academies, and training programs to use the assessment engine without rebuilding it themselves.

---

## 👥 Team

The project is developed by a three-person team:

- **Frontend Developer** : [**Doha Emad**](https://github.com/) 

  Web application and user experience

- **Backend Developer** : 
[**Alaa Mohamed**](https://github.com/) 

  API, database, execution, and infrastructure

- **AI Developer** :  [**Rawan Sotohy**](https://github.com/Rawan-Sotohy)

  AI evaluation engine, code analysis, scoring, and feedback


---

## 📄 License

This project and its source code are proprietary.
All rights reserved.