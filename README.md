RPKI Check Tool
Overview
The RPKI Check Tool is a Python script designed to help users fetch and display RPKI (Resource Public Key Infrastructure) validation data for prefixes associated with a given ASN (Autonomous System Number). This tool interacts with the RIPE Stat API to retrieve announced prefixes for an ASN and then allows the user to select a prefix to fetch its RPKI validation status.

Prerequisites
Python 3.x
requests library
Setup
Before running the script, ensure you have Python installed on your system. You can download Python from python.org.

Next, install the requests library using pip if you haven't already:
pip install requests

Running the Tool
Save the script to a file named rpki_check.py.
Open a terminal or command prompt.
Navigate to the directory where rpki_check.py is saved.
Run the script using Python:

python rpki_check.py (obviously use python3 when using python3 etc.) 

Usage Instructions
Enter ASN: When prompted, enter the ASN for which you wish to check RPKI data. Input should be the ASN number without the "AS" prefix.

Select Prefix: The script will then fetch and display the prefixes announced by the entered ASN. Select the prefix for which you want to check the RPKI validation status by entering the corresponding number.

View RPKI Data: The script will fetch and display the RPKI validation data for the selected prefix in a readable format. This includes whether the prefix's announcement is valid, invalid, or not found within the RPKI framework.

Output samples:

Tabbed (main script) 
Fetching RPKI validation data for ASN {asn} and prefix {selected_prefix}...
{
    "messages": [],
    "see_also": [],
    "version": "0.3",
    "data_call_name": "rpki-validation",
    "data_call_status": "supported",
    "cached": false,
    "data": {
        "validating_roas": [
            {
                "origin": "16509",
                "prefix": "198.160.143.0/24",
                "max_length": 24,
                "validity": "valid"
            }
        ],
        "status": "valid",
        "validator": "routinator",
        "resource": "16509",
        "prefix": "198.160.143.0/24"
    },
    "query_id": "20240214225248-f604791c-03a5-4224-a616-e1791002a473",
    "process_time": 12,
    "server_id": "app142",
    "build_version": "live.2024.2.7.194",
    "status": "ok",
    "status_code": 200,
    "time": "2024-02-14T22:52:48.642954"
}

One lined (one line script)

Selected prefix: 64.64.100.0/23

Fetching RPKI validation data for ASN {asn} and prefix {selected_prefix}...
{'messages': [], 'see_also': [], 'version': '0.3', 'data_call_name': 'rpki-validation', 'data_call_status': 'supported', 'cached': False, 'data': {'validating_roas': [{'origin': '16509', 'prefix': '64.64.100.0/23', 'max_length': 24, 'validity': 'valid'}, {'origin': '14618', 'prefix': '64.64.100.0/23', 'max_length': 24, 'validity': 'invalid_asn'}], 'status': 'valid', 'validator': 'routinator', 'resource': '16509', 'prefix': '64.64.100.0/23'}, 'query_id': '20240214225958-b4773569-d65f-4bc1-b4bf-9425cccc64e8', 'process_time': 23, 'server_id': 'app145', 'build_version': 'live.2024.2.7.194', 'status': 'ok', 'status_code': 200, 'time': '2024-02-14T22:59:58.364352'}


Troubleshooting
Ensure you have an active internet connection as the script fetches data from the RIPE Stat API.
If you encounter any issues with fetching data, verify the ASN and prefix inputs are correct and retry.
For requests library installation issues, ensure you have pip installed and your Python environment set up correctly.

License
This tool is open-source and free to use. Modify and distribute as you see fit.


