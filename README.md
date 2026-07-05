# Engincan Varan — CV

Source for my CV, available as a web page and a downloadable PDF.

**Live:** [engincanvaran.github.io](https://EngincanVaran.github.io/cv-github)

---

## Structure

| File | Purpose |
|---|---|
| `main.tex` | LaTeX source — single source of truth for all content |
| `index.html` | HTML version served via GitHub Pages |
| `build_cv.py` | Python build script |
| `Makefile` | Convenience targets (`deps`, `build`, `clean`) |
| `.github/workflows/build.yml` | CI — validates the PDF compiles on every push to `main.tex` |

> **Rule:** `main.tex` and `index.html` must always be kept in sync. Edit content in `main.tex` first, then mirror changes to `index.html`.

---

## Local build

**First time — install [tectonic](https://tectonic-typesetting.github.io):**

```bash
make deps
```

**Build the PDF:**

```bash
make build        # → engincan_varan_cv.pdf
```

**Clean up:**

```bash
make clean
```

> Tectonic auto-downloads any required LaTeX packages on first build. No `tlmgr` or manual package management needed.

---

## CI

Every push that touches `main.tex` triggers a GitHub Actions workflow that compiles the PDF and uploads it as a downloadable artifact (retained 30 days). See the **Actions** tab.
