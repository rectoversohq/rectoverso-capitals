# Decisions

## 2026-11-02 — Owner phone feedback

Answer context now exposes **Continent** and **Region** as separate English/French resources. Existing continent memberships and search aliases are unchanged. The new Region field is appended; existing deck/model/template/field identities remain intact.

The source remains a review candidate. Existing images, attribution, licenses and unaffected GUIDs remain intact. Where exercises are removed, their GUIDs are recorded separately and never reassigned. Updating an existing test collection does not delete retired cards; validation explicitly checks that limitation instead of claiming a clean replacement. Native app task visibility is tracked independently in [#655](https://github.com/simonpinkas/RectoVerso/issues/655).

## 2026-11-02 — Owner-authorized prerelease

The owner approved releasing all authored decks. Publish this reviewed bilingual candidate as 0.1.0-rc.1 after exact-head checks. This publication-only change updates package status and download/build instructions without changing note content, identities or artwork. Preserve the existing CC BY 4.0 license and original component rights. App pin/catalog delivery remains separate.
