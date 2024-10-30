# The script collects info regarding EoX based serials populated in serial.txt or pids added in pid.txt. It connects to Cisco API and saves the output in json files.

import requests
import json

# Define Cisco API Client ID and Secret
CLIENT_ID = '<your_client_id>'
CLIENT_SECRET = '<your_client_secret>'

# Set Cisco API Endpoints
TOKEN_URL = 'https://id.cisco.com/oauth2/default/v1/token'
EOX_SERIAL_API_URL = 'https://apix.cisco.com/supporttools/eox/rest/5/EOXBySerialNumber/1/'
EOX_PID_API_URL = 'https://apix.cisco.com/supporttools/eox/rest/5/EOXByProductID/'

def get_access_token():
    """Obtain an access token from Cisco API."""
    payload = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(TOKEN_URL, data=payload)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        raise Exception(f"Error fetching access token: {response.text}")

def get_eox_info(serial_number, access_token):
    """Get EoX information for a single serial number."""
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(f"{EOX_API_URL}{serial_number}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching EoX info for {serial_number}: {response.text}")
        return None

def load_serial_numbers(filename):
    """Load serial numbers from a text file."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def get_eox_info_pid(product_id, access_token):
    """Get EoX information for a single Product ID (PID)."""
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(f"{EOX_PID_API_URL}{product_id}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching EoX info for PID {product_id}: {response.text}")
        return None

def load_ids(filename):
    """Load IDs (serial numbers or PIDs) from a text file."""
EOX_SERIAL_API_URL = 'https://apix.cisco.com/supporttools/eox/rest/5/EOXBySerialNumber/1/'
EOX_PID_API_URL = 'https://apix.cisco.com/supporttools/eox/rest/5/EOXByProductID/1/'

def get_access_token():
    """Obtain an access token from Cisco API."""
    payload = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(TOKEN_URL, data=payload)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        raise Exception(f"Error fetching access token: {response.text}")

def get_eox_info_serial(serial_number, access_token):
    """Get EoX information for a single serial number."""
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(f"{EOX_SERIAL_API_URL}{serial_number}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching EoX info for serial {serial_number}: {response.text}")
        return None

def get_eox_info_pid(product_id, access_token):
    """Get EoX information for a single Product ID (PID)."""
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(f"{EOX_PID_API_URL}{product_id}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching EoX info for PID {product_id}: {response.text}")
        return None

def load_ids(filename):
    """Load IDs (serial numbers or PIDs) from a text file."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def main():
    serial_numbers_file = 'serials.txt'  # Update this to your serial numbers file
    product_ids_file = 'pids.txt'       # Update this to your PIDs file

    serial_numbers = load_ids(serial_numbers_file)
    product_ids = load_ids(product_ids_file)

    # Get access token
    access_token = get_access_token()

    # Collect EoX information for serial numbers
    eox_data_serials = []
    for serial in serial_numbers:
        info = get_eox_info_serial(serial, access_token)
        if info:
            eox_data_serials.append({serial: info})

    # Collect EoX information for Product IDs (PIDs)
    eox_data_pids = []
    for pid in product_ids:
        info = get_eox_info_pid(pid, access_token)
        if info:
            eox_data_pids.append({pid: info})

    # Save serials results to a separate file
    with open('eox_serials_results.json', 'w') as file:
        json.dump(eox_data_serials, file, indent=4)

    # Save PIDs results to a separate file
    with open('eox_pids_results.json', 'w') as file:
        json.dump(eox_data_pids, file, indent=4)

    print("EoX information collection complete. Serial Data saved to eox_serials_results.json. PID Data saved tp eox_pids_results.json")

if __name__ == "__main__":
    main()
