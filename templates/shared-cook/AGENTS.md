# SharedCook — project agent pointer

This project builds an India-first shared-cook platform for apartment societies. Jira product specification: https://sagarsuthar530.atlassian.net/browse/SCRUM-7

## Canonical agent instructions
- Universal contract: https://github.com/Winplaybox/emergentagent/blob/main/AGENTS.md
- Idea-to-Production skill: https://github.com/Winplaybox/emergentagent/blob/main/skills/idea-to-production/SKILL.md

Read both before substantial implementation. This file adds only product-specific context.

## Product context
- Working codename: SharedCook (not final branding).
- Users: residents/households, cooks/service professionals, society coordinators, platform operations/admin.
- Core workflow: aggregate household demand within a society, match only feasible and fairly compensated cook schedules, collect subscriptions, manage cook leave and verified backup substitutions.
- Trust principles: verified cooks, least-privilege handling of documents, transparent fees and cook earnings, realistic service/travel buffers, rest/leave protection and human support escalation.
- Initial inspiration: Mumbai/India. A launch locality or pilot society is not yet confirmed.

## Suggested stack (confirm against repo and connected services before adopting)
- React Native + Expo + TypeScript for resident/cook mobile experience.
- React + TypeScript for operations/admin web.
- Python 3.12+ + FastAPI for backend.
- Supabase Postgres/Auth/Storage/RLS for data and identity.
- GitHub Actions and free/open-source-first tooling.

## Non-negotiable product constraints
- Do not assume five flats can be served in one time window; use explicit service durations, travel buffers, cook capacity, rest and availability.
- Matching must not optimize household savings at the expense of cook safety, fair compensation, workload or commute.
- No live payments, payouts, paid maps/routing or production launch without owner approval and required legal/provider review.
- Demo transactions must be clearly simulated and cannot move real funds.
- Keep identity documents private, encrypted, access-controlled and subject to a retention/deletion policy.
- Never reuse an unrelated production database. Inspect existing Supabase projects first.

## Implementation entry point
Start with the SCRUM-7 acceptance criteria and shared Idea-to-Production workflow. Build a fictional-data resident/cook/admin demo before provisioning or enabling external side effects.
