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

- Prefer committed repo docs in this order when present: `AGENTS.md`, `AI-CONTRIBUTING.md`, `src/sections/README.md`, `THEMING.md`, `STORYBOOK.md`.
- `THEMING.md` is the source of truth for the design-system color tokens (`--theme-color-*`) and the themed-color patterns. It is the only committed doc covering theming, so consult it whenever a section sets, defaults, or overrides colors.
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
3. Apply the repo's current refactor-phase guidance before raising compatibility findings. If committed docs say there are no existing consumers or that an API migration is intentional, do not flag breaking API or shared default changes unless the task explicitly requires compatibility.
4. In ordinary branch review, do not flag older untouched sections for not matching new conventions. Mention them only when the branch touches them or the task is a full section audit/migration.
5. Report findings first, ordered by severity, with file/line references.
6. If no findings are found, state that and mention any residual test or design risks.

## Current Repo Direction

- Committed repo docs are the source of truth. If this skill conflicts with `AGENTS.md` or `src/sections/README.md`, the committed docs win.
- Current product-page sections are in a pre-consumer refactor phase. Section APIs and shared defaults may change when the change aligns with the agreed direction.
- `HowToUseStepsHorizontal` is the reference implementation for section CTA and stock/shipping rendering.
- Prefer flat CTA props such as `cta`, `ctaLabel`, `ctaIcon`, `ctaHref`, `ctaBackgroundColor`, `ctaBackgroundGradient`, `ctaBackgroundHoverColor`, `ctaBackgroundHoverGradient`, `ctaTextColor`, and `ctaBorderColor`.
- Use `CTAButton` with `StockAndShippingLevel`, explicit `showShipBy` / `showStockLevel` controls, and override slots such as `classes.ctaWrapper`, `classes.ctaButton`, `classes.shipByWrapper`, and `classes.stockLevelWrapper`.
- Gallery-like section media assets follow committed docs in `src/sections/README.md`: `assetType` may be `image` or `video`, missing `assetType` defaults to `image`, image assets use image object fields, and video assets use `videoUrl`.
- In reviews, do not flag `assetType` / `videoUrl` in touched sections as inconsistent with older image-only patterns. Still flag missing usable-URL filtering, missing mixed media Storybook coverage, and image/video accessibility regressions.

## Non-Negotiables

- Follow layer boundaries: atoms -> molecules -> organisms -> sections.
- Preserve backward compatibility for existing shared atoms, molecules, and organisms unless committed repo docs identify the work as part of a pre-consumer refactor or intentional migration.
- Keep `className` for root styling and `classes` for nested element overrides.
- Define default class constants near the top of TSX components.
- Use semantic HTML and accessible image alt text.
- Keep JSX readable; extract complex chunks into named helpers or components.
- Avoid hardcoded content or styling that should be props.
- Use clear prop names aligned with repo conventions, such as `image`, `imageAlt`, `heading`, `description`, `text`, `label`, `cta`, `ctaLabel`, `ctaIcon`, `ctaHref`, `stockLevel`, `stockLevelLabel`, and `stockLevelLowLabel`.
- Do not add inline styles unless the existing pattern or runtime value requires it (setting CSS custom properties for per-prop color overrides is an allowed exception — see below).
- For CMS/runtime backgrounds that may be HEX or gradients, use Tailwind `[background:var(--token)]` or React `{ background: value }`; use `bg-(--token)` or `{ backgroundColor: value }` only for values guaranteed to be color-only.
- Make colors theme-aware. Every configurable color must default to a design-system token: `var(--theme-color-*, neutralFallback)`. Keep colors out of `DEFAULT_*` classes; put them in `THEMED_*` constants or in a `buildVars()` map (see `references/design-principles.md` and `THEMING.md`). Fallbacks must be neutral gray/blue, never a brand color. Map one style prop to exactly one token — never chain props onto a token with `??`.
