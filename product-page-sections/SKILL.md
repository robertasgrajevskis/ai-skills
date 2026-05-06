---
name: product-page-sections
description: Create and review product-page section components in the commerce React component library. Use when building or reviewing src/sections components, section interfaces, supporting atoms/molecules, Storybook stories, exports, or checking the repo's Atomic Design, DEFAULT_*_CLASS, className/classes, accessibility, and section block patterns.
---

# Product Page Sections

Use this skill for product-page section implementation and PR review in the React component library.

## First Steps

1. Read the repo-local `AGENTS.md` and `AI-CONTRIBUTING.md` when present and treat them as the shared source of truth for repo conventions and AI doc precedence.
2. Inspect the current repo state before deciding:
   - `src/sections`
   - `src/sections/interfaces`
   - related `src/molecules` / `src/atoms`
   - `src/stories`
   - `src/index.ts`
3. Identify whether the request is **Create/Modify** or **Review**.
4. Load only the reference files needed for the task.

## Reference Selection

- Prefer committed repo docs in this order when present: `AGENTS.md`, `AI-CONTRIBUTING.md`, `src/sections/README.md`, `STORYBOOK.md`.
- Use this skill's references for product-section-specific workflow and review guidance.
- Treat repo-local `tmp/*` notes and other private notes as optional personal context only. They must not override committed repo policy. Do not confuse repo-local `tmp/` with the system `/tmp` directory.
- For implementation workflow and file patterns, read `references/section-patterns.md`.
- For PR review, read `references/review-checklist.md`.
- For design/API conventions, read `references/design-principles.md`.
- For concrete examples, read `references/examples.md`.

## Create Or Modify Workflow

1. Confirm the section's content model, responsive behavior, and visual source of truth.
2. Reuse existing atoms, molecules, organisms, and sections where they fit.
3. Create section interfaces in `src/sections/interfaces`.
4. Add or update the section component in `src/sections`.
5. Extract reusable support pieces into atoms or molecules only when likely reusable.
6. Add Storybook coverage for the section and any new public atom/molecule.
7. Export public components from `src/index.ts`.
8. Run `npm run build`; run `npm run build-storybook` when dependencies allow it.

## Review Workflow

1. Review changed files and nearby existing patterns before forming findings.
2. Prioritize behavioral bugs, regressions, API risks, accessibility issues, missing Storybook coverage, and incompatible shared-component edits.
3. Report findings first, ordered by severity, with file/line references.
4. If no findings are found, state that and mention any residual test or design risks.

## Non-Negotiables

- Follow layer boundaries: atoms -> molecules -> organisms -> sections.
- Preserve backward compatibility for existing shared atoms, molecules, and organisms.
- Keep `className` for root styling and `classes` for nested element overrides.
- Define default class constants near the top of TSX components.
- Use semantic HTML and accessible image alt text.
- Keep JSX readable; extract complex chunks into named helpers or components.
- Avoid hardcoded content or styling that should be props.
- Use clear prop names aligned with repo conventions, such as `image`, `imageAlt`, `heading`, `description`, `text`, `label`, `cta`, `ctaText`, `ctaIcon`, `ctaUrl`, `stockLevel`, `stockLabel`, and `lowLabel`.
- Do not add inline styles unless the existing pattern or runtime value requires it.
- For CMS/runtime backgrounds that may be HEX or gradients, use Tailwind `[background:var(--token)]` or React `{ background: value }`; use `bg-(--token)` or `{ backgroundColor: value }` only for values guaranteed to be color-only.
