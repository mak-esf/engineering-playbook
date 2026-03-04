# How We Work

In this documentation we refer to the cross-functional delivery team as a **"Crew"** (i.e., the team responsible for delivery on a project). This includes the dev team, tech lead, product manager (PM), data scientists, etc.

**The Fundamentals:**

- We keep a shared backlog of work that everyone on the team can access (e.g., Jira, Github, or Azure DevOps)
- We plan our work in iterations with clear goals (e.g., sprints)
- We have a clear idea of when work items are ready to implement (definition of ready)
- We have a clear idea of when work items are completed (definition of done)
- We communicate the progress in one place that everyone can access, and keep the progress up to date (e.g., sprint board and daily standups)
- We reflect on our work regularly to make improvements (e.g., retrospectives)
- The team has a clear idea of the roles and responsibilities in the project (e.g., tech lead, TPM, Scrum Master)
- We value and respect the opinions and work of all team members

**AI tooling note:** Teams are increasingly adapting traditional Scrum practices to take advantage of AI tools. Favor frequent, lightweight planning and validation over rigid cadences when it accelerates feedback loops. Use AI-assisted tooling (e.g., GitHub Copilot) to accelerate planning and generate drafts — while maintaining human oversight and review.

---

# Agile Ceremonies

## Sprint Planning

**Goals**

- The planning supports Diversity and Inclusion principles and provides equal opportunities.
- The Planning defines how the work is going to be completed in the sprint.
- Stories fit in a sprint and are designed and ready before the planning.

> **Note:** Self assignment by team members can give a feeling of fairness in how work is split in the team. Sometimes, this ends up not being the case as it can give an advantage to the loudest or more experienced voices in the team. Individuals also tend to stay in their comfort zone, which might not be the right approach for their own growth.

> Working with AI tools note: Some teams adapt sprint planning cadence to support the faster patterns which AI tools bring — favoring short, lightweight planning events or a continuous planning cadence when this enables faster feedback and delivery. Use AI-assisted planning tools (e.g., Copilot or planning assistants) to draft plans or acceptance criteria, but always validate and adapt output collaboratively with the team.

### Sprint Goal

Consider defining a sprint goal, or list of goals for each sprint. Effective sprint goals are a concise bullet point list of items. A Sprint goal can be created first and used as an input to choose the Stories for the sprint.

The sprint goal can be used:

- At the end of each stand up meeting, to remember the north star for the Sprint
- During the sprint review ("was the goal achieved?", "If not, why?")

### Stories

Example 1: Preparing in advance

- The tech lead and product owner plan time to prepare the sprint backlog ahead of sprint planning.
- The tech lead uses their experience and the estimation made for these stories to gauge how many should be in the sprint.
- The tech lead asks the entire team to look at the tentative sprint backlog in advance of the sprint planning.
- During the sprint planning meeting, the team reviews the sprint goal and the stories. Everyone confirms they understand the plan and feel it's reasonable.

Example 2: Building during the planning meeting

- The product owner ensures that the highest priority items of the product backlog is refined and estimated.
- During the Sprint planning meeting, the product owner describes each story, starting by highest priority.
- The team keeps considering more stories up to a point where they agree the sprint backlog is full.
- Stories are assigned during the planning meeting.

### Sprint Planning Resources

- [Planning](https://scrumguides.org/scrum-guide.html#sprint-planning 'Sprint Planning')
- [Refinement](https://learn.microsoft.com/devops/plan/what-is-agile-development#diligent-backlog-refinement 'Refinement')

## Estimation

**Goals**

- Estimation supports the predictability of the team work and delivery.
- The estimation process is improved over time and discussed on a regular basis.
- Estimation is inclusive of the different individuals in the team.

Common approaches: **T-shirt sizes** (S/M/L/XL), **planning poker** (story points), or a simple **"fits in a sprint?"** binary indicator. Avoid converting story points to days.

### Estimation Resources

- [The Most Important Thing You Are Missing about Estimation](https://www.scrum.org/resources/blog/most-important-thing-you-are-missing-about-estimation)

## Retrospectives

**Goals**

- Retrospectives lead to actionable items that help grow the team's engineering practices. These items are in the backlog, assigned, and prioritized.
- Retrospectives are used to ask the hard questions when necessary.

**Suggestions**

- Consider retro formats beyond Mad Sad Glad: Triple Nickels, Timeline, Team Radar, 5 Whys, Fishbone.
- Schedule enough time to get to the correct plan and action.
- Bring in a neutral facilitator for project retros or retros after a difficult period.

### Retrospective Resources

- [Agile Retrospective: Making Good Teams Great](https://www.goodreads.com/book/show/721338.Agile_Retrospectives)
- [Retrospective](https://scrumguides.org/scrum-guide.html#sprint-retrospective 'Retrospective')

## Sprint Demo

**Goals**

- Each sprint ends with demos that illustrate the sprint goal and how it fits in the engagement goal.

**Suggestions**

- Consider not pre-recording sprint demos in advance. You can record the demo meeting and archive them.
- A demo does not have to be about running code. It can be showing documentation that was written.

### Sprint Demo Resources

- [Sprint Review/Demo](https://scrumguides.org/scrum-guide.html#sprint-review 'Sprint Review')

## Stand-Up

**Goals**

- The stand-up is run efficiently.
- The stand-up helps the team understand what was done, what will be done and what are the blockers.
- The stand-up helps the team understand if they will meet the sprint goal or not.

**Suggestions**

- Keep stand up short and efficient. Table longer conversations for a parking lot section.
- Run daily stand ups: 15 minutes of stand up and 15 minutes of parking lot.
- Stand ups should include everyone involved in the project, including the customer.

### Stand-Up Resources

- [Stand-Up/Daily Scrum](https://scrumguides.org/scrum-guide.html#daily-scrum 'Stand-up/Daily Scrum')

---

## Backlog Management

**Goals**

- User stories have a clear acceptance criteria and definition of done.
- Design activities are planned as part of the backlog (a design for a story that needs it should be done before it is added in a Sprint).

**Guidance**

- Consider backlog refinement as an ongoing activity, not just a scheduled meeting.
- The team should decide on and have a clear understanding of a definition of ready and a definition of done.
- The team should have a clear understanding of what constitutes good acceptance criteria for a story/task. A common format: **Given** the initial context, **When** the action occurs, **Then** the expected outcome.
- Technical debt is mostly due to shortcuts in implementation. Shortcuts should generally be avoided; when they do happen, prioritize improvement activities to reduce this debt.

### Backlog Resources

- [Product Backlog](https://scrumguides.org/scrum-guide.html#product-backlog)
- [Acceptance Criteria](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/best-practices-product-backlog?view=azure-devops#acceptance-criteria)
- [Definition of Done](https://scrumguides.org/scrum-guide.html#increment)
- [Definition of Ready](https://www.scrum.org/resources/blog/walking-through-definition-ready)
