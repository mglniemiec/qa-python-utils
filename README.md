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

