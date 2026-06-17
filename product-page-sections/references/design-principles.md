# Design Principles

Use these rules when creating or reviewing product-page sections.

## Atomic Design

- Atoms are single-purpose UI primitives, such as `Text`, `Image`, `Icon`, `Divider`, and `Button`.
- Molecules compose atoms into reusable units, such as `SectionHeader`, `MarqueeImages`, and CTA groups.
- Organisms compose molecules/atoms into larger reusable chunks.
- Sections assemble the page-level modules used by the product page.

## Component Design

- Keep one clear purpose per component.
- Prefer composition over large prop surfaces.
- Pass prepared JSX or reusable components when behavior varies significantly.
- Extract reusable support pieces only when they are useful beyond one section.
- Avoid components that handle many unrelated variants.

## Props And Content

- Use a dedicated TypeScript interface for public props.
- Use optional props with sensible defaults.
- Prefer names such as `heading`, `subheading`, `description`, `text`, `image`, `imageAlt`, `icon`, `cta`, `ctaText`, `ctaUrl`, `variant`, and `position`.
- Render optional content conditionally.
- Keep content data typed instead of using `any`.

## Styling

- Define `DEFAULT_*_CLASS` constants near the top of each component.
- Use `className` for the root element.
- Use `classes` for nested element overrides.
- Merge default and consumer classes with the repo's class merging pattern.
- Keep styling in Tailwind CSS v4-compatible utility classes.
- Prefer existing repo Tailwind v4 patterns. Use `bg-(--token-name)` for color-only background tokens, but use `[background:var(--token-name)]` for configurable backgrounds that may contain gradients; likewise use React `{ background: value }` instead of `{ backgroundColor: value }` for runtime gradient-capable backgrounds.
- Do not introduce Tailwind v3-only config assumptions unless the repo already supports them.
- Avoid fixed text widths copied from design exports unless design explicitly requires them.

## Theming (design-system color tokens)

`src/checkout/theme.ts` defines a set of CSS custom properties (`--theme-color-*`) that registered themes (velvet, amber, cobalt, ember, sage, ocean, noir) populate at runtime. Sections must consume these tokens so any active theme applies automatically. `THEMING.md` is the committed source of truth; read it before touching colors.

- Never put colors in `DEFAULT_*` classes — those hold structure only (padding, flex, radius, font-size). Colors live in `THEMED_*` constants or in a `buildVars()` map.
- Every configurable color defaults to a token with a **neutral** fallback: `var(--theme-color-accent, #3B82F6)`, never a brand color as the fallback.
- Map one style/color prop to exactly one token. Do not chain multiple props onto one token with `??`.
- Omit a token entirely when its prop is `undefined` (don't write `undefined` into the style object) so the active theme value survives.

Two equivalent patterns are in use across `src/sections`; match whichever the surrounding file uses:

1. **`THEMED_*` class constants** (per `THEMING.md`) — color utilities reference tokens directly, merged with `DEFAULT_*` via `cn()`:

   ```tsx
   const DEFAULT_CARD_CLASS = 'rounded-xl border p-4 flex flex-col gap-2'; // no colors
   const THEMED_CARD_CLASS = 'bg-[var(--theme-color-bg-raised,#FAFAFA)] border-[var(--theme-color-border-light,#E5E7EB)]';
   <div className={cn(DEFAULT_CARD_CLASS, THEMED_CARD_CLASS)} />
   ```

2. **`buildVars()` local tokens** (e.g. `ContentImageSection.tsx`, `AboutProductCarouselSection.tsx`) — `DEFAULT_*` classes reference local section tokens, and a `buildVars()` function maps each color prop to `prop ?? var(--theme-color-*, neutralHex)`, applied via `style={buildVars(...)}`:

   ```tsx
   const DEFAULT_HEADING_CLASS = 'font-extrabold text-(--content-image-heading)';
   function buildVars({ headingTextColor }): React.CSSProperties {
     return {
       '--content-image-heading': headingTextColor ?? 'var(--theme-color-heading-primary, #000000)',
     } as React.CSSProperties;
   }
   ```

## Accessibility

- Use semantic elements such as `section`, `article`, `ul`, `li`, `h2`, and `p`.
- Provide useful `alt` text for meaningful images.
- Use empty alt text only for duplicated/decorative images.
- Do not weaken semantics just to reuse a component.
