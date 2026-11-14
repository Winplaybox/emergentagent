# FlatmateMatch — project agent pointer

This project is an India-first mobile app for compatible flatmate discovery and shared rentals. Product requirements: https://sagarsuthar530.atlassian.net/browse/SCRUM-9

## Canonical agent instructions
- Universal operating contract: https://github.com/Winplaybox/emergentagent/blob/main/AGENTS.md
- Idea-to-Production skill: https://github.com/Winplaybox/emergentagent/blob/main/skills/idea-to-production/SKILL.md

Read both before substantial implementation. This file adds product-specific context only; do not duplicate the shared workflow.

## Product context
- Working codename: FlatmateMatch (provisional; not final branding).
- Users: adults seeking a room/flatmate, existing tenants listing a room, and platform trust & safety operations.
- Core workflow: build profiles, declare housing and lifestyle preferences, discover explainably compatible people/listings, mutually connect, chat safely, and discuss expectations before moving in.
- Candidate preferences: budget, area, move-in date, sleep schedule, cleanliness, guests/noise, work-from-home, cooking, chores, pets and smoking compatibility.
- Preferences must be optional, user-controlled and neutrally worded. Users can mark unknown, skip or prefer not to disclose.

## Non-negotiable product constraints
- Build for eligible adults; define age eligibility with legal review.
- Treat compatibility as a transparent preference match, not a psychological assessment or guarantee of a successful tenancy.
- Explain why a match is suggested and show important differences.
- Do not infer or rank by caste, religion, health, sexuality, ethnicity or other sensitive traits.
- Avoid discriminatory housing filters and have Indian legal/privacy review for matching and listing rules.
- No unsolicited messaging; enforce mutual-connect or explicit enquiry rules.
- Exact home addresses, phone numbers and private contact details must not be publicly exposed.
- Include block/report, moderation, anti-scam guidance, rate limits and auditable admin actions.
- Verification badges must state exactly what was verified; phone verification is not identity verification, and identity verification is not a background check.
- Keep KYC/identity documents private, access-controlled and retention-limited. Do not collect unnecessary sensitive data.
- No rent collection, deposits, escrow, lease signing or landlord payouts in MVP.
- Inspect existing repositories and Supabase projects before provisioning. Never reuse unrelated production data.
- Do not enable paid services or public launch without explicit approval.

## Suggested technical direction
React Native + Expo + TypeScript is the candidate mobile stack. Admin web may use React + TypeScript. Evaluate backend, auth, storage and chat choices against the existing repository and connected resources before committing to a stack. Prefer free/open-source-first tooling and document costs.

## Implementation entry point
Start with SCRUM-9 and the shared Idea-to-Production workflow. Deliver a fictional-data prototype of onboarding, preference matching, listings and mutual-connect flows before provisioning external services.
