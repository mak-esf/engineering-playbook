# CI/CD

## CI/CD Overview

**Continuous Integration (CI)** is the engineering practice of frequently committing code in a shared repository (ideally several times a day) and running an automated build on each commit. This enables early detection of integration issues between multiple developers.

**Continuous Delivery (CD)** extends CI by also testing deployments of the integrated code base on a replica of the production environment. This surfaces operational issues early and validates that the main branch is always shippable.

**Why CI/CD:**

- Automated build and deployment of software
- Automated configuration of all components
- Quick re-build of the environment from scratch in case of disaster
- Latest version of the code always deployed to dev/test environments
- Reliable release strategy, well understood by all

**The Fundamentals:**

- Run a quality pipeline (linting, unit tests, etc.) on each PR and update to the main branch
- All cloud resources (including secrets and permissions) are provisioned through infrastructure as code (e.g., Terraform, Bicep, Pulumi)
- All release candidates are deployed to a non-production environment through an automated process
- Releases are deployed to production through an automated process
- Release rollbacks are carried out through a repeatable process
- Automated tests validate all release candidate artifacts end-to-end against a non-production environment

### AI-Assisted CI/CD Authoring

AI tools can accelerate writing CI/CD pipeline YAML and scripts, but use explicit guardrails:

- Use AI to draft pipeline templates as a starting point; validate in a safe non-production sandbox before merging
- Require human review of generated steps for correctness, idempotence, and security (especially around secrets and permissions)
- Annotate AI-generated content in the PR description so reviewers apply extra scrutiny

**Pre-merge checklist for AI-generated pipeline changes:**

- [ ] Human review completed and documented in PR
- [ ] No secrets or credentials are hard-coded
- [ ] Required linting and syntax checks pass
- [ ] Security and license scans run with no critical issues
- [ ] Pipeline steps are idempotent with clear rollback strategies

---

# Continuous Integration

![CI Pipeline](https://user-images.githubusercontent.com/7635865/76624154-c2c12800-6502-11ea-912d-a260c821ac41.png)

We encourage teams to establish an automated and repeatable CI pipeline before any service code is written (usually in Sprint 0). Each integration should be verified by an automated build that runs a suite of validation tests.

## Goals

A robust build automation pipeline will:

- Accelerate team velocity
- Prevent integration problems
- Avoid last minute chaos during release dates
- Provide a quick feedback cycle for system-wide impact of local changes
- Separate build and deployment stages
- Measure and report metrics around build failures/successes
- Reduce human errors

## Build Automation

An automated build should encompass:

### Build Task

A single step within your build pipeline that compiles your code project into a single build artifact.

### Unit Testing

Your build definition includes validation steps to execute a suite of automated unit tests.

### Code Style Checks

- Code across an engineering team must be formatted to agreed coding standards.
- Code and documentation should avoid non-inclusive language where possible.
- We recommend incorporating security analysis tools within the build stage: code credential scanner, static analysis, etc.
- Code standards are maintained within a single configuration file with a step in the build pipeline asserting conformance.

### Build Script Target

A single command should have the capability of building the system — both on a CI server and on a developer's local machine.

### DevOps Security Checks

Introduce security to your project at early stages. See [Secrets Management](./dev-sec-ops/secrets-management/README.md) for secrets handling guidance as part of CI.

## Build Environment Dependencies

- Maintain a central automated manifest/process that streamlines the installation and setup of any software dependencies.
- All developers should be able to emulate the build environment from their local desktop regardless of OS.
- For projects using VS Code, consider leveraging Dev Containers to standardize the local developer experience.

## Infrastructure as Code

Manage as much of the following as code:

- Configuration files
- Configuration management (environment variable automation)
- Secret management
- Cloud resource provisioning
- Role assignments
- Load test scenarios
- Alerting/monitoring rules

## Integration Validation

- Include tests in your pipeline to validate the build candidate conforms to automated business functionality assertions.
- Keep the build fast. Slow builds become a bottleneck — consider max timeout limits.
- All mocked datasets used for tests should be checked into the mainline repository.
- Integrate code coverage tools; fail builds when coverage falls below a minimum threshold (commonly 80%).

## Git Driven Workflow

- Every commit should trigger the CI pipeline to create a new build candidate.
- Protected branch policies should block PRs until CI stages pass.
- Broken builds should block pull request reviews and be treated as the highest priority issue.
- Avoid commenting out failing tests in the mainline branch.

## Deliver Quickly and Daily

Commit code on a daily cadence. End-of-day checked-in code should contain unit tests at minimum. Isolate work into small chunks which tie directly to business value.

---

# Continuous Delivery

A continuous delivery pipeline is an automated manifestation of your process to consistently and repeatably provision environments, install application versions, and configure applications.

## Define a Release Strategy

Establish a common understanding between the tech lead and stakeholders around the release strategy during the planning phase:

- Who is in charge of deployments to each environment and of the release
- An asset and configuration management strategy
- The environments available for acceptance, capacity, integration, and UAT testing, and how builds move through them
- Deployment to testing and production environments (change requests, approvals)
- Application configuration management across environments (use a secrets vault like Key Vault or KMS; never expose secrets in the runtime environment)
- A disaster recovery plan for restoring the application's state

## Application Release and Environment Promotion

Your release process should deploy the build artifact created from CI across all cloud environments, starting with the test environment. The test environment acts as a gate to validate your test suite before promoting to production.

The first deployment of any application should be showcased in a production-like environment (UAT) to solicit early customer feedback.

## Rolling Back Releases

Your release strategy must account for rollback scenarios. If there are no data changes to back out, simply trigger a new release candidate for the last known production version. For rollbacks involving data changes, ensure all data is backed up prior to each release.

Consider [deployment rings](https://learn.microsoft.com/en-us/azure/devops/migrate/phase-rollout-with-rings?view=azure-devops) to limit the impact of releases by gradually deploying to production.

## Zero Downtime & Blue-Green Deployments

**Blue-Green** runs two identical production environments. Only one accepts live traffic at a time. During a release, deploy the new version to the inactive environment, test it, then switch the router. Rollback is simply switching back.

**Canary releasing** rolls out new versions to a subset of production nodes first, collecting early insights before routing users to the new version.

## Resources

- [Martin Fowler's Continuous Integration Best Practices](https://martinfowler.com/articles/continuousIntegration.html)
- [Continuous Delivery](https://www.continuousdelivery.com/) by Jez Humble, David Farley
- [Azure DevOps multi stage pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/multi-stage-pipelines-experience?view=azure-devops)
