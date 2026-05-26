# Sanford Systematic Site Creation Receipt

Date: 2026-05-26

## What Was Created

Created a standalone static site source for the Sanford Systematic public front door.

First live route:

- `https://michaelcsanford1.github.io/sanfordsystematic-site/`

Target root route after DNS / Pages binding review:

- `https://sanfordsystematic.com`

Primary files:

- `index.html` - public front door for Sanford Systematic.
- `explain/constellation.html` - plain-English Constellation explanation page.
- `styles.css` - responsive visual system.
- `data/explanation-manifest.json` - generated explanation manifest from the local Constellation Understand Anything graph.
- `tools/update_explanation_manifest.py` - repeatable manifest refresh script.
- `assets/constellation-live-home.png` - current live Constellation role-selection screenshot.
- `assets/constellation-owner-view.png` - current live Constellation owner-view screenshot.
- `assets/jr-waving.png` - Jr character image for the explanation page.

## Inputs Used

- Local Constellation product surface at `https://constellation.sanfordsystematic.com`.
- Local Constellation Understand Anything graph at `/Users/michael/Emperor-Palantir/constellation/.understand-anything/knowledge-graph.json`.
- Domain registry and route-boundary notes in `/Users/michael/Emperor-Palantir/SSU_DOMAIN_REGISTRY_2026-05-22.md`.
- Constellation / Sanford Systematic product-positioning notes in `/Users/michael/Emperor-Palantir/CONSTELLATION_PATIENT_ZERO.md`.

## Verification

- `https://constellation.sanfordsystematic.com` returned HTTP 200 during creation.
- `https://sanfordsystematic.com` returned HTTP 403 during creation, so the root domain was not live from this environment.
- GitHub rejected direct custom-domain binding for `sanfordsystematic.com` during first deploy, so the first live version uses the GitHub Pages project URL.
- Local static preview served from `http://127.0.0.1:8088`.
- Desktop and mobile Playwright smoke checks passed for the home page and Constellation explanation page.
- Smoke checks found no page errors, request failures, or horizontal overflow.
- Manifest updater completed and wrote the graph metadata, layers, tour, and authority boundary.

## Authority Boundary

This site is an explanation layer. It is not contract authority, Sage authority, owner approval, field direction, payment support, project-control validation, or an owner/client reliance upgrade.

The site may explain:

- Sanford Systematic.
- Constellation.
- Project digital twin concepts.
- Jr as an interface.
- Source, citation, inference, and human-review discipline.

The site must not publish:

- Private canon.
- Credentials.
- Live customer records.
- Unreviewed project-control facts.
- Sage state.
- Contract claims.
- Field instructions.
- Owner/client reliance claims.

## Next Required Reviews

- Human product-owner review before making `sanfordsystematic.com` public.
- DNS / Cloudflare route review before changing the root domain.
- Copy review for public clarity and owner-facing tone.
- Scheduled manifest refresh only after the source graph refresh workflow is approved.
- Link review before adding any real project artifacts or Constellation deep links.
