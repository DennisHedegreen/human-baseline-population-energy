"""Model boundaries, locale parity and all twenty simple-edition views."""
import math
from pathlib import Path
from streamlit.testing.v1 import AppTest
from simple_model import COUNTRIES, load_population, demographics, energy_result
from simple_locale import TEXT, COUNTRY_NAMES


def main():
    data = load_population()
    totals = [demographics(data, c)["people"] for c in COUNTRIES]
    assert len(totals) == 27 and demographics(data, "DK")["people"] == 5992734
    for kcal in [0, 2500, 3000, 5500]:
        total = energy_result(sum(totals), kcal, "EU27", COUNTRIES)
        assert total["kcal_day"] == sum(energy_result(n, kcal)["kcal_day"] for n in totals)
        assert total["kcal_year"] == total["kcal_day"] * 365
        assert total["kcal_average_month"] == total["kcal_year"] / 12
    assert energy_result(0, 3000)["kcal_per_person_day"] is None
    for people, kcal in [(-1, 3000), (True, 3000), (1, -1), (1, math.nan), (1, math.inf)]:
        try:
            energy_result(people, kcal)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid input accepted")
    source = Path(__file__).with_name("app_simple.py")
    if not source.exists():
        source = source.with_name("app.py")
    app = AppTest.from_file(str(source), default_timeout=60).run()
    assert not app.exception
    assert app.sidebar.selectbox[0].value == "en"
    for locale, t in TEXT.items():
        assert set(t) == set(TEXT["en"])
        if locale != "en":
            assert len(COUNTRY_NAMES[locale]) == 27
        app.sidebar.selectbox[0].set_value(locale).run()
        for view in ["explore", "compare", "eu", "custom", "about"]:
            app.radio[0].set_value(view).run()
            assert not app.exception, app.exception
            assert len(app.sidebar.selectbox) == 1 and not app.sidebar.number_input
            if view == "about":
                assert len(app.get("download_button")) == 2
            else:
                assert app.metric[0].label == t["day"]
                assert all(m.proto.help for m in app.metric)
                next(n for n in app.number_input if n.label == t["kcal"]).set_value(4000.0).run()
                assert not app.exception
                if view == "custom":
                    next(n for n in app.number_input if n.label == t["number"]).set_value(0).run()
                    assert app.metric[0].value == "0"
                    next(n for n in app.number_input if n.label == t["number"]).set_value(100).run()
                    assert app.metric[0].value == "400 000"
        print(locale, "five views passed", flush=True)
    print("Simple edition passed: 27 countries, arithmetic/missing/invalid boundaries, four locales × five views; no reference datasets required.")


if __name__ == "__main__":
    main()
