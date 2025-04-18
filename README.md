# QA Python Utils

Collection of Python scripts useful for testing.

## 📋 Table of Contents

- [check_status_code.py](#check_status_codepy)
- [compare_json.py](#compare_jsonpy)
- [random_data_generator.py](#radom_data_generatorpy)
- [requirements](#requirements)

# check_status_code.py

A simple Python script to check if a given URL returns the expected HTTP status code — useful for quickly validating API health or availability during testing.

## Features

- Sends a GET request to the specified URL
- Verifies if the status code matches the expected one
- CLI-based for fast testing
- Custom timeout and expected code support
- Built with requests


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

# random_data_generator.py

A simple Python script to generate fake user or company data — useful for testing forms, mock APIs, or any QA scenario that needs realistic data.

---

## Features

- Geerates fake user or company data
- Supports multiple locales (e.g., `en_US`, `de_AT`, `en_GB`)
- Console output only — no files
- Easy command-line usage
- Built with [`Faker`](https://faker.readthedocs.io/)

---

## Usage
python3 random_data_generator.py [count] [locale] [mode]
- `count` *(optional)* – number of entries to generate (default: `10`)  
- `locale` *(optional)* – Faker locale code (default: `en_US`)  
- `mode` *(optional)* – `user` or `company` (default: `user`)

# Requirements

- Python 3
- faker package - for random_data_generator.py
- deepdif  package - for compare_json.py
- requests package - for check_status_code.py



Install requirements using pip:

```bash
python3 -m pip install -r requirements.txt
