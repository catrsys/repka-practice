import os
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup as bs


def download_static_files(url: str, dst: Path, extensions: list[str] = None) -> None:
    session = requests.Session()
    session.headers[
        "User-Agent"
    ] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    response = session.get(url)
    response.raise_for_status()
    html = response.content

    soup = bs(html, "html.parser")

    files_to_download = list()

    # get the file links
    for file in soup.find_all("script", src=True):
        file_url = urljoin(url, file["src"])
        try:
            file_url = file_url[: file_url.index("?")]
        except ValueError:
            pass
        files_to_download.append(file_url)

    for file in soup.find_all("link", href=True, rel="stylesheet"):
        file_url = urljoin(url, file["href"])
        try:
            file_url = file_url[: file_url.index("?")]
        except ValueError:
            pass
        files_to_download.append(file_url)

    if not os.path.exists(dst):
        os.makedirs(dst)

    # downloading files
    for filename in files_to_download:
        if extensions:
            file_ext = filename.split(".")[-1].lower()
            if not file_ext in extensions:
                continue

        file = requests.get(filename)
        with open(dst / filename.split("/")[-1], "wb") as result:
            result.write(file.content)
