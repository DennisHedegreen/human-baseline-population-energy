"""Streamlit entry point for the simple population × kcal edition."""
import json
import pandas as pd
import streamlit as st
from simple_model import COUNTRIES, POPULATION_FILE, source_root, load_population, demographics, energy_result
from simple_locale import LANGUAGES, TEXT, COUNTRY_NAMES, number, compact

REPO_URL = "https://github.com/DennisHedegreen/human-baseline-population-energy"


@st.cache_data
def population():
    return load_population()


def main():
    st.set_page_config(page_title="Human Baseline", layout="wide")
    st.markdown("""<style>
    .stApp{background:#f7f7fa;color:#252530} h1{font-family:Georgia,serif;font-weight:400}
    div[data-testid=stMetric]{background:white;border:1px solid #dadce8;padding:16px}
    div[data-testid=stMetricValue]{font-family:Georgia,serif;font-size:1.75rem}
    .stMainBlockContainer{max-width:1500px} .intro{border-left:3px solid #19d55b;padding:12px 20px;margin-bottom:22px}
    @media(max-width:600px){h1{font-size:1.9rem!important;white-space:normal!important;overflow-wrap:anywhere}
    [data-testid=stMarkdownContainer] p{white-space:normal!important;overflow-wrap:anywhere}}
    </style>""", unsafe_allow_html=True)
    with st.sidebar:
        st.caption("HEDEGREEN RESEARCH · HUMAN BASELINE")
        locale = st.selectbox("Language / Sprog", list(LANGUAGES), format_func=lambda x: LANGUAGES[x])
        t = TEXT[locale]
        mode = st.radio(t["view"], ["explore", "compare", "eu", "custom", "about"], format_func=lambda x: t[x])
        st.caption("2025 · v0.3 · " + t["subtitle"])
        st.link_button(t["repo"], REPO_URL)
    st.title(t["title"] if mode != "about" else t["about"])
    if mode == "about":
        st.write(t["about_intro"])
        for key in ["method", "sources", "limits", "reuse"]:
            st.subheader(t[key])
            st.write(t["source_text" if key == "sources" else key + "_text"])
        st.markdown("[Eurostat · DEMO_PJAN](https://ec.europa.eu/eurostat/databrowser/view/demo_pjan/default/table)")
        st.markdown("[Eurostat · Copyright and reuse policy](https://ec.europa.eu/eurostat/help/copyright-notice)")
        for label, path, mime in [
            ("population_download", POPULATION_FILE, "text/csv"),
            ("metadata_download", "manifests/eurostat-demo_pjan-eu27-2025.json", "application/json"),
        ]:
            file = source_root() / path
            st.download_button(t[label], file.read_bytes(), file.name, mime=mime)
        return
    st.write(t["intro"])
    names = COUNTRIES if locale == "en" else dict(zip(COUNTRIES, COUNTRY_NAMES[locale]))
    codes = []
    frame = None
    with st.container(border=True):
        if mode == "explore":
            code = st.selectbox(t["country"], list(COUNTRIES), index=list(COUNTRIES).index("DK"), format_func=lambda c: names[c] + " · " + c)
            codes = [code]
        elif mode == "compare":
            codes = st.multiselect(t["countries"], list(COUNTRIES), default=["DK", "DE", "PL"], format_func=lambda c: names[c] + " · " + c)
        elif mode == "eu":
            codes = list(COUNTRIES)
            st.subheader(t["eu"])
        elif mode == "custom":
            left, right = st.columns(2)
            custom_name = left.text_input(t["name"], t["custom_name"])
            people = right.number_input(t["number"], min_value=0, value=1000000, step=1000, help=t["number_help"])
        kcal = st.number_input(t["kcal"], min_value=0.0, value=3000.0, step=100.0, help=t["kcal_help"], key="uniform_kcal")
    if mode != "custom":
        if not codes:
            st.info(t["select_note"])
            return
        data = population()
        frame = pd.DataFrame([demographics(data, c) for c in codes])
        people = int(frame.people.sum())
        custom_name = names[codes[0]] if len(codes) == 1 else "EU27" if mode == "eu" else t["compare"]
    result = energy_result(people, kcal, custom_name or t["custom_name"], codes)
    for column, key, field in zip(st.columns(3), ["day", "month", "year"], ["kcal_day", "kcal_average_month", "kcal_year"]):
        exact = number(result[field], locale, 2)
        column.metric(t[key], compact(result[field], locale), help=t[key + "_help"] + "\n\n" + exact + " kcal")
    st.caption(t["assumption"])
    with st.expander(t["exact"]):
        st.write(f"{number(people, locale)} × {number(kcal, locale, 2)} = {number(result['kcal_day'], locale, 2)} kcal")
        st.write(t["month_help"])
        st.write(t["year_help"])
        st.json(result)
    st.download_button(t["download"], json.dumps(result, indent=2, ensure_ascii=False), "human-baseline-energy-scenario.json", mime="application/json")
    if frame is not None:
        st.subheader(t["population_heading"])
        st.write(t["population_note"])
        counts = {key: int(frame[field].sum()) for key, field in [("people", "people"), ("children", "children"), ("adults", "adults"), ("older", "older")]}
        for col, (key, value) in zip(st.columns(4), counts.items()):
            col.metric(t[key], number(value, locale), help=t["people_help"] if key == "people" else t["age_help"])
        if len(codes) == 1:
            for col, key in zip(st.columns(2), ["female", "male"]):
                col.metric(t[key], number(int(frame[key].sum()), locale), help=t["sex_help"])
        if int(frame.unknown.sum()):
            st.metric(t["unknown"], number(int(frame.unknown.sum()), locale), help=t["age_help"])
        if len(codes) > 1:
            st.write(t["table_help"])
            comparison = pd.DataFrame({t["country"]: [names[c] for c in codes], t["people"]: frame.people,
                                       t["day"]: frame.people * kcal})
            st.dataframe(comparison, hide_index=True, width="stretch", column_config={
                t["country"]: st.column_config.TextColumn(help=t["table_help"]),
                t["people"]: st.column_config.NumberColumn(help=t["people_help"], format="localized"),
                t["day"]: st.column_config.NumberColumn(help=t["day_help"], format="localized"),
            })
            st.bar_chart(comparison.set_index(t["country"])[t["day"]], color="#19d55b", horizontal=True)


if __name__ == "__main__":
    main()
