# Section Patterns

Use this reference when implementing product-page sections in this repo.

## File Layout

- Section component: `src/sections/ComponentName.tsx`
- Section interface: `src/sections/interfaces/ComponentName.ts`
- Section story: `src/stories/ComponentName.stories.tsx`
- Supporting molecule: `src/molecules/ReusableName.tsx`
- Supporting atom: `src/atoms/ReusableName.tsx`
- Public exports: `src/index.ts`

## TSX Structure

Use region markers in TSX files:

```tsx
//#region imports
import React from 'react';
import classNames from 'classnames';
//#endregion imports

//#region types
interface ComponentProps {}
//#endregion types

//#region constants
const DEFAULT_CONTAINER_CLASS = '...';
//#endregion constants

//#region component
export const Component: React.FC<ComponentProps> = () => {};
//#endregion component
```

Use `//#region Default Classes` instead of `//#region constants` if the touched file already uses that exact label.

## Section API

- Prefer a `block` object for banner-style sections that map CMS-like data to a thin wrapper.
- Prefer direct typed props for standalone reusable sections when existing nearby sections use that pattern.
- Include `className?: string`.
- Include `classes?: { ... }` for nested overrides.
- Return `null` when required repeated content is empty.
- Do not include optional display-only content in required render guards. For example, an optional domain label should be conditionally rendered instead of making the whole section return `null`.

## Existing Useful Components

- `Text` supports `as` for semantic tag control.
- `Image` renders image sources and should be reused for image elements.
- `SectionHeader` supports `headingAs`, sanitized rich headings through `headingHtml`, `showSubheading`, optional divider visibility through `showDivider`, and `subheadingPlacement`.
- `CTAButton` treats empty string icons as missing and centers CTA text independently from a right-positioned icon.
- `StockAndShippingLevel` supports `shipByText` with a `{date}` token plus `daysFromNow` and `shipByLocale` for generated ship-by copy.
- `MarqueeText` is text-specific continuous motion.
- `MarqueeImages` is image-specific continuous motion.
- `GalleryCarousel` is interactive carousel behavior, not a marquee.
- `ReviewCarouselMotion` is the auto-scrolling review carousel implementation.
- `StickyCtaFloaterSection` is the public section pattern for sticky CTA, shipping, and stock UI.

## Storybook

- Add a story for every new public section, molecule, or atom.
- Use realistic example data.
- Include variation stories for speed, item count, long content, radius, missing optional content, or responsive behavior when relevant.
- Use `layout: 'fullscreen'` for full-width sections.

## Verification

- Run `npm run build`.
- Run `npm run build-storybook` when dependencies are installed.
- If Storybook fails because of unrelated missing dependencies, report the blocker and the exact import/package.
