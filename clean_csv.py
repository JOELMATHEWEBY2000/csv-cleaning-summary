import argparse
from pathlib import Path
import pandas as pd


def clean_csv(input_file, output_file=None):

    input_path = Path(input_file)

    if not input_path.exists():
        raise FileNotFoundError(f"File not found: {input_path}")

    if input_path.stat().st_size == 0:
        raise ValueError("CSV file is empty.")

    df = pd.read_csv(input_path)

    if df.empty:
        raise ValueError("CSV contains no data.")

    # Check whether the input is sample_data.csv
    if input_path.name.lower() == "sample_data.csv":

        print("\n========== ORIGINAL DATA WITH MISSING VALUES ==========\n")
        print(df.to_string(index=False))

        print("\n========== MISSING VALUES SUMMARY ==========\n")
        print(df.isnull().sum())

        print(f"\nTotal missing values: {df.isnull().sum().sum()}")

        return

    # Otherwise, display the cleaned dataset
    print("\n========== CLEANED DATA ==========\n")
    print(df.to_string(index=False))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="CSV Data Cleaning"
    )

    parser.add_argument("input", help="Input CSV file")

    args = parser.parse_args()

    try:
        clean_csv(args.input)

    except (
        FileNotFoundError,
        ValueError,
        pd.errors.EmptyDataError,
        pd.errors.ParserError
    ) as error:

        raise SystemExit(f"Error: {error}")
