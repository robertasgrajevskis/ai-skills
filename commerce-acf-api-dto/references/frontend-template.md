# Frontend Template Rules

Use the closest existing Vite/React template as the starting point for dependencies, config, and WordPress layout.

## WordPress Template

- Add a root `single-*.php` with `Template Name` and `Template Post Type`.
- Enqueue assets through `ViteForWp::enqueue_asset()` using the template's `js/dist` directory.
- Include a layout file that emits `<div id="react-app"></div>`.
- Expose `window.postId` and `window.apiUrl` for DTO fetching.

## React App

- Define TypeScript DTO types matching the PHP DTO.
- Fetch `/api/v1/<dto-route>/{postId}` with `credentials: "same-origin"`.
- Include loading and error states.
- Use `ThemeProvider` for variables and `LinkEnhancer` for link behavior when the project uses `@commerce-core/react-components`.
- Render sections with a switch on `acf_fc_layout`; unknown layouts should render nothing.
- Do not pass ACF-managed Tailwind/class override props unless the template explicitly owns design-system class controls.

## Component Mapping

- Read component interfaces before creating ACF fields or DTO data.
- Block-based sections receive `{ block: ... }`.
- Direct-prop sections receive the props directly in `data`.
- Keep DTO prop names identical to React prop names after translation-prefix removal.
- Use `html-react-parser` anywhere DTO data contains WYSIWYG HTML so inline tags such as `<strong>` render instead of escaping.
- Use all ready exported non-Quiz sections requested by the template, and exclude Quiz-only components unless the task asks for quiz support.
