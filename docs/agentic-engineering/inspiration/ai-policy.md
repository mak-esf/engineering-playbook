Engineering Policy Statement: AI-Assisted Code Integrity and Human Accountability

1. Purpose and Scope of Agentic Engineering

Effective immediately, the organization adopts a formal transition from manual implementation to "Agentic Engineering." We are ending the era of "vibe coding"—the reckless, autopilot practice of accepting AI outputs without deep architectural oversight. As we scale, we must mitigate the Lethal Trifecta of AI agents: extreme speed, non-determinism, and hidden costs. Our strategy shifts the human role from a "writer of lines" to an "Editor-in-Chief" and "Architect of Intent." In this model, AI handles the mechanical implementation, but the human remains the sole authority for correctness, maintainability, and security.

The following distinctions are now the standard for all engineering sessions:

Parameter	Vibe Coding (Prototyping)	Agentic Engineering (Production)
Review Rigor	Minimal; "trusting the vibe"	Exhaustive; line-by-line human audit
Accountability	Autopilot; "hoping" it works	Absolute; human ownership of every diff
Primary Use Case	Hackathons, MVPs, scripts	Critical systems, scalable architecture
Quality Focus	Speed and exploration	Security, maintainability, and logic
Tooling Interaction	One-shot/Chat interfaces	Multi-step/Autonomous agents with tools

The Human-in-the-Loop Mandate: Every commit is the sole responsibility of the human author. As an IBM training axiom once stated: "A computer can never be held accountable. That's your job." You must be able to explain every line of code as if you wrote it by hand. No PR shall be approved if the author cannot articulate the underlying logic and its long-term impact on the system.

Adherence to this policy requires rigorous technical standards to ensure our velocity does not outpace our ability to verify.

2. The Burden of Proof: Standards for Verification

We must solve the "70% Problem." AI models excel at solving "accidental complexity"—the boilerplate and repetitive patterns that make up 70% of a codebase. However, they frequently falter on the remaining 30% of "essential complexity": the intricate business logic, security boundaries, and edge cases. Because AI-generated code is often "more taxing" to review than human code, verification is now our primary engineering bottleneck.

To maintain integrity, "Proof over Vibes" is mandatory. All contributions must be accompanied by the following verification artifacts:

* Automated Backstops: Authors must maintain test suites with a non-negotiable target of >70% coverage. High coverage is the only effective safety net for AI speed.
* Empirical Evidence: Every PR must include objective proof of functionality. This includes logs, screenshots, and browser console traces. Engineers are encouraged to use tools like Chrome DevTools MCP to give agents "eyes" for real-time UI/UX verification.

We strictly mandate a Red/Green TDD (Test-Driven Development) workflow for all agentic sessions. Post-hoc test generation (writing tests after the code) is forbidden for logic; such tests merely confirm what the implementation happens to do, rather than what it should do.

1. Write Test (Red): Define requirements by writing tests that fail as expected.
2. Implementation (Green): Direct the AI to generate code until the tests pass.
3. Human Sign-off: The Editor-in-Chief reviews the output for architectural fit.

These verification requirements must be formalized within the mandatory PR Contract.

3. The Mandatory PR Contract and Specification Standards

To prevent the "house of cards" effect, we require a formal PR Contract for every change. This prevents the accumulation of fragile, unread code. We operate on a principle of Spec-Driven Development, treating the planning phase as a "Waterfall in 15 minutes"—a rapid but rigorous period of structured intent definition before a single line is generated.

The four pillars of the PR Contract are:

1. Intent (What/Why): Definition of the goal in 1–2 sentences.
2. Empirical Evidence: Specific tests passed, logs, and screenshots provided.
3. Risk & AI Taxonomy: Identification of the AI's role and the code's risk tier.
4. Human Review Focus: Targeted areas (architecture, security) requiring senior scrutiny.

Every repository must maintain a SPEC.md as the living source of truth for the project's goals and tech stack (e.g., "React 18 with TypeScript"), and an AGENTS.md to store durable rules for AI behavior. Within these documents, you must define Three-Tier Boundaries:

* ✅ Always Do: Actions the agent takes autonomously (e.g., "Run unit tests before every commit").
* ⚠ Ask First: High-impact changes requiring human sign-off (e.g., "Modifying database schemas" or "Adding new dependencies").
* 🚫 Never Do: Hard stops (e.g., "Never commit secrets," "Never edit vendor directories").

These boundaries ensure agents operate safely within high-stakes system components.

4. High-Stakes Protocols: Security and Accountability

AI exhibits predictable and dangerous weaknesses. Research shows 45% of AI-generated code contains security flaws. Logic errors appear at 1.75x the frequency of human-written code, and XSS vulnerabilities occur at a staggering 2.74x higher rate. AI must be treated as a "high-speed intern"—capable of high volume but prone to hallucinatory security patterns.

The following areas require a Non-Negotiable Human Sign-off gate in the CI/CD pipeline:

* [ ] Authentication and Authorization logic.
* [ ] Payment Processing and Financial calculations.
* [ ] Secrets Management and API Key Handling.
* [ ] Processing of Untrusted Input.

Any logic touching these areas mandates a Threat Model Review. AI-generated security code must undergo a second-pass audit using a specialized security model or static analysis tool before final human verification. By enforcing these gates, we ensure the "Lethal Trifecta" does not compromise our core infrastructure.

5. Operational Governance: Orchestration and Review Efficiency

We are transitioning to a "Factory Model" of software engineering. As the arc of abstraction rises from bits to instructions to orchestrated systems, the developer’s job is now building the system that builds the software. This requires "Mission Control" orchestration and strict operational efficiency.

Engineers must manage their "Token Budgets" by selecting the right model for the task:

* Local High-Touch Sessions: Use reasoning-heavy models (e.g., Claude 3.5 Sonnet or Gemini 1.5 Pro) for architecture and ambiguous logic.
* Cloud/Background Async Sessions: Use smaller, faster models for bounded tasks like documentation or routine refactors.

To manage parallel orchestration and avoid the bottleneck that saw OCaml maintainers reject a 13,000-line AI PR as "too taxing to review," we mandate:

* Small, Stackable PRs: Break work into digestible, incremental commits.
* WIP Limits: Cap the number of active agent streams per developer to prevent review fatigue.
* Isolated Contexts: Use Git worktrees and separate branches to prevent merge conflicts and context loss.
* LLM-as-a-Judge: Use a secondary agent to perform initial style and anti-pattern scans, acting as a "first-pass" reviewer to triage text noise.

While AI accelerates the mechanical work, the human remains the ultimate Architect and Editor-in-Chief. You are responsible for the long-term maintainability and institutional context of the system. We use AI to accelerate our process, never to abdicate our responsibility.
