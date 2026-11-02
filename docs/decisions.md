# Decisions

## 2026-11-02 — Owner phone feedback

Answer context now exposes **Continent** and **Region** as separate English/French resources. Existing continent memberships and search aliases are unchanged. The new Region field is appended; existing deck/model/template/field identities remain intact.

The source remains a review candidate. Existing images, attribution, licenses and unaffected GUIDs remain intact. Where exercises are removed, their GUIDs are recorded separately and never reassigned. Updating an existing test collection does not delete retired cards; validation explicitly checks that limitation instead of claiming a clean replacement. Native app task visibility is tracked independently in [#655](https://github.com/simonpinkas/RectoVerso/issues/655).
