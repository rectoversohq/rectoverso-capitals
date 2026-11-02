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

## Updating a published deck

1. Branch in this deck repository and attach the PR to a source issue.
2. Edit content, retaining published GUIDs, field IDs and template IDs. Date a new reviewed version using `contentModifiedAt`; never forge a future modification time.
3. Run complete CI from the branch and a clean clone. Test an actual prior release → candidate import with existing progress if there is a published predecessor. This first candidate has none; a duplicate import is not misrepresented as a historical upgrade.
4. Review native Anki and RectoVerso cards, both languages/themes, all capital-role cases, search aliases and post-answer notes.
5. Obtain owner approval for source/release publication. Publish source and the two package assets only after that approval.
6. Update the app’s submodule pointer and catalog through its feature branch and compatibility checks. Deck CI does not deploy an Apple asset pack or start Xcode Cloud by itself.

## Remaining release gates

- Owner editorial/visual review, including the documented holds and disputed-role wording.
- Native Anki desktop and RectoVerso import/study confirmation; backend validation is separate.
- Source review and branch protection: see [the review record](review.md). The hosted workflow exposes the exact **Anki packages** check; require it before merging. A workflow existing in source is not evidence that branch protection is active.
- Publication approval and versioned artifact hashes in the app catalog.

See [validation and reviewer evidence](validation.md) for automated checks and the remaining manual review gates.
