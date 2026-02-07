import os
from bs4 import BeautifulSoup

def fix_links(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                print(f"Processing file: {filepath}")
                with open(filepath, "r+", encoding="utf-8") as f:
                    content = f.read()
                    soup = BeautifulSoup(content, "html.parser")
                    links_fixed = False
                    for a in soup.find_all("a"):
                        href = a.get("href")
                        if href and href.startswith("/ai-agent-services-page/"):
                            new_href = href.replace("/ai-agent-services-page/", "/")
                            a["href"] = new_href
                            links_fixed = True
                            print(f"  Fixed link: {href} -> {new_href}")

                    # Fix for links like ../pricing.html
                    for a in soup.find_all("a"):
                        href = a.get("href")
                        if href and "../" in href:
                            # Attempt to resolve the path relative to the root
                            # This is a simplification and might not cover all cases
                            new_href = os.path.normpath(os.path.join(os.path.dirname(filepath), href))
                            # We want to make it relative to the root of the project
                            new_href = os.path.relpath(new_href, start=directory)
                            # bring back the forward slashes
                            new_href = new_href.replace(os.sep, "/")
                            a["href"] = "/" + new_href
                            links_fixed = True
                            print(f"  Fixed relative link: {href} -> {a['href']}")


                    if links_fixed:
                        f.seek(0)
                        f.write(str(soup))
                        f.truncate()

if __name__ == "__main__":
    fix_links(".")
