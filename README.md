# Capitals

Connect places and their capitals, in both directions.

[Français](README.fr.md) · [Coverage and sources](docs/coverage.md) · [Build and update](docs/build.md)

**Prerelease 0.1.0-rc.1.** [Download the English/French Anki packages](https://github.com/rectoversohq/rectoverso-capitals/releases/tag/v0.1.0-rc.1).

| | |
|---|---|
| Languages | English · Français — two packages from one shared source |
| Cards | 488 per language |
| Reference | 249 ISO countries and territories; only applicable exercises |
| Exercises | place → capital, capital → place |
| Content | Text only; no image downloads |
| License | CC BY 4.0, with original asset licenses retained |

Capital and government-seat roles stay explicit. Continent and region fields support discovery without cluttering the question. In Anki, **Explore** opens a short answer note. In RectoVerso, compatible importers expose that note after confirmation; app import and native visual review remain separate checks.

Answer context uses separately labeled **Continent** and **Region** fields. See [owner feedback and update semantics](docs/coverage.md#owner-feedback-and-context-labels).

## Get the source

The complete candidate is reviewed in [source issue #1](https://github.com/rectoversohq/rectoverso-capitals/issues/1). Clone the tagged source to reproduce this prerelease:

```sh
git clone --branch v0.1.0-rc.1 https://github.com/rectoversohq/rectoverso-capitals.git
cd rectoverso-capitals
```

See [source review and validation status](docs/review.md).

## Build for Anki

Use Python 3.14 and the pinned Anki backend. No account, API key or paid service is needed. This text-only deck builds directly from its tracked JSON records; no drawing tool or image download is needed.

```sh
python3.14 -m venv /path/outside-the-repo/anki-venv
/path/outside-the-repo/anki-venv/bin/python -m pip install -r requirements.txt
/path/outside-the-repo/anki-venv/bin/python scripts/ci.py --output /path/outside-the-repo/first-build
```

The output must be a **new directory outside this checkout**. CI builds each language twice, checks semantic reproducibility, imports every card into Anki, renders both sides, performs a real study action, and verifies media plus progress through export/reimport. Reports and failed logs remain beside the packages.

Open `packages/Capitals-en-488.apkg` or `packages/Capitales-fr-488.apkg` in Anki. Choose the language you want; these are independent study collections, not a language toggle applied to existing progress.

## Edit and update

Create a source-repository feature branch. Edit the shared records or language files, keep stable identities, and run the same CI command into a new output directory. Before a release, review the [explicit exceptions](docs/coverage.md), both languages, light/dark presentation and native app behavior. A passing build is not permission to publish.

Small, attributable corrections belong here; app rendering, search and entitlement changes belong in the app repository. See [the source layout and release checklist](docs/build.md).

## Credit

Learner names and initial capital text draw on Ultimate Geography 5.3 (public domain), with primary-source corrections recorded on each place. The common learner names follow the reviewed Maps roster. Each capital record links the evidence for its spelling and role. New authored material © Simon Pinkas. Read [NOTICE](NOTICE.md) and [LICENSE](LICENSE.md) for the actual boundaries of each license.
