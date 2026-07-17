"""
This script provides functions to download and extract the Mini-MIAS dataset from a specified URL. The dataset is
downloaded as a zip file and extracted to a specified destination folder, and a metadata file is created.

The script includes the following functions:
- `download_mini_mias(destination_folder)`: Downloads the Mini-MIAS dataset from the specified URL and saves it to the
given destination folder.
- `extract_mini_mias(zip_path, extract_to)`: Extracts the Mini-MIAS dataset from the specified zip file to the given
destination folder.
- `create_metadata_file(meta_file_path, static_file_path)`: Creates a metadata file for the Mini-MIAS dataset.

Please see NOTICE.md for acknowledgement and licensing information of the MIAS dataset.
"""
import os
import shutil
import zipfile
from pathlib import Path

import requests

URL = "https://www.repository.cam.ac.uk/bitstreams/5960ab2b-5ea2-4db1-96ac-15b3605e7485/download"

def download_mini_mias(destination_folder: Path | str) -> None:
    """
    Download the Mini-MIAS dataset from the given URL and save it to the specified destination folder.
    
    Parameters
    ----------
    destination_folder : Path or str
        The folder where the dataset will be saved. If it doesn't exist, it will be created.
    """
    # Check if the dataset has already been downloaded
    zip_file_path = os.path.join(destination_folder, "mini_mias.zip")
    if os.path.exists(zip_file_path):
        print(f"Mini-MIAS dataset already downloaded at {zip_file_path}. Skipping download.")
        return

    os.makedirs(destination_folder, exist_ok=True)

    print(f"Downloading Mini-MIAS dataset from {URL} to {destination_folder}...")
    response = requests.get(URL, stream=True, timeout=10)
    if response.status_code == 200:
        file_path = os.path.join(destination_folder, "mini_mias.zip")
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded Mini-MIAS dataset to {file_path}")
    else:
        print(f"Failed to download Mini-MIAS dataset. Status code: {response.status_code}")


def extract_mini_mias(zip_path: Path | str, extract_to: Path | str) -> None:
    """
    Extract the Mini-MIAS dataset from the given zip file to the specified folder.
    
    Parameters
    ----------
    zip_path : Path or str
        The path to the zip file containing the Mini-MIAS dataset.
    extract_to : Path or str
        The folder where the dataset will be extracted. If it doesn't exist, it will be created.
    """
    os.makedirs(extract_to, exist_ok=True)

    # Check if the dataset has already been extracted
    final_extract_path = os.path.join(extract_to, "MIASDBv1.21")
    if os.path.exists(final_extract_path) and os.listdir(final_extract_path):
        print(f"Mini-MIAS dataset already extracted to {final_extract_path}. Skipping extraction.")
        return

    print(f"Extracting Mini-MIAS dataset from {zip_path} to {extract_to}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted Mini-MIAS dataset to {extract_to}")

    # Clean up the zip file after extraction
    os.remove(zip_path)
    print(f"Removed zip file {zip_path}")


def create_metadata_file(meta_file_path: Path | str, static_file_path: Path | str) -> None:
    """
    Create a metadata file for the Mini-MIAS dataset, which contains metadata for each sample in the dataset.
    
    Unfortunately, the metadata provided in the download is in a PDF format, which is not easily parseable. It would
    also need some manual work to e.g., duplicate REFNUM for specific double-entry samples. Rather than work on the
    functionality for this, I have simply created a static mias_metadata.txt file that is included in the repository.
    
    This function is provided a) as a way to copy this text file into the correct path and b) as a placeholder for 
    possible future functionality to create the metadata file from the PDF.

    Parameters
    ----------
    meta_file_path : Path or str
        The path where the metadata file will be created.
    static_file_path : Path or str
        The path to the static mias_metadata.txt file that will be copied.
    """
    if os.path.exists(meta_file_path):
        print(f"Metadata file already exists at {meta_file_path}. Skipping creation.")
        return
    shutil.copy(static_file_path, meta_file_path)
    print(f"Copied metadata file from {static_file_path} to {meta_file_path}")


if __name__ == "__main__":
    DESTINATION_FOLDER = "data/mini_mias"
    download_mini_mias(DESTINATION_FOLDER)
    extract_mini_mias(f"{DESTINATION_FOLDER}/mini_mias.zip", DESTINATION_FOLDER)
    create_metadata_file(f"{DESTINATION_FOLDER}/metadata.txt", "scripts/mias_metadata.txt")
