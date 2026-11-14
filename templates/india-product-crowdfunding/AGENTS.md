# India Product Crowdfunding — project agent pointer

This project is an India-first, all-or-nothing product crowdfunding and pre-order marketplace. Product requirements and acceptance criteria: https://sagarsuthar530.atlassian.net/browse/SCRUM-8

## Canonical agent instructions
- Universal operating contract: https://github.com/Winplaybox/emergentagent/blob/main/AGENTS.md
- Idea-to-Production skill: https://github.com/Winplaybox/emergentagent/blob/main/skills/idea-to-production/SKILL.md

Read both before substantial implementation. This file contains product-specific context only; do not duplicate or fork the shared workflow.

## Product context
- Working codename: IndiaProductCrowdfunding (provisional; not final branding).
- Users: product creators/makers, backers/customers, platform reviewers/operations, and later fulfilment partners.
- Core model: creators publish reviewed product campaigns; backers reserve/pre-order at disclosed campaign prices; a campaign succeeds only when its disclosed goal is reached by its deadline.
- Monetization: transparent platform commission on successful campaigns, subject to validated unit economics and legal review.
- Initial market: India. Pilot geography and creator segment are undecided.

## Non-negotiable product constraints
- Clearly distinguish pre-orders for proposed/in-development products from guaranteed purchases; disclose product risks, realistic delivery estimates, manufacturing plans, shipping, cancellation and refund terms.
- Do not present campaigns as equity investments, loans, guaranteed returns or risk-free backing.
- No creator campaign goes live without moderation and required disclosures.
- Implement all-or-nothing outcomes server-side with auditable campaign/payment state transitions and idempotent payment handling.
- Failed campaigns must not pay creators; successful-campaign collection and payout must use a legally reviewed, provider-supported flow.
- Do not hold or pool customer funds in an unapproved platform wallet or assume an escrow model is permitted.
- Sandbox/test payments only during development. No live charges, payouts, production credentials or public campaign launch without explicit owner approval and qualified Indian legal/compliance/payment-provider validation.
- Protect KYC, identity and payout information with least-privilege access, private storage, retention controls and audit logs.
- Never claim a payment succeeded based only on a browser redirect; verify signed provider webhooks and reconcile states.
- Inspect existing repositories and cloud projects before creating resources. Never reuse an unrelated production database.

## Suggested technical direction
Start responsive-web-first with React + TypeScript, and evaluate backend/data options against the repository and existing resources before choosing. FastAPI and Supabase are candidates, not mandatory decisions. Prefer free/open-source tooling and document costs before adoption.

## Implementation entry point
Start with the SCRUM-8 epic and shared Idea-to-Production skill. First deliver a fictional-data prototype and test-mode campaign lifecycle. Keep live payment, creator payout, public launch and paid services disabled by default.
