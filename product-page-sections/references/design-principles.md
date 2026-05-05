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
- Prefer existing repo Tailwind v4 patterns, including CSS variable utilities such as `bg-(--token-name)` and `text-(--token-name)`.
- Do not introduce Tailwind v3-only config assumptions unless the repo already supports them.
- Avoid fixed text widths copied from design exports unless design explicitly requires them.

## Accessibility

- Use semantic elements such as `section`, `article`, `ul`, `li`, `h2`, and `p`.
- Provide useful `alt` text for meaningful images.
- Use empty alt text only for duplicated/decorative images.
- Do not weaken semantics just to reuse a component.
