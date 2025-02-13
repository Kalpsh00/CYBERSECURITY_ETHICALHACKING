# CYBERSECURITY_ETHICALHACKING

**COMPANY** : CODTECH IT SOLUTIONS

**NAME** : KALE KALPESH JAGDISHPRASAD

**INTERN ID** : CT12JCL

**DOMAIN** : CYBER SECURITY AND ETHICAL HACKING

**BATCH DURATION** : JAN 5 2024 to MARCH 5 2024

**MENTOR NAME** : NEELA SANTHOSH

# TASK DESCRIPTION OF TASK1

 File integrity checking and monitoring are essential practices in ensuring the security and reliability of files within a system. By using the hashlib module in Python, you can create a robust solution to monitor file changes effectively.

 Purpose of File Integrity Checking:

File integrity checking involves verifying that a file's content remains unchanged. This is crucial in various scenarios, such as:
 Ensuring that software distributions are not tampered with.
 Verifying backups to ensure they are intact.
 Monitoring sensitive files for unauthorized modifications.

# Explanation of my python script for file integrity checker and monitoring.

- First libraries of python like os, time and hashlib is used.
- Then calculate hash_function process start of a particular file where 

 calculate_hash(file_path): # Calculates the SHA-256 hash of a file.
 hasher = hashlib.sha256(): # Initializes the SHA-256 hash object.
 with open(file_path, 'rb') as f: # Opens the file in binary read mode.
 buf = f.read(): # Reads the file content.
 hasher.update(buf): # Updates the hash with the file content.
 return hasher.hexdigest(): # Returns the hash as a hexadecimal string

- Monitoring the files are main part so here also function is used.
- In this function file will be monitored continuously calculating , storing and printing hash value of a file. 
- As some one changes the specified file then it will show New hash and again that script will run in infinite loop (i.e no changes detected).
- If and else statements are used to check if new hash value is different and if it is changed for a file then prints a new hash value else it will show no change detected.

At the end function call of monitor_file is done to monitor files

# OUTPUT of TASK1

![Image](https://github.com/user-attachments/assets/a7bb429f-8181-4f56-b706-e7029cdb364d)





# Task Description of TASK 2

WEB APPLICATION VULNERABILITY SCANNER

# SQL Injection (SQLi):

SQL Injection is a type of attack that allows an attacker to interfere with the queries that an application makes to its database. This vulnerability occurs when an application includes untrusted data in a SQL query without proper validation or sanitization. Attackers can manipulate SQL queries by injecting malicious SQL code into input fields, such as login forms or search boxes.

# Example Script Explanation:

The SQLi script provided earlier demonstrates a basic testing tool that sends a series of predefined SQL injection payloads to a specified URL. The script constructs URLs with these payloads and sends GET requests to the target application. It checks the responses for common indicators of SQL injection vulnerabilities, such as error messages or database-related keywords.

Payloads: 

The script includes a list of common SQL injection payloads designed to manipulate SQL queries. These payloads can bypass authentication, extract sensitive data, or even modify the database.
Testing Function: The test_sql_injection function iterates over the payloads, constructs URLs with the payloads, and sends requests to the target application. It analyzes the responses to identify potential vulnerabilities.
Response Analysis: If the response contains error messages or database-related terms, the script flags the URL as potentially vulnerable to SQL injection.
SQL injection can lead to severe consequences, including unauthorized access to sensitive data, data manipulation, and even complete database compromise. Organizations must implement proper input validation, parameterized queries, and prepared statements to mitigate SQL injection risks. 
# HERE the Target website is testphp.webvuln.com.

# Cross-Site Scripting (XSS)

Cross-Site Scripting is a vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users. XSS attacks occur when an application includes untrusted data in a web page without proper encoding or escaping. This can lead to various malicious activities, such as session hijacking, defacement, or redirecting users to malicious sites.

Example Script Explanation
The XSS script provided demonstrates a basic testing tool that checks for potential XSS vulnerabilities by injecting a simple JavaScript payload into a URL parameter.

Payload: 
- The script uses a basic JavaScript payload (<script>alert('XSS')</script>) designed to trigger an alert box when executed in a browser. This payload is a common test for XSS vulnerabilities.
Testing Function: The find_xss_vulnerabilities function replaces a placeholder in the URL with the XSS payload and sends a GET request to the target application.
Response Analysis: If the response contains the injected payload, the script flags the URL as potentially vulnerable to XSS. This indicates that the application is reflecting the untrusted input back to the user without proper sanitization.
# HERE the Target website is beyondordinary.in.

# Output of TASK 2


![Image](https://github.com/user-attachments/assets/796b453a-daa8-430f-8a5b-abb0909d8519)

![Image](https://github.com/user-attachments/assets/a58311c5-946d-418f-abfe-5cccc526e2fe)


# TASK DESCRIPTION OF TASK 3


# Project Structure
First, create a project directory called pen_test_toolkit. Inside this directory, create a modules folder containing Python scripts for each module, and ensure there's an __init__.py file to mark it as a package. Also, create a main.py script and a README.md file in the root directory.

Port Scanner Module: 

Create a file named port_scanner.py within the modules directory. This module will use Python’s socket library to scan specified ports on a given target. The function scan_ports takes a target and a list of ports, attempts to connect to each port, and returns a list of open ports.

Brute Forcer Module

Next, create brute_forcer.py within the modules directory. This module includes a function validate_http_basic_auth that attempts HTTP Basic Authentication using the requests library. It tries various username-password combinations against a target URL. The function brute_force iterates through a list of passwords, using the validation function to check each one.

# Main Script

The main.py script ties everything together. Use the argparse library to parse command-line arguments for each module. The script should handle port scanning, brute forcing, and HTTP server scanning based on the provided arguments.

To ensure the script finds the modules directory, adjust the Python path using sys.path.insert. This line of code makes sure the interpreter is aware of the modules directory.

# Running the Toolkit

Port Scanning:
- python main.py --scan example.com 80 443 22

Brute Forcing: 
- python main.py --brute example.com username password123 admin123 secretpassword test

![Screenshot 2025-02-13 143639](https://github.com/user-attachments/assets/91e73c62-d77a-489f-8019-760967c3eb52)


