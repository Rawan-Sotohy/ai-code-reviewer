# Smart Code Review — System Architecture

## 1. Overview

Smart Code Review is a web-based code assessment platform that connects Students, Mentors, and Organizations.

The system follows a service-oriented architecture in which the **Backend API acts as the central orchestrator** between the Frontend, Database, Executor, and AI Engine.

```text
                         ┌─────────────────────────┐
                         │        Frontend         │
                         │   React + TypeScript    │
                         │                         │
                         │ Student │ Mentor │ Org  │
                         └────────────┬────────────┘
                                      │
                              HTTP / REST API
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │       Backend API       │
                         │    ASP.NET Core / C#    │
                         │                         │
                         │ Authentication          │
                         │ Authorization           │
                         │ Business Logic          │
                         │ Task Management         │
                         │ Submission Management   │
                         │ Appeals & Questions     │
                         │ Orchestration            │
                         └──────┬──────────┬───────┘
                                │          │
                       ┌────────┘          └──────────┐
                       ▼                              ▼
          ┌─────────────────────┐          ┌─────────────────────┐
          │      Database       │          │      Executor       │
          │      SQL Server     │          │       Docker        │
          │                     │          │                     │
          │ Users               │          │ Code Execution      │
          │ Organizations       │          │ Test Execution      │
          │ Groups              │          │ Resource Limits     │
          │ Tasks               │          │ Network Isolation   │
          │ Rubrics             │          │ Filesystem Isolation│
          │ Submissions         │          └──────────┬──────────┘
          │ Evaluations         │                     │
          │ Reviews             │               Test Results
          │ Questions           │                     │
          └─────────────────────┘                     ▼
                                           ┌─────────────────────┐
                                           │      AI Engine      │
                                           │       Python        │
                                           │       FastAPI       │
                                           │                     │
                                           │ Code Analysis       │
                                           │ AST Analysis        │
                                           │ Static Analysis     │
                                           │ Requirements        │
                                           │ Rubric Evaluation   │
                                           │ LLM Evaluation      │
                                           │ Feedback Generation │
                                           │ Output Validation   │
                                           └─────────────────────┘
```

## 2. Core Evaluation Flow

```text
Student
   │
   ▼
Frontend
   │
   ▼
Backend API
   │
   ├──────────────► Database
   │
   ├──────────────► Executor
   │                     │
   │                     ▼
   │                Test Results
   │                     │
   │                     ▼
   └──────────────► AI Engine
                         │
                         ▼
                   AI Evaluation
                         │
                         ▼
                    Backend API
                         │
                         ▼
                     Database
                         │
                         ▼
                     Frontend
                         │
                         ▼
                  Student Result
```

## 3. User Roles

### Organization

- Manage Groups
- Manage Mentors
- Manage Students
- View high-level statistics

### Mentor

- Create and manage Tasks
- Define Requirements
- Define Rubrics
- Set Hints and Deadlines
- Monitor Submissions
- Review Appeals
- Provide Final Scores
- Answer Student Questions

### Student

- Join Groups
- View Tasks
- Solve and submit Tasks
- Run and test code
- View personal submission history
- View AI Evaluation
- Submit Appeals
- Ask Questions
- View other students' Solutions after the deadline

Students cannot see other students' scores, submission times, or rankings.

## 4. Architectural Rules

### Backend as the Central Orchestrator

```text
Frontend
    │
    ▼
Backend API
    │
    ├──► Database
    ├──► Executor
    └──► AI Engine
```

The Frontend must not communicate directly with the Database, Executor, or AI Engine.

### Isolated Code Execution

Student code is untrusted and must never be executed inside the main Backend process.

The Executor runs submissions inside isolated Docker environments with:

- Execution time limits
- CPU and memory limits
- Network restrictions
- Filesystem restrictions

### AI Evaluation

The AI score is not the final authoritative score.

```text
AI Evaluation
      │
      ▼
AI Score + Feedback
      │
      ▼
Student Appeal
      │
      ▼
Mentor Review
      │
      ▼
Final Score
```

The Mentor's final decision is authoritative.

## 5. Main Components

### Frontend

**Technology:** React, TypeScript, Vite, Tailwind CSS, React Router, Axios, Monaco Editor

Responsible for:

- User interfaces
- Dashboards
- Task management
- Code Editor
- Submission interfaces
- Results and feedback
- Questions and Appeals

### Backend API

**Technology:** C#, ASP.NET Core Web API

Responsible for:

- Authentication and Authorization
- Role and permission management
- Business logic
- Task management
- Submission management
- Appeals and Questions
- Database access
- Internal service communication
- System orchestration

### Database

**Technology:** SQL Server

Stores:

- Users
- Organizations
- Groups
- Tasks
- Requirements
- Rubrics
- Submissions
- Executions
- Test Results
- AI Evaluations
- Mentor Reviews
- Appeals
- Questions

### Executor

**Technology:** Docker-based isolated execution environments

Responsible for:

- Running student code
- Running tests
- Enforcing resource limits
- Isolating untrusted code
- Returning Test Results

### AI Engine

**Technology:** Python, FastAPI

Responsible for:

- Code Analysis
- AST Analysis
- Static Analysis
- Requirements Evaluation
- Rubric Evaluation
- LLM-based Evaluation
- Feedback Generation
- Output Validation

## 6. Repository Architecture

```text
ai-code-reviewer/
│
├── apps/
│   ├── web/                 # Frontend
│   └── api/                 # Backend API
│
├── services/
│   ├── ai-engine/           # AI Evaluation Service
│   └── executor/            # Secure Code Execution Service
│
├── packages/
│   └── contracts/           # Shared JSON Schemas
│
├── deploy/                  # Deployment Configuration
│
├── assets/
├── .github/
│   └── workflows/
│
├── .env.example
├── .gitignore
├── README.md
└── LICENSE
```