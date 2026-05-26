# Sanford Systematic Site

Static source for the public Sanford Systematic front door.

Live first-pass review URL:

`https://fc13d55b511e58.lhr.life/`

GitHub Pages target URL after GitHub public edge exposure resolves:

`https://michaelcsanford1.github.io/sanfordsystematic-site/`

Target root domain after DNS / Pages binding review:

`https://sanfordsystematic.com`

The site is designed as an explanation layer, not a project-control authority.
It links to live product surfaces and real artifacts while preserving source
boundaries.

## Local Preview

```bash
python3 -m http.server 8088
```

Then open `http://127.0.0.1:8088`.

## Update Explanation Data

```bash
python3 tools/update_explanation_manifest.py
```

The updater reads the Constellation Understand Anything graph and writes
`data/explanation-manifest.json`.

## Authority Boundary

This site may explain systems, workflows, and public architecture. It must not
publish live Devere project facts, Sage state, owner/client reliance claims,
private canon, credentials, or unreviewed customer artifacts.
