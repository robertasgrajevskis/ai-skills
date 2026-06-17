# ACF Flexible Content Rules

Use ACF JSON in the theme's `acf-json` directory for template field groups. Add the group key to the theme ACF loader when the project uses an allowlist for save routing.

## Field Group

- Use a clear title, template-specific location rule, and stable field names.
- Use snake_case for every ACF field `name` value, including nested group and repeater fields; keep `tr_` prefixes snake_case as well. Do not use frontend camelCase prop names as ACF field names.
- For builder templates, prefer one root Flexible Content field for ordered sections.
- Every layout starts with `is_active`; API DTO mappers skip inactive rows.
- For Product Page Builder layouts, add optional `section_anchor` near `is_active` when sections need editor-controlled hash targets. Instruct editors to enter the value without `#`, for example `reviews`, and to keep anchors unique per page.
- Row order in Flexible Content is the page section order.
- Update the root JSON `modified` timestamp whenever the JSON file changes.

## Translation

- Prefix admin-authored translatable text field names with `tr_`.
- Do not translate brand names, person names, numeric values, enum values, URLs, colors, booleans, IDs, class-like tokens, or media IDs.
- Select fields are never translated. Use stable values such as `left`, `right`, `slow`, `medium`, `fast`, `male`, `female`.
- If a select needs visible copy, add a separate text field for the visible label, for example `tr_gender_label`.

## Field Design

- Do not expose code-only React props in ACF: `className`, `classes`, `carouselClasses`, `cardClasses`, Tailwind overrides, or component internals.
- Use image fields with `return_format: array` when DTO mappers need URL and alt.
- Do not add separate text fields such as `imageAlt`, `iconAlt`, `productImageAlt`, or `badgeImageAlt` only to describe an ACF image. Editors should set the alt text on the WordPress media attachment, and DTO mappers should retrieve it from the image array.
- Use groups for cohesive nested objects and repeaters for arrays consumed by components.
- Add concise descriptions to complex repeaters, groups, image collections, and selects.
- Use WYSIWYG fields for rich admin-authored text that may need inline markup such as `<strong>`; set `toolbar: full` and `media_upload: 0`.
- Simple obvious text fields can omit descriptions.
- Keep ACF layout names aligned with DTO `acf_fc_layout` values and frontend switch cases.
- Prefer relying on the active theme for section colors rather than exposing per-section color fields. Sections default their colors to `--theme-color-*` tokens, so the theme already styles them. Add color-override ACF/DTO fields only when design requires a section to deviate from the theme; keep them optional and map each to the matching section color prop. Token rules and prop names are owned by the React docs (`THEMING.md`).
