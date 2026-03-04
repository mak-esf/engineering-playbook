# Security

Developers working on projects should adhere to industry-recommended standard practices for secure design and implementation of code. Our engineers should understand the [OWASP Top 10 Web Application Security Risks](https://owasp.org/www-project-top-ten/), as well as how to mitigate as many of them as possible.

**If you are looking for a fast way to get started** evaluating your application or design, check out the "Secure Coding Practices Quick Reference" document below, which contains an itemized checklist of high-level concepts you can validate are being done properly.

## Quick Resources

- [Secure Coding Practices Quick Reference](https://owasp.org/www-pdf-archive/OWASP_SCP_Quick_Reference_Guide_v2.pdf)
- [Web Application Security Quick Reference](https://owasp.org/www-pdf-archive//OWASP_Web_Application_Security_Quick_Reference_Guide_0.3.pdf)
- [Security Mindset/Creating a Security Program Quick Start](https://github.com/OWASP/Quick-Start-Guide/blob/master/OWASP%20Quick%20Start%20Guide.pdf?raw=true)
- Credential Scanning / Secret Detection — see [Secrets Management](../CI-CD/dev-sec-ops/secrets-management/README.md)

## DevSecOps

Introduce security to your project at early stages. Security practices, automation, tools, and frameworks should be integrated as part of the CI pipeline — see [Secrets Management](../CI-CD/dev-sec-ops/secrets-management/README.md) for one example.

## OWASP Cheat Sheets

> OWASP is considered to be the gold-standard in computer security information. To view all cheat sheets, check out their [Cheat Sheet Index](https://github.com/OWASP/CheatSheetSeries/blob/master/Index.md).

- [Attack Surface Analysis](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.md)
- [Authorization Basics](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Authorization_Cheat_Sheet.md)
- [Cross-Site Request Forgery (CSRF) Prevention](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.md)
- [Cross-Site Scripting (XSS) Prevention](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.md)
- [Input Validation](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Input_Validation_Cheat_Sheet.md)
- [SQL Injection Prevention](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.md)
- [Cryptographic Storage](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cryptographic_Storage_Cheat_Sheet.md)

## Recommended Tools

- **Vulnerability Scanning:** [SonarCloud](https://sonarcloud.io/), [Snyk](https://github.com/snyk/snyk), [Trivy](https://github.com/aquasecurity/trivy), [Anchore](https://github.com/anchore/anchore-engine)
- **Runtime Security:** [Falco](https://github.com/falcosecurity/falco), [Tracee](https://github.com/aquasecurity/tracee)
- **K8s Security:** [OPA/Gatekeeper](https://github.com/open-policy-agent/gatekeeper), [cert-manager](https://github.com/jetstack/cert-manager)

---

## Threat Modeling

Threat modeling is a systematic approach to identifying potential threats and recommendations to help reduce risk and meet security objectives earlier in the development lifecycle.

### STRIDE Framework

Use the **STRIDE** framework to identify threats:

| Threat | Description |
|--------|-------------|
| **S**poofing | Impersonating something or someone |
| **T**ampering | Modifying data or code |
| **R**epudiation | Claiming not to have performed an action |
| **I**nformation disclosure | Exposing information to unauthorized parties |
| **D**enial of service | Denying or degrading service |
| **E**levation of privilege | Gaining capabilities without proper authorization |

### Threat Modeling Phases

1. **Diagram** — Capture all requirements for your system and create a data-flow diagram
2. **Identify** — Apply the STRIDE framework to the data-flow diagram to find potential security issues
3. **Mitigate** — Decide how to approach each issue with the appropriate combination of security controls
4. **Validate** — Verify requirements are met, issues are found, and security controls are implemented

### Resources

- [Microsoft Threat Modeling Tool](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool)
- [STRIDE framework](https://learn.microsoft.com/en-us/training/modules/tm-use-a-framework-to-identify-threats-and-find-ways-to-reduce-or-eliminate-risk/1b-threat-modeling-framework)
- [Threat Modeling Security Fundamentals](https://learn.microsoft.com/en-us/training/paths/tm-threat-modeling-fundamentals/)

---

## Security Testing Rules of Engagement

When performing application security analysis or requesting a security review, follow these rules.

### For Those Requesting a Review

- Web Application Firewalls can be configured but do not enable automatic blocking — it will greatly slow down the tester
- Do not make changes to the running application until the test is complete (to avoid accidentally breaking a valid attack in progress)
- Disable services such as `fail2ban` on VMs during the test
- Any review results are not considered "final" — a formal security review by the customer's security team is required before moving an application into production

### For Those Performing Tests

- Do not attempt to perform Denial-of-Service attacks or otherwise crash services; heavy active scanning is tolerated
- Do not interact with human beings — phishing credentials or client-side attacks are off-limits; documenting XSS and similar vulnerabilities is encouraged, but do not leverage them against internal users or customers
- Attack from a single point and provide the IP address or hostname of the attacking host to avoid setting off alarms

---

## Resources

- [Non-Functional Requirements Guidance](../design/design-patterns/non-functional-requirements-capture-guide.md)
- [Azure DevOps Data Protection Overview](https://learn.microsoft.com/en-us/azure/devops/organizations/security/data-protection?view=azure-devops)
