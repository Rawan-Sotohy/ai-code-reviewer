# Smart Code Review — Data Model

## 1. Overview

The data model represents the relationships between Users, Organizations, Groups, Tasks, Submissions, Executions, Evaluations, Appeals, Reviews, and Questions.

## 2. Entities

### User

```text
User
- id
- username
- email
- password_hash
- role
- created_at
```

Roles:

```text
STUDENT
MENTOR
ORGANIZATION
```

### Organization

```text
Organization
- id
- name
- description
- owner_user_id
- created_at
```

### Group

```text
Group
- id
- organization_id
- name
- description
- start_at
- end_at
- created_at
```

### Group Membership

```text
GroupMembership
- id
- group_id
- user_id
- role
- joined_at
```

Membership roles:

```text
MENTOR
STUDENT
```

### Task

```text
Task
- id
- group_id
- mentor_id
- title
- description
- hint
- rubric_id
- start_at
- deadline
- submission_type
- status
- created_at
- updated_at
```

Submission types:

```text
EDITOR
GITHUB
BOTH
```

Task statuses:

```text
DRAFT
PUBLISHED
CLOSED
```

### Requirement

```text
Requirement
- id
- task_id
- description
- order
```

### Rubric

```text
Rubric
- id
- task_id
- name
- description
```

### Rubric Criterion

```text
RubricCriterion
- id
- rubric_id
- name
- description
- weight
- order
```

The total weight of all criteria must equal 100.

### Submission

Represents a final submission attempt.

```text
Submission
- id
- task_id
- student_id
- attempt_number
- source_type
- code
- github_repository
- github_branch
- submitted_at
- status
```

Submission statuses:

```text
PENDING
EVALUATING
EVALUATED
FAILED
```

### Execution

Represents every code execution, including executions performed before final submission.

```text
Execution
- id
- task_id
- student_id
- submission_id
- source_type
- code
- created_at
- status
```

`submission_id` may be null for executions performed before Final Submit.

### Test Result

```text
TestResult
- id
- execution_id
- total_tests
- passed_tests
- failed_tests
- execution_time
- status
```

### Test Case Result

```text
TestCaseResult
- id
- test_result_id
- name
- passed
- expected
- actual
- error
```

### AI Evaluation

```text
AIEvaluation
- id
- submission_id
- ai_score
- feedback
- strengths
- weaknesses
- created_at
```

### Requirement Result

```text
RequirementResult
- id
- ai_evaluation_id
- requirement_id
- passed
- feedback
```

### Rubric Result

```text
RubricResult
- id
- ai_evaluation_id
- criterion_id
- score
- feedback
```

### Appeal

```text
Appeal
- id
- submission_id
- student_id
- reason
- status
- created_at
```

Appeal statuses:

```text
PENDING
ACCEPTED
REJECTED
```

### Mentor Review

```text
MentorReview
- id
- submission_id
- mentor_id
- appeal_id
- decision
- mentor_score
- final_score
- comment
- reviewed_at
```

The `final_score` is the authoritative score.

### Question

```text
Question
- id
- task_id
- student_id
- content
- status
- created_at
```

Question statuses:

```text
OPEN
AI_ANSWERED
ESCALATED
ANSWERED
```

### Question Answer

```text
QuestionAnswer
- id
- question_id
- responder_type
- responder_id
- content
- created_at
```

Responder types:

```text
AI
MENTOR
```

## 3. Relationships

```text
Organization
    │
    └──< Group
            │
            ├──< GroupMembership >── User
            │
            └──< Task
                    │
                    ├──< Requirement
                    │
                    ├──1 Rubric
                    │      └──< RubricCriterion
                    │
                    ├──< Submission
                    │      ├──< Execution
                    │      │      └──< TestResult
                    │      │             └──< TestCaseResult
                    │      │
                    │      ├──< AIEvaluation
                    │      │      ├──< RequirementResult
                    │      │      └──< RubricResult
                    │      │
                    │      ├──< Appeal
                    │      │      └── MentorReview
                    │      │
                    │      └──< MentorReview
                    │
                    └──< Question
                           └──< QuestionAnswer
```

## 4. Business Rules

- A Student can belong to multiple Groups.
- A Task belongs to one Group.
- A Task is created by a Mentor assigned to that Group.
- A Student can make multiple Submission attempts for a Task.
- A Student can perform multiple Executions before submitting.
- Every Final Submission is evaluated through the Executor and AI Engine.
- AI Score is not the final authoritative score.
- A Mentor Review can produce the Final Score.
- Students can only view their own submission history and scores before the deadline.
- Mentors can view submissions, scores, and submission times for their Groups.
- Solutions are represented by student Submissions.
- Student Submissions become viewable to Group members after the Task deadline.
- Students cannot see peer scores or rankings.
- No leaderboard or ranking entity is required.
- No new submissions are accepted after the Task deadline.