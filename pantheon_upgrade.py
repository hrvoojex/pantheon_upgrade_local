#!/usr/bin/env python3
# coding: utf-8 -*-

""" Automatska nadogradnja Pantheona za neposlušne

# Windows:
# platform.win32_ver() --> ('XP', '5.1.2600', 'SP3', 'Multiprocessor Free')
# uname_result(system='Windows', node='DOMAGOJ-STROJ', release='XP', version='5.1.
# 2600', machine='x86', processor='x86 Family 6 Model 42 Stepping 7, GenuineIntel')
# Ako je procesor 64-bitni, onda je 'processor=AMD64'
#
# Linux:
# uname_result(system='Linux', node='probook6470b', release='4.10.0-24-generic',
# version='#28-Ubuntu SMP Wed Jun 14 08:14:34 UTC 2017', machine='x86_64', processor='x86_64')
# Ako je procesor 32-bitni onda je 'processor=i686'
#
# Ovdje je objašnjeno --> url: https://pymotw.com/2/platform/
"""

import sys
import platform
import requests
import time
import os.path

# When downloading large files from Google Drive, a single GET request is not
# sufficient. A second one is needed, and this one has an extra URL parameter
# called confirm, whose value should equal the value of a certain cookie.
# https://stackoverflow.com/questions/25010369/wget-curl-large-file-from-google-drive
def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def where_to_save():
    my_os_version = (
        platform.system(), platform.release(), platform.win32_ver()[2],
        platform.version(), platform.machine())

    # Asign a path based on a CPU arch
    my_x86_path = "C:/Program Files/DataLab/"
    my_x64_path = "C:/Program Files (x86)/DataLab/"

    if platform.machine() == "x86" or platform.machine() == "i686":
        my_pantheon_path = my_x86_path
    elif platform.machine() == "AMD64" or platform.machine() == "x86_64":
        my_pantheon_path = my_x64_path
    else:
        my_pantheon_path = "Unknown"
        print("No arch detected...")
        sys.exit()

    print(my_os_version)
    print(my_pantheon_path)

    return(my_pantheon_path)


if __name__ == "__main__":
    my_pantheon_path = where_to_save()
    # Anyone with the link can view - Google Disk Share
    url_origin = 'https://drive.google.com/file/d/0BwYhPjVGn186X0pwVWk1MjBiZ3M/view?usp=sharing'
    file_id = '0BwYhPjVGn186X0pwVWk1MjBiZ3M'
    destination = os.path.join(my_pantheon_path, 'Pantheon.exe')
    download_file_from_google_drive(file_id, destination)
    print("Završeno preuzimanje.")
    time.sleep(5)
