---
name: commerce-acf-api-dto
description: Use when creating or reviewing CommerceCore WordPress ACF Flexible Content structures, REST API DTO mappers/controllers, or React template wiring for product-page, quiz-builder, upsell-flex, builder-page, or similar template families.
---

# Commerce ACF/API DTO

Use this skill when a CommerceCore template needs ACF JSON, a normalized API DTO, or frontend wiring that consumes section data.

## Workflow

1. Read the repo-local `AGENTS.md` and `AI-CONTRIBUTING.md` when present and treat them as the shared source of truth for repo conventions and AI doc precedence.
2. Identify the template family, post type, template slug, and frontend component props before editing fields or DTOs.
3. For ACF Flexible Content rules, read [references/acf-flexible-content.md](references/acf-flexible-content.md).
4. For REST controller, mapper, helper, and normalization rules, read [references/api-dto.md](references/api-dto.md).
5. For Vite/React template and section-renderer conventions, read [references/frontend-template.md](references/frontend-template.md).
6. When the task adds or changes shared React sections or their stories in this repo, also read `src/sections/README.md` and `STORYBOOK.md`.
7. Preserve existing endpoints and templates unless the task explicitly asks for a breaking replacement.
8. Validate with JSON parsing, PHP linting, route search, and frontend build when dependencies are available.

## Policy Precedence

- Prefer committed repo docs first: `AGENTS.md`, `AI-CONTRIBUTING.md`, and any task-specific committed docs relevant to the template family.
- Use this skill's references for CommerceCore-specific ACF, DTO, controller, and frontend wiring guidance.
- Treat repo-local `tmp/*` notes and other private notes as optional personal context only. They must not override committed repo policy.

## Defaults

- For this CommerceCore project, treat `parent-v2-main` as the main/integration base branch when comparing changes or preparing PRs.
- Use snake_case for ACF field `name` values; DTO mappers should translate ACF snake_case keys into the frontend prop names expected by React components.
- Prefer parent-theme implementations unless the user names a child theme.
- Keep controller methods thin and move section-specific DTO mapping into mapper classes.
- Use admin-controlled Flexible Content row order as frontend section order.
- For image alt text, prefer ACF image fields with `return_format: array` and read the media alt via the shared image object helper; do not create separate ACF text fields only for alt text.
- Treat new template families as future-extensible: add mapper classes instead of growing a monolithic controller.
