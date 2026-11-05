# Coverage and editorial convention

This source candidate contains **488 cards per language** from a 249-entry ISO reference. The 39 regional additions belong only to Maps.

## Included exercises

| Exercise | Cards per language |
|---|---:|
| place-capital | 244 |
| capital-place | 244 |

## Explicit omissions and holds

Where no verified applicable capital or seat exists, no capital exercise is invented. The table below accounts for every omitted or held reference entry.

| Place | Kind | Reason |
|---|---|---|
| Antarctica (`ATA`) | capital | No national capital. |
| French Southern Territories (`ATF`) | capital | Administration is outside this territory; bases are not a capital. |
| Bonaire, Sint Eustatius and Saba (`BES`) | capital | Three separate public bodies; no single capital for this ISO aggregate. |
| Bouvet Island (`BVT`) | capital | Uninhabited; administered from outside the territory. |
| Western Sahara (`ESH`) | capital | Held: competing claimed capital and administrative centres need a reviewed status-qualified record. |
| Gibraltar (`GIB`) | capital | PCGN 2026 explicitly identifies no separate capital or administrative centre. |
| Hong Kong (`HKG`) | capital | No separate capital for the city territory. |
| Heard Island and McDonald Islands (`HMD`) | capital | Uninhabited; administered from outside the territory. |
| British Indian Ocean Territory (`IOT`) | capital | No permanent civilian capital. |
| Macau (`MAC`) | capital | No separate capital for the city territory. |
| South Georgia and the South Sandwich Islands (`SGS`) | capital | No capital; scientific stations are not capitals. |
| Svalbard and Jan Mayen (`SJM`) | capital | Statistical aggregate; Longyearbyen serves Svalbard, not Jan Mayen. |
| Tokelau (`TKL`) | capital | No single capital; administration rotates among atolls. |
| United States Minor Outlying Islands (`UMI`) | capital | Statistical aggregate; no single capital. |

## Geographic search

Seven explicit geographic groups: Africa, Antarctica, Asia, Europe, North America, South America and Oceania. Multiple memberships describe the place itself. Remote territories are located geographically, not assigned their sovereign parent’s continent. The full boundary convention and rationales are in [continents.json](../source/continents.json). The owner approved the named Antarctic-island discovery convention below on 2 November 2026; Antarctic-program management is not proof of continental membership.

## Names and capitals

Common English/French learner names are inherited from the reviewed Maps roster. Capitals are single, role-qualified records: South Africa, Bolivia, Netherlands, Malaysia, Eswatini, Benin, Palestine and Yemen have separate questions for each included role. Bern is the federal city; Yaren is a government district, not an official capital. Commercial centres are not added merely because they are sometimes called an “economic capital”.

Ciudad de la Paz replaces Malabo under the 2 January 2026 decree. Brades replaces the destroyed Plymouth under Montserrat Cabinet Decision 534/2025, recorded in PCGN’s March 2026 guide. Jakarta remains the legal capital pending the transfer decree. Jerusalem questions distinguish the declared/claimed role and the unresolved final status. A capital question does not alter the map boundary convention.

## Sources and freshness

Capital names began with Ultimate Geography 5.3 public-domain text and were checked against IGN’s country table and the French foreign ministry’s June 2026 world map, with primary corrections and territory/role references on each record. The IGN workbook is a dated reference, not a live freshness guarantee. [Places](../source/places.json) includes each capital’s URLs. The candidate still needs final editorial and native visual review before publication.

## Whole-place membership audit

Continent metadata in this deck describes the whole ISO reference place. Separately coded territories are represented independently. Non-separately-coded islands remain part of that place even when the 39 additional regional quiz questions are Maps-only.

| Place | Membership | Reason |
|---|---|---|
| France | Europe + North America | Metropolitan France plus Clipperton; separately ISO-coded overseas places remain independent. |
| Portugal | Europe | Mainland, the Azores and Madeira. UN M49, GeoNames and the CIA World Factbook classify Portugal in Europe, and no source assigns Madeira to Africa: the owner moved Madeira to Europe on 5 November 2026, as in Maps. |
| Spain | Europe + Africa | Ceuta, Melilla and the plazas de soberanía on the North African coast. The Canary Islands go with Europe, as the sources classify Spain and none assigns them to Africa: the owner's decision on 5 November 2026, as for Madeira. |
| Colombia | South America + North America | Includes San Andrés/Providencia in the Caribbean. |
| Venezuela | South America + North America | Includes the remote Caribbean Isla de Aves. |

These memberships are not copied from Maps’ deliberately core-only France/Portugal questions. The private combined deck’s map artwork keeps the approved core/overview geometry; its continent metadata describes the named whole place rather than claiming every island is shown in that image. No new regional quiz card or boundary geometry is added.

Primary references and the distinction between geographic groups and the separate primary Region field are recorded in [continents.json](../source/continents.json). The owner approved the BVT/HMD/SGS/ATF Antarctic-group assignments documented below: the independent GeoNames register supports this discovery grouping, which must not be generalized from agency or administrative coverage to all subantarctic islands. Australia, New Zealand, South Africa and Saint Helena are not relabeled Antarctica.

## Approved Antarctic-island convention

This is a named discovery-classification choice, not uncertainty about where the islands are. [GeoNames’ continent register](https://download.geonames.org/export/dump/countryInfo.txt) groups the four entries below with Antarctica; [UN M49’s statistical geography](https://unstats.un.org/unsd/methodology/m49/) groups them differently.

| Entry | Approved search groups | UN M49 comparison |
|---|---|---|
| Bouvet Island | Antarctica | South America |
| Heard Island and McDonald Islands | Antarctica | Oceania |
| South Georgia and South Sandwich Islands | Antarctica | South America |
| French Southern Territories | Africa + Antarctica | Eastern Africa |

Owner decision, 2 November 2026: retain the explicitly named GeoNames Antarctic group while preserving ATF’s African Scattered Islands separately. Its Kerguelen and Crozet groups use AN; Amsterdam/Saint-Paul, Glorioso, Juan de Nova, Europa, Bassas da India and Tromelin use AF. Owner decision, 5 November 2026, following Maps: Amsterdam and Saint Paul are Africa, as UN M49 classifies ATF, not Antarctica; this replaces the 2 November call for those two islands, which lie north of the Antarctic Convergence although IPEV counts them among France’s subantarctic islands. There is no automatic Antarctica membership for Australia, New Zealand, South Africa or Saint Helena merely because an Antarctic program operates on an island. This wording does not say the named islands are on the Antarctic continental landmass.

The owner approved these existing candidate assignments, so this decision changes no package content, card count, artwork or boundary. The exact decision and source comparison remain under `taxonomyReview` in the continent JSON. This geographic classification is settled; publication gates are tracked separately.

## Owner feedback and context labels

Answer context exposes **Continent** and **Region** as separately named fields in English and French. Region preserves the existing source classification; it is not relabeled as a continent or subcontinent. Multiple continent memberships and bilingual search aliases are unchanged. The old **Details** field keeps only the remaining optional note, if any.
