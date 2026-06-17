# Review Checklist

Use this reference when reviewing PRs that add or modify product-page sections.

## Findings First

Write review output with findings first, ordered by severity. Include file/line references. Keep summaries brief and after findings.

## High Severity

- Runtime crash from missing required data checks.
- Shared atom/molecule behavior changed in a way that can break existing consumers.
- Section cannot compile or is not exported when it should be public.
- Accessibility issue that blocks meaningful use, such as non-semantic clickable UI or missing labels on controls.

## Medium Severity

- Missing typed interface or use of broad `any` for public data.
- Missing Storybook coverage for a new public section or support component.
- Required visual behavior not represented in responsive classes.
- Optional content renders empty wrappers or bad spacing.
- Consumer styling cannot target important nested elements.

## Low Severity

- Naming differs from repo conventions.
- Region markers are missing in new TSX files when nearby files use them.
- Story data is unrealistic but does not hide behavior.
- Minor class organization or duplicated literals.

## Section Checks

- Section lives in `src/sections`.
- Interface lives in `src/sections/interfaces`.
- Public section is exported from `src/index.ts`.
- Required repeated content returns `null` when empty.
- Section root is semantic and full-width when design requires it.
- `className` targets the root only.
- `classes` covers relevant nested elements.

## Supporting Component Checks

- New atoms/molecules are genuinely reusable.
- Existing shared components are changed only additively.
- Default classes are constants near the top.
- Optional props have sensible defaults.
- Semantic HTML is preserved.

## Storybook Checks

- New public atoms, molecules, and sections have stories.
- Stories cover meaningful variations.
- Responsive or count-dependent behavior is visible in stories.
- Full-width sections use `layout: 'fullscreen'`.

## Design Checks

- Do not blindly copy fixed text widths from design exports.
- Preserve specified spacing, sizing, and responsive breakpoints.
- Use existing primitives unless doing so weakens semantics or creates awkward APIs.
- Check that styling uses Tailwind CSS v4-compatible classes and follows existing repo syntax.
- Check that CMS/runtime backgrounds that may contain gradients use CSS `background`, not `background-color`, `bg-(--token)`, or React `{ backgroundColor: value }`.

## Theming Checks

Apply these to new sections and to colors in touched sections; do not flag untouched older sections (see SKILL.md "Review Workflow").

- Configurable colors default to a design-system token, `var(--theme-color-*, fallback)`, rather than a hardcoded color.
- Fallbacks are neutral (gray/blue), not brand colors.
- `DEFAULT_*` classes carry no color utilities — colors live in `THEMED_*` constants or a `buildVars()` map.
- Each color prop maps to exactly one token; no `??` chaining of multiple props onto one token.
- Per-prop overrides write CSS custom properties (inline `style` / `buildVars`), and an unset prop leaves the theme value intact rather than writing `undefined`.
