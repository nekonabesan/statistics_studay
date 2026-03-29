# OECD SDMX Metadata Download Summary

## Saved Files
- dataflow: `metadata/dataflow.xml` (8,361,777 bytes)
- datastructure: `metadata/datastructure.xml` (4,666,381 bytes)
- codelist: `metadata/codelist.xml` (72,093,799 bytes)
- conceptscheme: `metadata/conceptscheme.xml` (1,877,835 bytes)
- contentconstraint: `metadata/contentconstraint.xml` (26,689,269 bytes)

## Counts
- Dataflows: 1,479
- Data structures: 398
- Codelists: 792
- Concept schemes: 257
- Content constraints: 2,767

## Focus Dataflows (Productivity DB)
- DSD_PDB@DF_PDB_LV: Productivity levels (DSD ref: ?)
- DSD_PDB@DF_PDB_ULC_Q: Productivity and unit labour costs (DSD ref: ?)

## Request Parameter Structure (from DSD)
SDMX data endpoint template:
`/public/rest/data/{flow_ref}/{key}?startPeriod=...&endPeriod=...`

### DSD_PDB dimensions (key order)
- 1. REF_AREA (codelist: )
- 2. FREQ (codelist: )
- 3. MEASURE (codelist: )
- 4. ACTIVITY (codelist: )
- 5. UNIT_MEASURE (codelist: )
- 6. PRICE_BASE (codelist: )
- 7. TRANSFORMATION (codelist: )
- 8. ASSET_CODE (codelist: )
- 9. CONVERSION_TYPE (codelist: )

Attributes:
- OBS_STATUS (assignmentStatus=Mandatory, codelist=)
- UNIT_MULT (assignmentStatus=Conditional, codelist=)
- BASE_PER (assignmentStatus=Conditional, codelist=)
- DECIMALS (assignmentStatus=Conditional, codelist=)
