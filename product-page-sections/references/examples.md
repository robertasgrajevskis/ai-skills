# Examples

Use these examples as compact shape references, not copy-paste templates.

## ContentImage Blueprint

Goal: create a flexible molecule that displays heading, description, optional CTA, optional stock level, and an image with left/right layout variants.

Applied principles:

- Compose atoms (`Image`, `Text`) and molecules (`CTAButton`, `StockLevel`) inside an organism layout (`Hero`).
- Keep one purpose: rich content beside an image.
- Define default classes in constants.
- Use a dedicated props interface with defaults such as `imagePosition = 'right'`.
- Use `classes` for nested styling.
- Render optional content only when provided.
- Use prop names such as `image`, `imageAlt`, `heading`, `description`, `cta`, and `stockLevel`.

Good output shape:

```tsx
//#region Imports
import React from 'react';
import classNames from 'classnames';
import { Hero } from '../organisms/Hero';
import { Image } from '../atoms/Image';
import { Text } from '../atoms/Text';
import { CTAButton } from '../molecules/CtaButton';
import { StockLevel } from '../molecules/StockLevel';
import { ContentImageProps } from './interfaces/content-image';
//#endregion imports

//#region Default Classes
const DEFAULT_SECTION_CLASS = 'w-full [background:var(--content-image-bg-color)] py-12 md:py-20';
const DEFAULT_IMAGE_WRAPPER_CLASS = 'flex justify-center items-center';
const DEFAULT_IMAGE_CLASS = 'w-full h-auto object-contain max-h-96';
const DEFAULT_CONTENT_CLASS = 'flex flex-col gap-6';
const DEFAULT_HEADING_CLASS =
  'text-[28px] md:text-[36px] lg:text-[40px] font-black leading-tight text-(--content-image-heading-color)';
const DEFAULT_DESCRIPTION_CLASS = 'text-base text-(--content-image-text-color) leading-relaxed';
const DEFAULT_CTA_WRAPPER_CLASS = 'flex flex-col gap-3 pt-4';
//#endregion

export const ContentImage: React.FC<ContentImageProps> = ({
  image,
  imageAlt = '',
  heading,
  description,
  imagePosition = 'right',
  cta = false,
  ctaText,
  ctaIcon,
  stockLabel = '',
  stockLevel,
  stockLowLabel,
  className,
  classes = {},
}) => {
  const imageColumn = (
    <div className={classNames(DEFAULT_IMAGE_WRAPPER_CLASS, classes.imageWrapper)}>
      <Image src={image} alt={imageAlt} className={classNames(DEFAULT_IMAGE_CLASS, classes.image)} />
    </div>
  );

  const contentColumn = (
    <div className={classNames(DEFAULT_CONTENT_CLASS, classes.content)}>
      {heading && <Text className={classNames(DEFAULT_HEADING_CLASS, classes.heading)}>{heading}</Text>}
      {description && (
        <Text className={classNames(DEFAULT_DESCRIPTION_CLASS, classes.description)}>
          {description}
        </Text>
      )}
      {cta && (
        <div className={classNames(DEFAULT_CTA_WRAPPER_CLASS, classes.ctaWrapper)}>
          {ctaText && <CTAButton buttonText={ctaText} icon={ctaIcon} classes={{ button: classes.cta }} />}
          {stockLabel && (
            <StockLevel
              label={stockLabel}
              level={stockLevel}
              lowLabel={stockLowLabel}
              className={classes.stockLevel}
            />
          )}
        </div>
      )}
    </div>
  );

  const left = imagePosition === 'left' ? imageColumn : contentColumn;
  const right = imagePosition === 'left' ? contentColumn : imageColumn;

  return (
    <section className={classNames(DEFAULT_SECTION_CLASS, className, classes.section)}>
      <Hero left={left} right={right} classes={{ base: classes.hero, left: classes.left, right: classes.right }} />
    </section>
  );
};
```

### Theming the blueprint

The local `--content-image-*` vars above must default to design-system tokens so any active theme applies. Keep colors out of `DEFAULT_*` and resolve them through a `buildVars()` map applied to the root `style`:

```tsx
function buildVars({
  sectionBgColor,
  headingTextColor,
  textColor,
}: Pick<ContentImageProps, 'sectionBgColor' | 'headingTextColor' | 'textColor'>): React.CSSProperties {
  return {
    '--content-image-bg-color': sectionBgColor ?? 'var(--theme-color-bg-page, #FFFFFF)',
    '--content-image-heading-color': headingTextColor ?? 'var(--theme-color-heading-primary, #000000)',
    '--content-image-text-color': textColor ?? 'var(--theme-color-text-primary, #333333)',
  } as React.CSSProperties;
}

// <section className={...} style={buildVars({ sectionBgColor, headingTextColor, textColor })}>
```

Fallbacks stay neutral, each prop maps to one token, and an unset prop is omitted so the theme value survives. See `references/design-principles.md` and `THEMING.md`.

## ProductBenefitsSection Pattern

- Direct typed section props.
- Uses `SectionHeader`.
- Uses `ul`/`li` for repeated benefits.
- Computes layout classes from `benefits.length`.
- Includes Storybook variants for 3, 4, 5, and 6 items.

## SocialProofImagesMotion Pattern

- Thin section accepts a `block`.
- Maps CMS-like image data into a reusable `MarqueeImages` molecule.
- Returns `null` when no valid image URLs exist.
- Exposes speed and border-radius configuration through typed block fields.
- Adds both molecule and section stories.
