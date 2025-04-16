import json
import sys
from deepdiff import DeepDiff

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def compare_json_files(file1, file2):
    data1 = load_json(file1)
    data2 = load_json(file2)

    diff = DeepDiff(data1, data2, ignore_order=True)
    if not diff:
        print("✅ JSON files are identical.")
    else:
        print("❌ Differences found:")
        print(diff)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_json.py file1.json file2.json")
        sys.exit(1)

    compare_json_files(sys.argv[1], sys.argv[2])



