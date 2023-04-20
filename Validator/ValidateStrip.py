"""
This script performs a DNS lookup on a list of domains provided in a file specified by the variable filename. It reads the list of domains from the file and strips any whitespace characters. It then uses the socket.gethostbyname() function to get the IP address of each domain in the list. If a domain's IP address cannot be obtained due to a socket.gaierror exception, the script adds an error message to the results dictionary.

Finally, the script writes the list of valid domains (i.e., domains for which an IP address was successfully obtained) to a file named valid.txt. If there are valid domains, the script writes each domain to a new line in the valid.txt file. If there are no valid domains, the script writes the message "No valid domains found" to the valid.txt file.
"""


import socket

def nslookup(filename):
    with open(filename, 'r') as f:
        domains = f.readlines()
    domains = [domain.strip() for domain in domains]
    results = {}
    for domain in domains:
        try:
            results[domain] = socket.gethostbyname(domain)
        except socket.gaierror as e:
            results[domain] = str(e)
    
    with open('valid.txt', 'w') as f:
        valid_domains = [domain for domain, ip in results.items() if not isinstance(ip, str) and '[Errno 11001] getaddrinfo failed' not in ip]
        if valid_domains:
            for domain in valid_domains:
                f.write(f"{domain}\n")
        else:
            f.write("No valid domains found\n")

filename = r"C:\Users\jorda\OneDrive\Documents\domains.txt"
nslookup(filename)
