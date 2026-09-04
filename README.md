# AI Code Assessment Platform

An AI-powered code assessment and review platform designed to help mentors, educators, academies, universities, and learning platforms evaluate programming submissions automatically and consistently.

The platform combines **automated code execution, objective test results, static/code analysis, customizable rubrics, and AI-powered evaluation** to provide meaningful scores and actionable feedback.

---

## 🎯 Vision

Build a standalone **Code Assessment as a Service** platform that can be used directly by educators and students, while remaining integration-ready for educational platforms in the future.

The long-term goal is to enable learning platforms, universities, academies, and coding programs to integrate automated code assessment and AI code review directly into their existing systems.

---

## ✨ Core Features

### Organization

- Organization Dashboard
- Create and manage groups
- Manage mentors
- Manage students
- Monitor overall activity

### Groups

- Group Dashboard
- Group Members
- Group Feed / Announcements
- Group Tasks

### For Mentors

- Create and manage programming tasks
- Define task requirements
- Create customizable evaluation rubrics
- Add optional hints
- Set deadlines and submission types
- View student submissions
- Review AI-generated evaluations
- Review and handle appeals
- Override AI evaluations when necessary
- Issue final scores
- Answer student questions
- Monitor student performance

### For Students

- View assigned programming tasks
- Read requirements and evaluation criteria
- View hints
- Write and submit code
- Run code against test cases
- Receive automated evaluation
- View AI score and detailed feedback
- Resubmit improved solutions
- Track submission history
- Submit appeals
- Ask questions
- View other students' solutions after the task deadline

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

The AI is **not used as the sole source of truth**. Objective execution and testing are combined with AI-based qualitative evaluation, while mentors can review and override AI-generated evaluations.

### Learning & Collaboration

- Student questions
- Task-aware AI assistance
- Mentor intervention when required
- Solutions unlocked after the deadline
- No student leaderboard or ranking

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
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
        Organization         Mentor           Student
              │                │                │
        Manage Groups     Create Tasks      View Tasks
        Manage Users      Requirements      Submit Code
                          Rubric / Hint
                          Deadline
                               │
                               ▼
                         Backend API
                               │
                 ┌─────────────┼─────────────┐
                 ▼             ▼             ▼
             Database       Executor      AI Engine
                               │             │
                               ▼             ▼
                          Test Results   AI Evaluation
                                         Score + Feedback
                               │             │
                               └──────┬──────┘
                                      ▼
                                 Evaluation
                                      │
                           ┌──────────┴──────────┐
                           ▼                     ▼
                        Student               Mentor
                     View Results        Review / Appeal
                     Resubmit Code        Final Score
                           │
                           ▼
                    Submission History
                           │
                           ▼
                    Deadline Reached
                           │
                           ▼
                    Solutions Unlocked
                    (Learning, No Ranking)
```

The Backend API acts as the main orchestrator between the Web Application, Database, Code Executor, and AI Engine.

---

## 🧩 Project Components

### Web Application

The frontend application provides the user-facing experience for organizations, mentors, and students.

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
- Users, Roles, Organizations & Groups
- Tasks, Requirements, Rubrics & Hints
- Submissions & Submission History
- AI Evaluation Management
- Mentor Reviews & Appeals
- Final Score Management
- Student Questions & Mentor Answers
- Notifications
- GitHub Integration
- Database Management
- Business Logic & Service Orchestration
- Communication with the AI Engine and Code Executor

**Planned stack:**

- C# / ASP.NET Core Web API
- Entity Framework Core
- SQL Server
- JWT Authentication
- Roles, Claims & Policies
- ILogger

---

### AI Engine

An independent internal service responsible for AI-powered code evaluation.

Responsibilities include:

- Prompt management
- LLM communication
- Code analysis
- AST analysis
- Static analysis
- Requirement evaluation
- Rubric-based evaluation
- Test result analysis
- AI scoring
- Feedback generation
- AI output validation

The AI Engine does not communicate directly with the frontend or database.

**Planned stack:**

- Python
- FastAPI
- LLM
- AST Parsing Tools
- Static Analysis Tools

---

### Code Executor

An isolated internal service responsible for safely executing untrusted student code and running automated tests.

Responsibilities include:

- Code execution
- Test execution
- Test result generation
- Execution timeouts
- CPU and memory limits
- Restricted filesystem access
- Restricted network access
- Controlled execution environments

The Executor does not communicate directly with the frontend. All execution requests are handled through the Backend API.

**Planned stack:**

- Docker
- Isolated execution environments
- Language-specific runtimes

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

- **Frontend Developer:** [**Doha Emad**](https://github.com/Doha-2004)  
  Web application and user experience

- **Backend Developer:** [**Alaa Mohamed**](https://github.com/Alaa304)  
  API, database, execution, and infrastructure

- **AI Developer:** [**Rawan Sotohy**](https://github.com/Rawan-Sotohy)  
  AI evaluation engine, code analysis, scoring, and feedback

---

## 📄 License

This project and its source code are proprietary.

All rights reserved.
