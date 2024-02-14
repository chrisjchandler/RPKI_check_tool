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

Troubleshooting
Ensure you have an active internet connection as the script fetches data from the RIPE Stat API.
If you encounter any issues with fetching data, verify the ASN and prefix inputs are correct and retry.
For requests library installation issues, ensure you have pip installed and your Python environment set up correctly.

License
This tool is open-source and free to use. Modify and distribute as you see fit.
