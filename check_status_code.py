import sys
import requests

def check_status(url, expected_code=200, timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        actual_code = response.status_code

        if actual_code == expected_code:
            print(f"Success: {url} returned {actual_code} (as expected)")
        else:
            print(f"Error: {url} returned {actual_code} (expected {expected_code})")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 check_status_code.py <URL> [expected_status_code]")
        sys.exit(1)

    url = sys.argv[1]
    expected_code = int(sys.argv[2]) if len(sys.argv) >= 3 else 200

    check_status(url, expected_code=expected_code)
