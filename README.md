# Vaishak Rajeev's Guide to Automotive Electronics

A static, single-page website: no build step, no server code, no database. All diagrams and simulations run in the browser.

## Files

| File | Purpose |
|---|---|
| `index.html` | The whole site (HTML, CSS and JavaScript in one file) |
| `favicon.svg` | Browser-tab icon |
| `robots.txt` | Allows search engines to index the site |
| `.nojekyll` | Tells GitHub Pages to serve files as-is |

The only external resource is Google Fonts. Without internet access the page falls back to system fonts and still works.

## Preview locally

Double-click `index.html`, or serve the folder:

```
python -m http.server 8000
```

then open http://localhost:8000.

## Deploy (pick one)

**Netlify (drag and drop, fastest)**
1. Go to https://app.netlify.com/drop
2. Drag this folder onto the page. You get a public `*.netlify.app` URL in seconds.
3. Optional: Site settings → Domain management to rename it or add your own domain.

**GitHub Pages (free, versioned)**
1. Create a public repository, e.g. `automotive-electronics-guide`.
2. Upload the contents of this folder to the repository root (keep `.nojekyll`).
3. Settings → Pages → Source: *Deploy from a branch* → `main` / `root` → Save.
4. The site appears at `https://<your-username>.github.io/automotive-electronics-guide/` within a minute or two.

**Cloudflare Pages / Vercel**
Create a new project, choose "direct upload" (Cloudflare) or import the GitHub repo (Vercel), and leave the build command empty and the output directory as `/`.

## Updating

Edit `index.html` and re-upload (Netlify) or commit and push (GitHub Pages). Chapters are `<section class="view" id="…">` blocks; the navigation uses `#hash` links, so no server routing is needed.

## Sources

Concepts and diagram structure reference *Bosch Automotive Electrics and Automotive Electronics* (5th ed.), cross-checked with the author's M.Tech course material, AUTOSAR specifications and Bosch CAN papers. See `docs/drive-sources-verification.md` for the source register and corrections. All diagrams are original drawings; no figures from the book are included.
