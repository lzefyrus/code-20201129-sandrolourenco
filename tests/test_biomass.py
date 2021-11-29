import pandas as pd
from click.testing import CliRunner
import biomass
from constants import Fields

def test_load_file():
    df = biomass.load_data("../docs")
    assert len(df) == 6

def test_conversion():
    df = pd.DataFrame({'cm': [180]})
    df = biomass.convert_cm_m(df, "cm")

    assert float(df[Fields.HEIGHT_M]) == 1.8

def test_biomass_calculation():
    df = pd.DataFrame({'m': [1.8], 'kg': 100})
    df = biomass.biomass(df, 'm', 'kg', 'bm')

    assert float(df['bm']) == 30.864197530864196

def test_bmi_index():
    result = CliRunner().invoke(biomass.calculate_biomass, ("../docs"))
    assert not result.exception
    assert result.stdout == 'Found 1 Overweight people.\n'