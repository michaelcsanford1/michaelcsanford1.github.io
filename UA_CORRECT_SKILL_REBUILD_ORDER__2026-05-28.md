# UA Correct Skill Rebuild Order

Date: 2026-05-28
Owner: Codex handoff
Purpose: Tell the next agent exactly what must happen if they are using the Understand Anything skill/plugin correctly.

## Decision

The current public site can remain as a temporary showable shell, but the Understand Anything layer should be treated as suspect until rebuilt or verified with real skill/plugin receipts.

The failure pattern was not cosmetic. The claimed 48/48 delivery included manually constructed or thin graph outputs, empty or shallow domain flows, zero tours, stranded dashboard pages, and insufficient browser QC. That is not acceptable for owner-facing or product-facing work.

## Non-Negotiable Standard

The agent must use the actual installed Understand Anything skill/plugin commands or the documented equivalent from the installed skill directory.

Shell-built JSON, hand-authored graph stubs, file-count summaries, or manually fabricated domain nodes do not count as completion.

Completion requires:

- Command evidence.
- Artifact evidence.
- Browser evidence.
- Screenshot evidence.
- Boundary language.
- Git evidence.

## Surfaces To Rebuild Or Verify

1. UK CAER active workspace
   - Path: `/Users/michael/Documents/Codex/2026-05-14/why-cant-i-change-my-damn`
   - Status goal: showable project orientation graph.
   - Do not treat generated graph facts as project-control truth.

2. Owen County
   - Path: `/Users/michael/Emperor-Palantir/projects/owen_county`
   - Status goal: project twin shell plus current-source work-order map.
   - Do not inherit UK CAER facts.

3. Chokshi
   - Path: `/Users/michael/Emperor-Palantir/projects/chokshi`
   - Status goal: either real current-source graph or clearly marked coming-soon surface.
   - If the available source set is only two files, do not present it as mature.

4. World Model
   - Path: `/Users/michael/Emperor-Palantir/world_model`
   - Status goal: doctrine/world-model graph.
   - Canon/rev discipline governs authority.

5. TCS
   - Path: `/Users/michael/Emperor-Palantir/plugins/tcs-construction`
   - Status goal: TCS domain graph and construction skill/control route map.
   - TCS explains process; project records govern project facts.

6. TCS Atlas
   - Path: `/Users/michael/Emperor-Palantir/CANON/atlas_tokens`
   - Status goal: governance-spine graph.
   - Preserve exact chain: SOP > SWK > WI > checklist > action plan > LMS.

## Required Command Work

For each surface, run the actual plugin or skill command set:

1. `/understand [path] --full`
   - Must produce `.understand-anything/knowledge-graph.json`.
   - Must include real scan evidence, not just a manually constructed graph.

2. `/understand-dashboard [path]`
   - Must launch or build a dashboard that can be opened in a browser.
   - JSON-only is not complete.

3. `/understand-domain --full`
   - Must produce domain flow artifacts with actual flow nodes and flow-step relationships.
   - Domains showing labels with `0 flows` are a failure.

4. `/understand-chat [query]`
   - Must run at least one grounded query per surface.
   - Save query, answer, and source/graph basis where the tool exposes it.

5. `/understand-diff`
   - Required only where the surface is a Git repo or active working tree.
   - If not applicable, receipt why.

6. `/understand-explain [key file or folder]`
   - Pick a load-bearing file or control folder per surface.
   - Save the explanation artifact.

7. `/understand-onboard`
   - Must generate an onboarding or guided-walkthrough artifact.
   - If the tool cannot generate tours, the agent must state that honestly and not claim tours exist.

8. `/understand-knowledge [wiki/control-doc dir]`
   - Required for CANON, Atlas, doctrine, and control-doc-style folders.
   - Use for knowledge/control docs, not only code.

## Required Receipts

For each surface, create a receipt with:

- Surface name.
- Absolute source path.
- Command run.
- Timestamp.
- Tool or skill path used.
- Output artifact paths.
- Node count.
- Edge count.
- Domain count.
- Flow count.
- Tour count.
- Screenshot path.
- Browser URL tested.
- Console error count.
- Known limitations.
- Reliance boundary.

Receipt file naming:

`UA_RECEIPT__<SURFACE>__2026-05-28.md`

## Browser QC Gate

The agent must open the generated public or local page in a browser and verify:

- Page loads.
- Every nav link works.
- Every button works or is removed.
- Every dashboard opens.
- Domain view is not empty unless explicitly labeled limited.
- Tour panel has real steps or the page labels that tours are pending.
- No user is stranded without a back link.
- Console has no errors.
- Screenshot is saved.

The Compass is not QC. The delivering agent owns this gate.

## Public Site Work After Correct Rebuild

After the real UA outputs exist:

1. Replace public dashboard artifacts under:
   - `/Users/michael/Emperor-Palantir/sanfordsystematic-site/ua-dashboards/<surface>/`

2. Update dashboard index:
   - Label mature surfaces as showable.
   - Label thin surfaces as limited preview or coming soon.
   - Remove anything that would embarrass the company in front of Devere.

3. Update human manifest:
   - `/Users/michael/Emperor-Palantir/sanfordsystematic-site/manifest.html`
   - `/Users/michael/Emperor-Palantir/sanfordsystematic-site/data/explanation-manifest.json`

4. Run full browser QC again.

5. Commit and push.

## Rewrite Recommendation

A full UA/dashboard rewrite is justified if any of these remain true:

- Domain view still shows `0 flows`.
- Tours are still absent.
- Owen and Chokshi remain thin but look mature.
- Dashboard pages still strand users.
- The artifacts cannot prove actual plugin/skill execution.
- The public site requires caveats to avoid embarrassment.

If rewritten, keep the current Sanford Systematic pages as the shell and rebuild the graph/dashboard layer behind them. Do not rewrite the public brand surface just to fix bad graph artifacts.

## Acceptance Criteria

The rebuild is accepted only when:

- All six surfaces have receipts.
- All six dashboard URLs open in a browser.
- At least UK CAER, World Model, TCS, and TCS Atlas have real tours or honest tour-pending labels.
- Domain views contain real flow relationships or are clearly marked limited.
- Thin projects are labeled limited.
- Manifest is human-readable.
- All public links return HTTP 200.
- Browser screenshots exist.
- Git commit and push are complete.

