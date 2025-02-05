# CYBERSECURITY_ETHICALHACKING

**COMPANY** : CODTECH IT SOLUTIONS

**NAME** : KALE KALPESH JAGDISHPRASAD

**INTERN ID** : CT12JCL

**DOMAIN** : CYBER SECURITY AND ETHICAL HACKING

**BATCH DURATION** : JAN 5 2024 to MARCH 5 2024

**MENTOR NAME** : NEELA SANTHOSH

# TASK DESCRIPTION OF TASK1

# File integrity checking and monitoring are essential practices in ensuring the security and reliability of files within a system. By using the hashlib module in Python, you can create a robust solution to monitor file changes effectively.

# Purpose of File Integrity Checking:

# File integrity checking involves verifying that a file's content remains unchanged. This is crucial in various scenarios, such as:
# Ensuring that software distributions are not tampered with.
# Verifying backups to ensure they are intact.
# Monitoring sensitive files for unauthorized modifications.

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
