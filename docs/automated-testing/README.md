# Testing

## Why Testing

- Tests allow us to find flaws in our software
- Good tests document the code by describing the intent
- Automated tests save time compared to manual tests
- Automated tests allow us to safely change and refactor our code without introducing regressions

## The Fundamentals

- We consider code to be incomplete if it is not accompanied by tests
- We write unit tests (tests without external dependencies) that can run before every PR merge
- We write integration tests / E2E tests that test the whole system end to end, and run them regularly
- We write our tests early and block any further code merging if tests fail
- We run load tests / performance tests where appropriate

---

## Test Planning

Be intentional when thinking about how to test applications. Build test plans for various scenarios and work out test cases at the design stage of each user story.

### Building Test Cases for a User Story

1. **Understand the Acceptance Criteria** — Thoroughly read and understand the acceptance criteria; clarify ambiguities with the product owner
2. **Identify Test Scenarios** — Consider both positive and negative scenarios (happy paths and error cases)
3. **Define Test Cases** — For each scenario, document:
    - **Title:** What is being tested
    - **Preconditions:** Any setup or test data required
    - **Test Steps:** Step-by-step instructions
    - **Expected Result:** The expected outcome

    Use the Given-When-Then format: **Given** the initial context, **When** the action, **Then** the precise outcome

4. **Automate where Possible** — Focus on automating hot paths and critical areas
5. **Review and Refine** — Review test cases with peers or stakeholders

### Common Test Plans

| Plan | Purpose |
|------|---------|
| Full Regression | Verify recent changes have not adversely affected existing functionality |
| Smoke | Quick check that the most critical functionalities are working |
| Functional | Verify each function conforms to specification |
| Integration | Verify different modules work together as expected |
| Load/Performance | Determine how the system performs under heavy load |
| Security | Identify and mitigate security vulnerabilities |
| UAT | Ensure the system meets business requirements and is ready for production |

---

## Unit Tests

Unit testing is a fundamental tool in every developer's toolbox. A unit test should be:

- **Provably reliable** — 100% reliable so failures indicate a bug in the code
- **Fast** — should run in milliseconds; a whole suite shouldn't take longer than a couple seconds
- **Isolated** — removing all external dependencies ensures reliability and speed

### Arrange / Act / Assert (AAA)

The standard pattern for organizing unit tests:

1. **Arrange** — Set up all variables, mocks, interfaces, and state needed
2. **Act** — Run the system under test
3. **Assert** — Check that the system acted appropriately

```csharp
[Fact]
public void TrySomething_NoElements_ReturnsFalse()
{
    // Arrange
    var elements = Array.Empty<string>();
    var myObject = new MyObject();

    // Act
    var myReturn = myObject.TrySomething(elements);

    // Assert
    Assert.False(myReturn);
}
```

### Best Practices

- Keep tests small and test only one thing
- Use a standard naming convention: `UnitName_StateUnderTest_ExpectedResult`
- Use Test-Driven Development (TDD) to guarantee a testable design from the start

### Things to Avoid

- **Sleeps** — A sleep is usually a sign of an untested dependency; it breaks the "fast" tenet
- **Reading from disk** — Creates a file system dependency; breaks isolation
- **Calling third-party APIs** — Wrap third-party calls in interfaces so they are not invoked in unit tests

### Key Tools

- [Visual Studio Live Unit Testing](https://learn.microsoft.com/en-us/visualstudio/test/live-unit-testing-intro?view=vs-2019)
- [Wallaby.js](https://wallabyjs.com/)
- [Infinitest](http://infinitest.github.io/) (Java)
- [PyCrunch](https://plugins.jetbrains.com/plugin/13264-pycrunch--live-testing) (Python)

---

## Integration Tests

Integration testing determines how well individually developed components communicate with each other. It ensures higher test coverage and serves as an important feedback loop throughout development.

> Integration testing confirms components work together as intended from a **technical** perspective; acceptance testing confirms they work together from a **business** perspective.

### Techniques

**Big Bang** — All components tested as a single unit. Best for small systems; requires all components to be complete before testing begins.

**Incremental** — Two or more logically related components tested together, with additional components added iteratively:

- *Top Down* — Test higher-level components first; use stubs to emulate lower-level modules not yet complete
- *Bottom Up* — Test lower-level modules first; use drivers to emulate higher-level modules

### Things to Avoid

- Avoid testing business logic in integration tests; keep test suites separate
- Avoid writing tests in a production environment; use a scaled-down copy
- Too much mocking will slow down the test suite; consider other test types if mocking becomes excessive
- Clean up any resources created for a given test

### Key Tools

- [JUnit](https://junit.org/junit5/), [moq](https://github.com/moq/moq4), [Cucumber](https://cucumber.io/), [Selenium](https://www.selenium.dev/), [Behave (Python)](https://behave.readthedocs.io/), [Robot Framework](https://robotframework.org/)

---

## E2E Tests

End-to-end (E2E) testing verifies a functional and data application flow consisting of several sub-systems working together from start to finish.

### E2E Testing Design Blocks

**User Functions** — List user-initiated functions and their interconnected sub-systems; track actions, inputs, and outputs.

**Conditions** — For each user function, prepare a set of conditions (timing, data conditions, and other factors).

**Test Cases** — For every scenario, create one or more test cases to test each functionality. Automate through the CI/CD build pipeline where possible.

### E2E Testing Phases

1. **Planning** — Business/functional requirement analysis, test plan development, environment setup, test data setup
2. **Pre-requisite** — System testing complete for all participating systems; production-like test environment ready
3. **Test Execution** — Execute test cases, register results, report bugs, verify bug fixes
4. **Test Closure** — Test report preparation, evaluation of exit criteria

### Key Metrics

- Test case preparation status (ready vs. total)
- Defects status (open vs. closed, by severity)
- Test environment availability

### Key Tools

- [Gauge Framework](https://gauge.org/) — Markdown-based, modular architecture
- [Robot Framework](https://robotframework.org/) — Keyword-based, extensible with Python/Java
- [Playwright](https://playwright.dev/) — Modern web E2E testing
- [Selenium](https://www.selenium.dev/) — Browser automation standard

---

## Map of Outcomes to Testing Techniques

| When working on... | I want to... | Consider |
|---|---|---|
| Development | Prove backward compatibility | Shadow testing |
| Development | Ensure program logic is correct | Unit testing; Integration testing |
| Development | Prevent regressions | Unit testing; Integration testing; Rings |
| Development | Validate component interactions | Consumer-driven Contract Testing |
| Development | Validate multiple components across a call chain | Integration testing; E2E tests |
| Development | Find security vulnerabilities | Security scenario testing |
| Development; Staging | Prove provisioned capacity meets goals | Load testing; Performance testing |
| Development; Staging; Operation | Discover system melt points | Squeeze; Load testing (stress) |
| Staging; Operation | Measure behavior under rapid traffic changes | Spike |

---

## Build for Testing

- **Parameterize everything.** Make variables configurable with reasonable defaults, especially for performance testing.
- **Document at startup.** Log all parameters when the application starts.
- **Log to console and external systems.** Console logging is essential for local debugging; external systems (e.g., Azure Monitor) provide traceability across services.
- **Log all activity.** Log when activities start and complete to understand application behavior.
- **Correlate distributed activities.** Use a Correlation ID passed between systems to trace distributed flows.

## Resources

- [Unit Testing Best Practices](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-best-practices)
- [Integration testing approaches](https://www.softwaretestinghelp.com/what-is-integration-testing/)
- [The One Page Test Plan](https://www.ministryoftesting.com/articles/the-one-page-test-plan)
