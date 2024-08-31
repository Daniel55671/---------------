import requests
import os
import time

apikey = input("Enter your API key: ")
upload_url = 'https://www.virustotal.com/api/v3/files'
report_url = 'https://www.virustotal.com/api/v3/analyses/'

def upload_file(file_path):
    headers = {
        'x-apikey': apikey
    }
    with open(file_path, 'rb') as file:
        response = requests.post(upload_url, headers=headers, files={'file': file})
    if response.status_code == 200:
        result = response.json()
        print(f"Upload successful: {result}")
        return result.get('data', {}).get('id')
    else:
        print(f"Failed to upload this file: {response.status_code}")
        print(response.json())
        return None

def check_analysis_status(analysis_id):
    headers = {
        'x-apikey': apikey
    }
    url = f"{report_url}{analysis_id}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        result = response.json()
        status = result.get('data', {}).get('attributes', {}).get('status', 'unknown')
        print(f"Analysis status for ID {analysis_id}: {status}")  # Debugging line
        return status
    else:
        print(f"Failed to check analysis status: {response.status_code}")
        print(response.json())
        return None

def check_file(file_path):
    analysis_id = upload_file(file_path)
    if analysis_id:
        print("Waiting for analysis to complete...")
        while True:
            status = check_analysis_status(analysis_id)
            if status == 'completed':
                headers = {
                    'x-apikey': apikey
                }
                response = requests.get(f"{report_url}{analysis_id}", headers=headers)
                if response.status_code == 200:
                    result = response.json()
                    print(f"Report retrieval successful: {result}")
                    attributes = result.get('data', {}).get('attributes', {})
                    last_analysis_stats = attributes.get('last_analysis_stats', {})
                    positives = last_analysis_stats.get('malicious', 0)
                    total = last_analysis_stats.get('total', 0)
                    if positives > 0:
                        print(f"File {file_path} is not clean.")
                    else:
                        print(f"File {file_path} is clean.")
                else:
                    print(f"Failed to retrieve report for {file_path}: {response.status_code}")
                    print(response.json())
                break
            elif status == 'queued':
                print("Analysis is still in progress. Checking again...")
            else:
                print("Unexpected analysis status.")
                break
            time.sleep(30)  # Wait for 30 seconds before checking the status again
    else:
        print("Failed to upload file, cannot check report")

def check_folder(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            check_file(file_path)

def main():
    path = input("Enter the file or folder path: ")
    if os.path.isfile(path):
        check_file(path)
    elif os.path.isdir(path):
        check_folder(path)
    else:
        print("Invalid path, please enter a valid file or folder path")

if __name__ == "__main__":
    main()
