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
- Use `LinkEnhancer` for link behavior when the project uses `@commerce-core/react-components`.
- Activate a theme by feeding `getCheckoutThemeVariables(themeName)` to `ThemeProvider`, or by injecting its kebab-cased output as `--theme-color-*` custom properties in a `<style>` block for non-React/static pages (see `THEMING.md`). `themeName` is one of `velvet`, `amber`, `cobalt`, `ember`, `sage`, `ocean`, `noir`. Despite its name, `getCheckoutThemeVariables` returns the shared design-system tokens used by all sections — product-page sections included — not checkout-only variables; use it (kebab-cased) rather than the raw `getThemeVariables`.
- Render sections with a switch on `acf_fc_layout`; unknown layouts should render nothing.
- Apply section-level runtime metadata, such as Product Page Builder `anchorId`, in the template section wrapper after content renders. Do not add shared React section props only to support CMS wrapper behavior.
- Clean hash scrolling or URL cleanup may be implemented in the template runtime when marketing UX requires hash links to scroll without leaving the hash in the address bar.
- Do not pass ACF-managed Tailwind/class override props unless the template explicitly owns design-system class controls.

## Component Mapping

- Read component interfaces before creating ACF fields or DTO data.
- Block-based sections receive `{ block: ... }`.
- Direct-prop sections receive the props directly in `data`.
- Keep DTO prop names identical to React prop names after translation-prefix removal.
- Use the component library's rich-text renderer when available for DTO data that contains WYSIWYG HTML. Use `html-react-parser` only in templates that do not have a shared rich-text component.
- Use all ready exported non-Quiz sections requested by the template, and exclude Quiz-only components unless the task asks for quiz support.
