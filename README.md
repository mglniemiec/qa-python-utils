# QA Python Utils

Collection of Python scripts useful for testing.

## 📋 Table of Contents

- [compare_json.py](#compare_jsonpy)
- [check_status_code.py](#check_status_codepy)

# check_status_code.py

A simple Python script to check if a given URL returns the expected HTTP status code — useful for quickly validating API health or availability during testing.

## Features

- Sends a GET request to the specified URL
- Verifies if the status code matches the expected one
- CLI-based for fast testing
- Custom timeout and expected code support
- Built with requests

## Requirements

- Python 3
- requests package

Install requirements using pip:

python3 -m pip install -r requirements.txt


# compare_json.py

A simple Python script to compare two JSON files and highlight differences — useful for QA testing, debugging API responses, and validating data structures.

---

## Features

- Compares nested JSON files
- Ignores order of elements (e.g., in lists)
- Highlights only the differences
- Easy command-line usage
- Built with [`deepdiff`](https://github.com/seperman/deepdiff)

---

## Requirements

- Python 3
- `deepdiff` package

Install requirements using pip:

```bash
python3 -m pip install -r requirements.txt

