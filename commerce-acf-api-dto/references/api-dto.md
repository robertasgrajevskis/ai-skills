# API DTO Rules

DTO endpoints should return stable, frontend-oriented data, not raw `get_fields()` output.

## Controller Pattern

- Keep existing legacy endpoints backward-compatible.
- Add a dedicated DTO action and route for new frontend templates when the existing endpoint has legacy shape.
- Validate: post exists, expected post type, published status, and expected template slug.
- Return clear `400` responses for wrong post type/template and `404` for missing posts.
- Delegate mapping to a mapper class; the controller should mostly validate and return `WP_REST_Response`.

## Mapper Pattern

- Put template-family mappers under `src/CcRestApi/Mappers/<Family>`.
- Use a shared helper for booleans, nullable numbers, image URLs/objects, URLs, links, rich text, and money when repeated.
- Preserve frontend prop names in DTO `data`.
- Map ACF `tr_*` fields to the component prop name without the prefix, such as `tr_heading` to `heading`.
- Explicitly cast booleans, integers, floats, enum strings, and nullable values.
- Normalize images to the exact shape expected by the React component: URL string or `{ url, alt }`.
- When a component expects separate URL and alt props, still read the alt from `Helper::imageObject($row['image'] ?? null)` or the equivalent image array helper, then emit the existing prop shape, for example `image` plus `imageAlt`.
- Do not read separate ACF alt text fields such as `imageAlt`, `iconAlt`, `productImageAlt`, or `badgeImageAlt` unless there is an explicit product/content requirement to override the media-library alt.
- Sanitize WYSIWYG/rich text fields through the shared mapper helper when available, for example `Helper::wysiwyg()`.
- Skip unknown layouts and inactive layouts.
- Keep future template families separate; do not add unrelated section logic to a product-page mapper.

## Section DTO Shape

Use:

```php
[
    'acf_fc_layout' => 'section_layout_name',
    'data' => [
        // frontend props
    ],
]
```

For block-based React components, `data` may contain `block` plus any extra component props such as `headingLevel`.

For Product Page Builder sections, optional editor anchors should live as top-level section metadata:

```php
[
    'acf_fc_layout' => 'section_layout_name',
    'anchorId' => 'reviews',
    'data' => [
        // frontend props
    ],
]
```

- Map ACF `section_anchor` to optional top-level `anchorId`, not into component `data`.
- Normalize anchors in the mapper: trim, remove a leading `#`, lowercase, replace invalid characters or spaces with `-`, and strip leading/trailing `-`.
- Omit `anchorId` when the normalized value is empty.
- Keep Navbar and other link href mapping unchanged; URL helpers such as `Helper::urlOrNull()` should preserve hash-only links like `#reviews`.
