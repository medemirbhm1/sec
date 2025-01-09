import os
import requests
import zipfile

def download_file(url, output_path):
    """Download a file from a URL and save it to the specified path."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Downloaded: {output_path}")
    else:
        print(f"Failed to download {url}. HTTP Status: {response.status_code}")

def extract_zip(zip_path, extract_to):
    """Extract a ZIP file to the specified directory."""
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted: {zip_path} to {extract_to}")

def main():
    # URLs of the bulk data ZIP files
    urls = {
        "companyfacts": "https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip",
        "submissions": "https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip"
    }

    # Directory to save the downloaded files
    download_dir = "downloads"
    extracted_dir = "extracted"

    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Download and extract each file
    for name, url in urls.items():
        zip_path = os.path.join(download_dir, f"{name}.zip")
        extract_to = os.path.join(extracted_dir, name)

        print(f"Processing {name}...")
        download_file(url, zip_path)
        extract_zip(zip_path, extract_to)

if __name__ == "__main__":
    main()