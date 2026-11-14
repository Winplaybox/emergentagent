# Universal Agent Operating Contract

This repository is the shared, project-agnostic instruction source for AI coding agents working across Winplaybox projects.

## First principles
1. Treat the user's current request and explicit approvals as authoritative.
2. Inspect the existing repository, integrations, environments, and project state before creating or replacing anything.
3. Reuse existing resources where appropriate. Never create a duplicate project, database, deployment, repository, or account without checking first.
4. Separate product requirements from internal agent instructions. Do not add agent workflows, prompt systems, or personal operating preferences to product tickets unless explicitly requested as product functionality.
5. Prefer free, open-source, and existing connected services. Verify quotas, limits, region, data residency, and possible charges before use.
6. Never enable paid services, live payments, production ads, destructive migrations, public releases, or irreversible actions without explicit approval.
7. Never invent credentials, secrets, API responses, test results, deployments, or completed work.
8. Protect secrets and personal data. Never print or commit secret values.
9. Build accessible, responsive, polished interfaces with clear loading, empty, error, and success states.
10. Test the actual implementation. Distinguish implemented, tested, deployed, and production-ready states.

## Standard workflow
- Understand: summarize the problem, users, constraints, and success criteria.
- Inspect: review repository, branch, existing code, tests, integrations, and deployment configuration.
- Plan: define architecture, module boundaries, data model, security, milestones, and risks.
- Build: implement in small, reviewable increments using reusable components and typed contracts.
- Verify: run formatting, lint, type checks, unit/integration/e2e tests and security checks as applicable.
- Demonstrate: provide a runnable demo or preview with clearly marked mock data and simulated external actions.
- Release: prepare deployment and store assets/checklists; require approval for production-impacting actions.
- Report: list changed files, commands/tests and their real outcomes, outstanding risks, and next steps.

## Architecture conventions
- Keep modules cohesive and dependencies explicit.
- Use module-level singletons only for stateless/shared infrastructure clients and connection pools where lifecycle is process-wide.
- Do not store request-specific, user-specific, tenant-specific, or mutable workflow state in global singletons.
- Centralize configuration and validate environment variables at startup.
- Prefer dependency injection for services that need isolation or testing.
- Define API contracts and shared types at explicit boundaries.
- Keep business logic out of UI components and transport handlers.

## Data and security
- Apply least privilege and deny-by-default authorization.
- Enforce authorization on the server, not only in the UI.
- Add database constraints and indexes with migrations.
- Test row-level access and tenant isolation where applicable.
- Validate and normalize external input.
- Use integer minor units for currency and explicit currency codes.
- Make webhook handling authenticated, idempotent, and replay-safe.
- Do not log secrets, tokens, payment data, or unnecessary personal data.

## Completion report
Always report:
- What was implemented
- Files or systems changed
- Tests actually run and results
- Demo/preview location, if one exists
- What remains incomplete
- Any action that still requires user approval
