# WinPlaybox Emergent Agent System

**A shared, project-agnostic operating system for AI coding agents across Winplaybox repositories.**

This repository is the single source of truth for common agent behavior. It is not part of any one product.

## Start here

- [Universal operating contract](AGENTS.md)
- [Idea-to-Production skill](skills/idea-to-production/SKILL.md)
- [Claude Code adapter](adapters/claude-code/README.md)
- [Codex adapter](adapters/codex/README.md)
- [Project instruction pointer template](templates/project-agent-pointer.md)

## What it does

Give an agent a plain-language product idea. The shared skill guides it to inspect existing resources, define requirements, plan architecture, build a working demo, test it, and prepare release materials.

## Non-negotiable rules

- Inspect existing repositories, cloud projects and integrations before creating new resources.
- Prefer free/open-source options and verify possible costs.
- Separate product requirements from internal agent instructions.
- Do not enable paid services, live payments, production ads, destructive migrations or public releases without explicit approval.
- Never claim work or tests succeeded unless verified.

## Use in any project

Keep each project's local agent file focused on project-specific context and link to this repository for common instructions. See the pointer template.

## Repository structure

```text
AGENTS.md
skills/
  idea-to-production/
    SKILL.md
adapters/
  claude-code/
  codex/
templates/
  project-agent-pointer.md
  shared-cook/
  india-product-crowdfunding/
```

The skill is intentionally stack-agnostic: it chooses technologies based on the product, current codebase, existing services, constraints and cost.

## Project pointers

### SharedCook
- [AGENTS.md](templates/shared-cook/AGENTS.md)
- [Claude Code](templates/shared-cook/CLAUDE.md)
- [Codex](templates/shared-cook/CODEX.md)
- Product specification: [Jira SCRUM-7](https://sagarsuthar530.atlassian.net/browse/SCRUM-7)

### India Product Crowdfunding (provisional codename)
- [AGENTS.md](templates/india-product-crowdfunding/AGENTS.md)
- [Claude Code](templates/india-product-crowdfunding/CLAUDE.md)
- [Codex](templates/india-product-crowdfunding/CODEX.md)
- Product specification: [Jira SCRUM-8](https://sagarsuthar530.atlassian.net/browse/SCRUM-8)
