# Capitals: rules for agents

**Read `kit/AGENTS.md` first.** The deck kit ([rectoverso-deck-kit](https://github.com/rectoversohq/rectoverso-deck-kit), a submodule at `kit/`: `git submodule update --init kit`) holds what every deck follows: the deck contract, its check, and the rules for authoring, covers, languages, versions and releases. This file adds only this deck's own rules and checks.

## This deck
- **Capitals** (« Capitales »), `rectoversohq/rectoverso-capitals`, public. GUID prefix `rv-capitals`; languages English and French; license CC BY 4.0. Asks each place's capital, and the place of each capital.

## This repository
- **Read first:** README.md, README.fr.md, docs/coverage.md and rectoverso.json; docs/review.md records the reviewed snapshot, docs/build.md how the deck and its covers are built, docs/validation.md the checks' evidence, docs/decisions.md the dated decisions.
- **Where things are:** source content in source/, the covers' masters in artwork/covers/, builders in scripts/ (build.py, covers.py, source_data.py, ci.py), checks in scripts/checks/, tests in tests/, guides in docs/.
- **Before a commit:** `python scripts/ci.py --output <a new folder outside the repository>`, then again in a fresh clone.

## This deck's content
- **Coverage:** keep all 249 reference records (every place with an ISO 3166-1 code), and account in docs/coverage.md for each exercise that doesn't apply or is held back. The 39 regional questions are Maps' alone.
- **Never invent** a flag, a capital, artwork, a boundary or a fact. A flag's proportions and colors are its own, never a style.
- **Continents** agree with Maps' `continents.json` place by place; a difference is the owner's call.

## This deck's checks
- `python3 kit/check.py --rectoverso`: the deck contract, as RectoVerso's gallery takes a deck, by the kit pinned here (`kit/docs/check.md` explains each refusal). The workflow runs it first.
- `scripts/ci.py --output <folder>` builds both languages twice, checks the source (verify-source.py), the covers (verify-covers.py, comparing the two builds byte for byte), the packages in Anki (validate-anki.py), a rebuild's identities (validate-rebuild.py) and Anki's rendering for review; tests in tests/.
- Anki desktop's look and RectoVerso's own are separate checks: a rendering in Anki's backend isn't a visual approval.

## This deck's covers
- **Covers exist** (artwork/covers/): `rv-capitals-cover-1` (landmarks of capitals), `rv-capitals-en-cover-2` and `rv-capitals-fr-cover-2` (the sample question, Australia → Canberra, in each language), `rv-capitals-cover-3` (more landmarks), the same picture in light and dark mode. Their sources are in docs/build.md; the lettering is outlined from Apple's SF fonts, kept for now by the owner's call (2026-11-06).
- Not yet listed in rectoverso.json's `covers`: that comes with the next release (1.0.0), with the owner's go.

## The kit
- **Pinned at `kit/`, at a tag.** Moving it is a pull request of its own, with the check run again (`kit/docs/versioning.md`). Never edit a file under `kit/` from here.
- **A new field, value or form** is a change to the kit, made there first (`kit/CONTRIBUTING.md`): this deck never uses one alone.
