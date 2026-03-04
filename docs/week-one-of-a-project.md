# Week One of a Project

The purpose of this document is to:

- Organize content in the playbook for quick reference and discoverability
- Provide content in a logical structure which reflects the engineering process
- Extensible hierarchy to allow teams to share deep subject-matter expertise


## Before Starting the Project

- [ ] Discuss and start writing the Team Agreements. Update these documents with any process decisions made throughout the project
  - [Working Agreement](agile-development/team-agreements/working-agreement.md)
  - [Estimation](agile-development/ceremonies.md#estimation)
- [ ] [Set up the repository/repositories](source-control/README.md#creating-a-new-repository)
  - Decide on repository structure/s
  - Add README.md, LICENSE, .gitignore, etc
- [ ] Build a Product Backlog — see [Agile & Ceremonies](agile-development/ceremonies.md#backlog-management)
  - Set up a project in your chosen project management tool (ex. Azure DevOps)
  - INVEST in good User Stories and Acceptance Criteria
  - [Non-Functional Requirements Guidance](design/design-patterns/non-functional-requirements-capture-guide.md)

## Day 1

- [ ] [Plan the first sprint](agile-development/ceremonies.md#sprint-planning)
  - Agree on a sprint goal, and how to measure the sprint progress
  - Determine team capacity
  - Assign user stories to the sprint and split user stories into tasks
  - Set up Work in Progress (WIP) limits
- [ ] [Decide on test frameworks and discuss test strategies](automated-testing/README.md)
  - Discuss the purpose and goals of tests and how to measure test coverage
  - Agree on how to separate unit tests from integration, load and smoke tests
  - Design the first test cases
- [ ] Decide on branch naming — see [Source Control](source-control/README.md#branch-naming)
- [ ] [Discuss security needs and verify that secrets are kept out of source control](./CI-CD/dev-sec-ops/secrets-management/README.md)

## Day 2

- [ ] [Set up Source Control](source-control/README.md)
  - Agree on [best practices for commits](source-control/README.md#commit-best-practices)
  - [ ] [Set up basic Continuous Integration with linters and automated tests](./CI-CD/continuous-integration.md)
  - [ ] [Set up meetings for Daily Stand-ups and decide on a Scrum Master](agile-development/ceremonies.md#stand-up)
  - Discuss purpose, goals, participants and facilitation guidance
  - Discuss timing, and how to run an efficient stand-up

## Day 3

- [ ] [Agree on code style and on how to assign Pull Requests](code-reviews/pull-requests.md)
- [ ] [Set up Build Validation for Pull Requests (2 reviewers, linters, automated tests)](code-reviews/pull-requests.md)
- [ ] Agree on logging and observability frameworks and strategies — see [Observability](observability/best-practices.md)

## Day 4

- [ ] [Set up Continuous Delivery](./CI-CD/continuous-integration.md#continuous-delivery)
  - Determine what environments are appropriate for this solution
  - For each environment discuss purpose, when deployment should trigger, pre-deployment approvers, sign-off for promotion.
- [ ] Agree on how to Design a feature and conduct a Design Review — see [Design & NFRs](design/design-patterns/non-functional-requirements-capture-guide.md#design-reviews--trade-studies)

## Day 5

- [ ] Conduct a [Sprint Demo](agile-development/ceremonies.md#sprint-demo)
- [ ] Conduct a [Retrospective](agile-development/ceremonies.md#retrospectives)
  - Determine required participants, how to capture input (tools) and outcome
  - Set a timeline, and discuss facilitation, meeting structure etc.
- [ ] Refine the Backlog — see [Backlog Management](agile-development/ceremonies.md#backlog-management)
  - Determine required participants
  - Update estimates, and the [Estimation](agile-development/ceremonies.md#estimation) process
- [ ] Conduct a team retrospective and capture lessons learned
