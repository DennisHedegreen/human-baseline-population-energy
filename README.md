# Human Baseline: Population and Energy

The simple edition, v0.3.0. Choose an EU27 country, compare countries, select
EU27, or enter a custom headcount. Choose one kcal/person/day figure, applied
equally to everyone, including infants. The output is total kcal/day,
average month and year. English is default; Danish, Spanish and German are included.

This is an energy-volume scenario, not a nutrition recommendation, measured
individual requirement or demonstrated food-production/delivery system. Any
energy margin is included in the chosen figure; nothing else is added silently.
The initial 3,000 is an editable arithmetic example, not an official reference.

## Run and verify

Use Python 3.12:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m streamlit run app.py
.venv/bin/python check_simple.py
.venv/bin/python verify_release.py
```

Daily = people × chosen kcal. Annual = daily × 365. Average month = annual ÷ 12.
Demographics describe the official population but do not modify these formulas.
Custom headcount has no invented demographics. Zero people yields zero energy.

## Data and source responsibility

Source: Eurostat DEMO_PJAN, population on 1 January 2025 by age and reported sex,
captured 5 October 2026. Original response, processed counts and metadata are
included, with hashes in the release manifest. The app reads this fixed capture
instead of fetching live population on each visit.

Source links and reuse basis are in SOURCE-NOTICES.md. Selection, formatting,
translations and scenario calculations are our own. Eurostat is not responsible
for this app or its calculations. No institutional endorsement is implied.

NNR, WHO infant weights and maternal reference datasets are not shipped in this
edition. Earlier detailed local models and release candidates are preserved in
the research workspace, not published through this repository's history.

## Hosting

Streamlit Community Cloud: repository `DennisHedegreen/human-baseline-population-energy`,
branch `main`, entrypoint `app.py`, Python 3.12, no secrets required. Record the
actual assigned URL after deployment; no subdomain is promised in advance.

Source-code availability is not a blanket open-source licence. No new project
code licence has been assigned; source-data reuse follows its separate notice.
Later foods, nutrients, prices and cost allocation will be a separate project,
not a silent expansion of this simple edition.
