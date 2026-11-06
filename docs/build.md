# Build, review and update

`python scripts/ci.py --output NEW_EXTERNAL_DIRECTORY` is the single complete source check. Run it with the Python 3.14 environment installed from `requirements.txt`. Do not use an existing output folder; old and failed evidence stays intact.

For one package only:

```sh
python scripts/build.py --language en --out /outside/repo/Capitals-en-488.apkg
python scripts/build.py --language fr --out /outside/repo/Capitales-fr-488.apkg
```

## Source layout

| Path | Purpose |
|---|---|
| `source/places.json` | Shared named places, applicability, capital roles and provenance |
| `source/languages/` | English/French field names and small interface text |
| `source/continents.json` | Geographic convention, memberships and bilingual search labels |
| `source/curriculum.json` | Exercises and new-card introduction order |
| `source/identities.json` | Frozen candidate GUID, deck/model/field/template identities |
| `scripts/` | Builder and CI |
| `scripts/checks/`, `tests/` | Source, Anki round-trip and reproducibility checks |

## Gallery metadata

RectoVerso's gallery reads this deck from `rectoverso.json` and each package's `.rectoverso.json` sidecar, attached to the release with the release's `SHA256SUMS` (the contract: [RectoVerso #690](https://github.com/simonpinkas/RectoVerso/issues/690)). Beside the identity and version: the headline and description in each language, the categories, the creator, the license, the upstream sources, and under each language its `sample`, the GUID of the card the gallery opens as the deck's sample question. A sample is one of that language's cards and shows alone with all its pictures; `scripts/checks/verify-source.py` checks it.

## Gallery covers

To render just the cover masters into an external directory:

```sh
python scripts/covers.py --output /outside/repo/covers
python scripts/checks/verify-covers.py --output /outside/repo/covers
```

The masters are SVGs in `artwork/covers/`, named
`rv-capitals[-<en|fr>]-cover[-<light|dark>]-<n>.svg` (brackets mean optional).
Omit the language for artwork without words, shared by every language. Omit the
appearance when one file serves both light and dark mode. Include a language or
appearance only when the artwork differs by it. Use lowercase and number from 1.
A worded cover needs every shipped language at the same number and appearance
(including an omitted appearance). At one number, shared and localized files
cannot coexist; within one language, shared-appearance and explicit-appearance
files cannot coexist either.

The four current masters use the approved charcoal artwork for both appearances.
Each replaces a light/dark pair confirmed identical by SHA-256, without changing
the SVG bytes. Lettering is outlined
so the pinned renderer does not need system fonts. Masters must have a 3:2
viewport; the renderer rejects any other ratio before writing the final PNGs.

The package builder renders all masters beside the package and sidecar as
2,010 × 1,340 PNGs. CI checks filenames, dimensions, both appearances for
each language, complete localized sets, unambiguous scopes, and a uniform upper-right corner
(`x ≥ 1608`, `y ≤ 335`, within 4 per channel of the corner's dominant colour).
It compares PNG bytes across independent builds and attaches the rendered PNGs
to the Actions run as the `capitals-covers` artifact. Generated files belong
outside the checkout.

### Artwork provenance

Original vector compositions © Simon Pinkas, CC BY 4.0. The landmark paths
were drawn using the references below. The question is the published
Australia → Canberra gallery sample. Its SF and SF Mono letter shapes are
outlined, with no font files included.

The outlined lettering derives from Apple's system font files below, identified
by their embedded version and SHA-256. Font software remains © Apple Inc. under
its own terms, separate from the composition's CC BY 4.0 attribution. The
`SFNS.ttf` license record refers to the applicable OS software license; the
`SFNSMono.ttf` record contains the Apple SF Mono license. See [Apple's font
information and licensing](https://developer.apple.com/fonts/). These font files
are authoring provenance only; rebuilding uses the tracked paths.

| Authoring source | Embedded version | SHA-256 |
|---|---|---|
| macOS `/System/Library/Fonts/SFNS.ttf` | `22.0d5e1` | `44890958f3e0b997028121ed7c7a789f3f5cce227c7a93ce8f86ec0db26da571` |
| macOS `/System/Library/Fonts/SFNSMono.ttf` | `22.0d3e3` | `fc99d1608690ab5f2e1f78af9fbd4ef9ffef61f3eef36ceeea3ac3c844e652d4` |

| Master (shared by both appearances) | Reference | SHA-256 |
|---|---|---|
| [rv-capitals-cover-1.svg](../artwork/covers/rv-capitals-cover-1.svg) | [Colosseum](https://colosseo.it/en/area/colosseo/), [Eiffel Tower elevation](https://www.musee-orsay.fr/fr/oeuvres/elevation-generale-de-la-tour-eiffel-68404), [Hall of Prayer for Good Harvests](https://whc.unesco.org/en/list/881/gallery/) | `e989a70d4b0d8c9221a0c682a5a8f3a93941c90378b7414a231e3f0345a84f8d` |
| [rv-capitals-en-cover-2.svg](../artwork/covers/rv-capitals-en-cover-2.svg) | [Sample](../rectoverso.json), [place and answer](../source/places.json) | `c93bd9ff9921727777c2ec9903d1a7205f6e3f6bd5311556471c4bcf86f42e00` |
| [rv-capitals-fr-cover-2.svg](../artwork/covers/rv-capitals-fr-cover-2.svg) | [Sample](../rectoverso.json), [place and answer](../source/places.json) | `e636768775b328066d8271ef62cbad14ca3d56df705592dbd072d4875a56c6a0` |
| [rv-capitals-cover-3.svg](../artwork/covers/rv-capitals-cover-3.svg) | [U.S. Capitol](https://www.aoc.gov/explore-capitol-campus/buildings-grounds/capitol-building), [Martyrs’ Memorial](https://ont.dz/en/news/fb-708e03d18d26c2161591d8b6/), [National Congress](https://www2.camara.leg.br/english/visiting-the-chamber) | `f990112cc75c40b50c0cc5c58e783957d9e87b8f02214fb074b4dbc3eeab7428` |

## Updating a published deck

1. Branch in this deck repository and attach the PR to a source issue.
2. Edit content, retaining published GUIDs, field IDs and template IDs. Date a new reviewed version using `contentModifiedAt`; never forge a future modification time.
3. Run complete CI from the branch and a clean clone. Test an actual prior release → candidate import with existing progress: import the published predecessor (0.1.0-rc.1 for 0.1.0-rc.2) into a disposable Anki collection, study it, then import the candidate with Anki’s default import and with **Always**. Every note GUID, the studied schedules and the review log must survive. A duplicate import is not misrepresented as a historical upgrade.
4. Review native Anki and RectoVerso cards, both languages/themes, all capital-role cases, search aliases and post-answer notes.
5. Obtain owner approval for source/release publication. Publish source and the two package assets only after that approval.
6. Update the app’s submodule pointer and catalog through its feature branch and compatibility checks. Deck CI does not deploy an Apple asset pack or start Xcode Cloud by itself.

## Remaining release gates

- Owner editorial/visual review, including the documented holds and disputed-role wording.
- Native Anki desktop and RectoVerso import/study confirmation; backend validation is separate.
- Source review and branch protection: see [the review record](review.md). The hosted workflow exposes the exact **Anki packages** check; require it before merging. A workflow existing in source is not evidence that branch protection is active.
- Publication approval and versioned artifact hashes in the app catalog.

See [validation and reviewer evidence](validation.md) for automated checks and the remaining manual review gates.
