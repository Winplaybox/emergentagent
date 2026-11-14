---
name: idea-to-production
description: Turn a plain-language app or product idea into a scoped, architected, implemented, tested, demonstrated, and release-prepared software project. Use for new apps, features, MVPs, internal tools, websites, mobile apps, and automation products.
---

# Idea to Production

## Purpose
Convert the user's idea into a working software deliverable with minimal repeated questioning. This is a universal skill: adapt the stack to the idea and existing repository rather than forcing one fixed technology stack.

## Trigger
Use when the user describes a new product/app idea, asks to build an app, asks to turn an idea into a project, or asks to implement a substantial feature end to end.

## Interaction rules
- Treat the user's idea as the primary input. Do not ask them to repeat known preferences or standing constraints.
- Ask only for information that blocks safe or correct implementation. Prefer sensible, documented defaults for non-blocking details.
- Before asking about infrastructure, inspect connected services and existing projects first.
- Never create a new repository, cloud project, database, or deployment before checking whether a suitable existing resource is available.
- Never make irreversible, paid, public, or production-impacting changes without explicit approval.
- Keep internal agent process separate from end-user product scope and Jira/product requirements.

## Workflow

### 1. Discover and clarify
Extract:
- Problem and target users
- Main user journeys
- Platforms and accessibility needs
- Core features and non-goals
- Data sensitivity and compliance considerations
- Monetization and external integrations
- Success metrics and acceptance criteria

Ask one concise question at a time only when a missing answer materially changes the architecture, cost, security, or user experience.

### 2. Inspect before creating
- Inspect repository structure, existing implementation, branches, tests, package manager, CI and deployment.
- Inspect connected GitHub, Supabase, hosting, analytics, and other integrations where relevant.
- List existing projects and identify ownership, region, status, schema/data, auth configuration and cost tier.
- Reuse appropriate existing resources. Do not reuse unrelated production databases merely to avoid creating a project.
- Report what was found and obtain approval before creating or modifying infrastructure.

### 3. Product specification
Create a concise product specification with:
- Vision, personas, jobs-to-be-done and journeys
- Functional and non-functional requirements
- MVP versus later scope
- Acceptance criteria
- Analytics events and success metrics
- Risks, assumptions and open decisions

Keep product tickets focused on product outcomes. Put agent operating rules in this shared skill/repository.

### 4. Architecture and plan
Choose a stack based on requirements, existing code, maintainability, team familiarity, and total cost. Consider web, mobile, backend, database, auth, storage, background jobs, observability, CI/CD and deployment.

Produce:
- Architecture overview and data-flow diagram
- Repository folder tree
- Module responsibilities and dependency boundaries
- Data model and migration strategy
- API contracts
- AuthN/AuthZ and threat model
- Testing strategy
- Milestones and definition of done

Singleton guidance:
- Use module-level singleton instances for process-wide stateless clients, SDK clients and connection pools when appropriate.
- Never put per-request, per-user, per-tenant, mutable business state, or authorization context in a singleton.
- Make configuration explicit, validate it at startup, and provide test seams.

### 5. UX and implementation
- Build a coherent design system with tokens, typography, spacing, responsive breakpoints and reusable components.
- Include loading, empty, error, offline and success states.
- Use realistic but fictional demo data when backend credentials or production data are unavailable.
- Clearly label simulated payments, emails, notifications, and external side effects.
- Implement in small increments; keep code typed, documented where useful, and maintainable.
- Do not leave dead controls or fake functionality presented as working.

### 6. Backend and data
- Use migrations for schema changes.
- Apply least privilege, server-side authorization and row-level security where supported.
- Validate inputs and outputs.
- Add idempotency for retryable operations and webhooks.
- Use safe money and date/time representations.
- Never expose service-role keys or privileged secrets to clients.

### 7. Quality gates
Run the checks that exist and add appropriate tests:
- Formatting and lint
- Static analysis and type checking
- Unit tests
- Integration tests
- End-to-end critical journeys
- Accessibility and responsive checks
- Security and authorization tests
- Build and deployment preview validation

Never claim a check passed unless it was actually run and its result was observed.

### 8. Demo and release preparation
Deliver a working local demo or preview when feasible. Prepare:
- Setup guide and environment variable example
- Screenshots or demo walkthrough
- Store listing copy and required assets for mobile apps
- Privacy policy/data safety checklist where applicable
- Release checklist, rollback plan and monitoring notes

Keep production publishing, live payment processing, ads, paid services and public release disabled until explicitly approved.

### 9. Final report
Summarize:
- What works now
- What was changed
- How to run and test it
- Test results
- Demo/preview link if verified
- Remaining blockers and risks
- Decisions or approvals still needed

## Definition of done
A task is done only when the agreed acceptance criteria are implemented and verified. A design mock, plan, documentation-only scaffold, or successful deployment command is not by itself proof that the product is complete.
