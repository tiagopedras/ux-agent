# Linear: delegating issues to agents

Source: <https://linear.app/docs/assigning-issues> and <https://linear.app/developers/aig>. Pulled 21 Sep 2026. No date shown on either page.

How Linear, a Jira-style issue tracker, lets people hand an issue to an AI agent without
splitting it or moving it to a separate board.

## Delegation

- "Delegate an issue to an agent while keeping a human teammate as the assignee. The assignee
  remains responsible for the work, while the agent contributes on their behalf."
- "Assigned issues, even those delegated to an agent, appear in your My Issues default view,
  where you can review all issues you're responsible for across your workspace."
- "The assignment and delegation history is tracked in its Activity feed, which shows changes
  over time and who made them."
- Views and Inbox can be filtered by assignee or by agent.

## Agent Interaction Guidelines

| # | Guideline | Linear's wording |
| --- | --- | --- |
| 1 | An agent should always disclose that it's an agent | "When humans and agents work side by side, humans need instant certainty about who they are interacting with. The agent must signal its identity clearly so that it can never be mistaken for a person." |
| 2 | An agent should inhabit the platform natively | "By default, agents should be able to work through existing UI patterns and standard actions of the platform they operate in." |
| 3 | An agent should provide instant feedback | "Silence leads to uncertainty. When invoked, an agent should provide immediate, but unobtrusive, feedback to reassure the user it has received a request." |
| 4 | An agent should be clear and transparent about its internal state | "Agents should clearly indicate whether they're thinking, waiting for input, executing, or finished working. Humans should be able to understand what's happening at a glance and, when needed, inspect the underlying reasoning, tool calls, prompts, and decision logic." |
| 5 | An agent should respect requests to disengage | "When asked to disengage, an agent should step back, immediately – and only re-engage once it's received a clear signal to do so." |
| 6 | An agent cannot be held accountable | "There should be a clear delegation model between humans and agents. An agent can carry out tasks, but the final responsibility should always remain with a human." |
