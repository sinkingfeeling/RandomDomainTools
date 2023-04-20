"""
This code generates a list of subdomains for a specified domain and validates them in parallel using multiprocessing. It writes valid subdomains to an output file and displays a progress bar using the tqdm library.
"""

import os
import socket
from tqdm import tqdm
from multiprocessing import Pool

# specify the domain
domain = "whiskergalaxy.com"

# specify the output file path
output_file = "output.txt"

# define a function to validate a single subdomain
def validate_subdomain(subdomain):
    try:
        socket.gethostbyname(subdomain)
        print(f"{subdomain}: valid")
        return subdomain
    except socket.error:
        print(f"{subdomain}: invalid")
        return None

if __name__ == "__main__":
    # generate a list of subdomains to validate
    subdomains = [f"uk-{num}.{domain}" for num in range(1, 101)]

    # validate the subdomains in parallel
    with Pool() as pool, open(output_file, "w") as f, tqdm(total=100, desc="Generating subdomains") as pbar:
        for subdomain in pool.imap_unordered(validate_subdomain, subdomains):
            if subdomain:
                f.write(subdomain + os.linesep)
            pbar.update(1)
