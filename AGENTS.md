# Capitals: rules for agents

This repository is one deck of RectoVerso's Deck gallery: the Capitals deck, in English and French. Any agent working here (Codex, Claude Code or another) reads this file first. Three kinds of work happen here; find the one you're doing, read what it lists, and keep its rules. Work that crosses two kinds keeps both.

The rules every gallery deck follows are RectoVerso's `agents/decks.md`: `~/Dev/RectoVerso/agents/decks.md` on the owner's Mac. Until RectoVerso 1.1 is merged, its gallery side (the gallery's check, the Library page's deck contract and cover specification) is in the worktree `~/Dev/RectoVerso-worktrees/605-deck-gallery`. Read `agents/decks.md` whatever the work.

## For every kind of work
- **Read first:** README.md, README.fr.md, docs/coverage.md and rectoverso.json; docs/review.md records the reviewed snapshot, docs/build.md how the deck is built.
- **Where things are:** source content in source/, the covers' masters in artwork/covers/, builders in scripts/, checks in scripts/checks/, tests in tests/, guides in docs/.
- **The owner decides** coverage, names, conventions, categories, the sample, the covers and every release. Bring each choice with a recommendation; never settle it in the deck.
- **Git:** a branch and a pull request for every change; commit only your own files, by name; never force-push, rewrite pushed history, or push to main. A merge, a tag and a release each wait for the owner's go.
- **Outside Git:** packages, rendered covers and large evidence go outside the checkout (the owner's external drive), passed as arguments; no tool names a drive or a user's path. Keep failed evidence.
- **Before a commit:** `python scripts/ci.py --output <a new folder outside the repository>`, then again in a fresh clone.

## 1. Deck authoring: the content
The places, capitals, names, exercises, words and pictures the learner studies.
- Read `agents/decks.md`: "Content changes; identities don't", "Words" and "The owner's calls".
- **Coverage:** keep all 249 reference records, and account for each exercise that doesn't apply or is held back. The 39 regional questions are Maps' alone.
- **Never invent** a flag, a capital, artwork, a boundary or a fact: every fact is checked against an independent source, and every asset has its exact provenance, license and hash. A flag's proportions and colors are its own, never a style.
- **Every language is complete:** English in American spelling; French in the French of RectoVerso's `docs/app/languages.md` (its terms and typography: a narrow no-break space before ? ! : ; and inside « »). Names, role qualifiers, source notes and docs agree across languages.
- **New exercises** get stable note identities of their own; an existing exercise never becomes a different question. New-card stages are an introduction order, never a scheduler or an entitlement.
- **Search metadata** (RectoVerso search v1) is hidden from studying: only the learner-facing names, values and aliases, never geometry, ids or license text.
- Anki desktop's look and RectoVerso's own are separate checks: a rendering in the backend isn't a visual approval.

## 2. Contract honoring: what the app reads
rectoverso.json, the deck's identities, its packages and its releases: what RectoVerso's gallery and Anki rely on.
- Read `agents/decks.md`: "Content changes; identities don't", "One contract, changed everywhere at once", "Checks before the owner sees a candidate" and "Releases"; and the Library page's "A deck's metadata" (RectoVerso's `docs/app/library.md`).
- **The contract is RectoVerso's:** rectoverso.json holds only what the Library page specifies, as RectoVerso's gallery check (`scripts/gallery/decks.py check`) reads it. A new field, value or form is a change to RectoVerso's contract first, made there everywhere at once; never one the deck uses alone.
- **Identities never change** once a version has been published or studied: each note's GUID (`rv-capitals-<language>-…`, the deck's `guidPrefix`, then the language, then the note), the ids of its note types, fields, templates and deck, each language's package id.
- **Every content change is a new version,** with contentModifiedAt moved forward and what's new written in every language. The next release is 1.0.0, after the owner's review. A release attaches the packages, their sidecars and the covers, listed in its SHA256SUMS; rectoverso.json's `covers` lists the released covers per language and appearance.
- **Checks:** this deck's own, then RectoVerso's gallery check on the built packages, then Anki's (each package opens with its cards and media, and an update over the previous version keeps every review). A green check publishes nothing.

## 3. Cover making: the gallery's pictures
The covers the gallery shows for this deck. Their design is the owner's; this work is their masters, build and checks.
- Read the Library page's "Covers" (RectoVerso's `docs/app/library.md`) and `agents/decks.md`'s cover naming.
- **The specification:** 3:2 at exactly 2010 × 1340 px; the subject and any words inside x 221–1789, y 228–1112; the top-trailing corner (x ≥ 1608, y ≤ 335) clear for the app's language pill; never the deck's title (the app sets it beside the cover); words allowed, in each shipped language.
- **Names:** `rv-capitals[-<language>]-cover[-<light|dark>]-<n>.png`, n from 1 in the order shown. The language only on a cover with words (one file per language, the same n); without one, every language lists the same file. The appearance only on a cover made for light or dark mode; without one, the same file is both.
- **Masters** in artwork/covers/, SVG with the lettering outlined, named as their PNGs. scripts/covers.py renders them, from build.py, into the build's output folder; nothing rendered is committed. scripts/checks/verify-covers.py holds them to the specification in CI, and two independent builds give the same bytes. Tests in tests/test_covers.py.
- A new cover or a changed one is shown to the owner as rendered PNGs before it's merged; it reaches the app with the deck's next release.
