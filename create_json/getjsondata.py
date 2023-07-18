import json
import requests

def fetch_data_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError('Failed to fetch data from the URL')

def save_data_to_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)

def main():
    url = 'https://api-adresse.data.gouv.fr/reverse/?lat=50.622772&lon=3.043936&limit=10'
    data = fetch_data_from_url(url)

    file_path = 'data.json'
    save_data_to_json_file(data, file_path)
    print(f'Data saved to {file_path}')

if __name__ == '__main__':
    main()
