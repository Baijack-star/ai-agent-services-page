import os
import requests
from bs4 import BeautifulSoup

def check_links(directory):
    broken_links = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                print(f"Checking file: {filepath}")
                with open(filepath, "r") as f:
                    soup = BeautifulSoup(f, "html.parser")
                    for a in soup.find_all("a"):
                        href = a.get("href")
                        if href:
                            print(f"  Checking link: {href}")
                            if href.startswith("http") or href.startswith("https"):
                                try:
                                    response = requests.get(href)
                                    if response.status_code >= 400:
                                        broken_links.append((filepath, href))
                                except requests.exceptions.RequestException:
                                    broken_links.append((filepath, href))
                            elif not href.startswith("#") and not href.startswith("mailto:") and not href.startswith("tel:"):
                                linked_file = os.path.normpath(os.path.join(root, href))
                                if not os.path.exists(linked_file):
                                    broken_links.append((filepath, href))
    return broken_links

if __name__ == "__main__":
    broken_links = check_links(".")
    if broken_links:
        print("\nBroken links found:")
        for link in broken_links:
            print(f"  File: {link[0]}, Link: {link[1]}")
    else:
        print("\nNo broken links found.")
