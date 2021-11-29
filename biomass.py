import glob
import os
from pathlib import Path

import click
import pandas as pd

from constants import Fields, BMI_HR


@click.command()
@click.argument("path", type=click.Path(exists=True), required=True)
@click.argument("category", type=str, default="Overweight")
def calculate_biomass(path: str, category: str):
    """
    main function to return the number overweight people giving a list of gender, heights and weights
    :param path: path with the json directory
    :param category: str with the name of the index to search against
    """

    data_df = load_data(path=path)

    if data_df.empty:
        click.echo("couldn't find loadable data.")

    data_df = convert_cm_m(data_df, Fields.HEIGHT_CM)
    data_df = biomass(data_df, Fields.HEIGHT_M, Fields.WEIGHT, Fields.BIOMASS)

    bmi_index = data_df[Fields.BIOMASS].between(BMI_HR[category][0], BMI_HR[category][1])

    click.echo(f"Found {bmi_index.sum()} {category} people.")

    return bmi_index.sum()


def convert_cm_m(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    creating one function to explore the tests it's too simple
    :param df: pd.DataFrame loaded data
    :param col: str column to apply the conversion
    :return: pd.DataFrame
    """

    df[Fields.HEIGHT_M] = df[col] / 100

    return df


def biomass(df: pd.DataFrame, height: str, weight: str, destination: str) -> pd.DataFrame:
    """
    calculate the biomass index
    :param df: pd.DataFrame loaded data
    :param height: str column used in height
    :param weight: str column used in weight
    :param destination: str destination column to be used for the index
    :return: pd.DataFrame
    """

    # this saves some memory space instead calculating the square of height and vectoring calculation still in place
    df[destination] = df[weight] / (df[height] * df[height])

    return df


def load_data(path: str) -> pd.DataFrame:
    """
    loads all json files for the giver path and return a singe DataFrame
    for the sake of this test I'm assuming that all json files have the same schema
    :param path: str path for the json files
    :return: pd.DataFrame
    """
    df = pd.DataFrame()
    path = Path(path).absolute()

    for f in glob.glob(os.path.join(path, "*.json")):
        try:
            tmp_df = pd.read_json(f)
            df = df.append(tmp_df, ignore_index=True)
        except Exception as e:
            print(e)

    return df


if __name__ == '__main__':
    calculate_biomass()
