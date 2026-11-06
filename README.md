"# csv-cleaning-summary" 

# CSV Cleaning and Summary using Python

## Project Overview
A beginner-friendly Python project that reads CSV datasets, identifies missing values, cleans incomplete data, and saves the cleaned dataset using Pandas.

## Technologies Used
- Python
- Pandas
- CSV
- Git and GitHub

## Features
- Read CSV datasets
- Identify missing values
- Display missing-value summary
- Handle missing numeric values using median
- Handle missing categorical values using mode
- Generate cleaned CSV files

## Project Structure
```text
csv-cleaning-summary/
├── clean_csv.py
├── sample_data.csv
├── cleaned_data.csv
├── README.md
└── screenshots/
    └── terminal-output.png
```

## How to Run

Install Pandas:

```bash
pip install pandas
```

Display original data and missing values:

```bash
python clean_csv.py sample_data.csv
```

Display cleaned data:

```bash
python clean_csv.py cleaned_data.csv
```

## Terminal Output

![Terminal Output](screenshots/terminal-output.png)

## Author
Joel Mathew Eby

Python Full Stack Developer