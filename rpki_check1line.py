import requests

def fetch_prefixes_for_asn(asn):
    """Fetch prefixes for a given ASN using the RIPE Stat API."""
    api_url = f'https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS{asn}'
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        prefixes = data['data']['prefixes']
        return [prefix['prefix'] for prefix in prefixes]
    except requests.RequestException as e:
        print(f"Error fetching prefixes: {e}")
        return []

def select_prefix(prefixes):
    """Prompt the user to select a prefix from the list."""
    for idx, prefix in enumerate(prefixes, start=1):
        print(f"{idx}. {prefix}")
    while True:
        choice = input("Select a prefix by number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(prefixes):
            return prefixes[int(choice) - 1]
        else:
            print("Invalid selection. Please try again.")

def fetch_rpki_validation(asn, prefix):
    """Fetch RPKI validation information for a given ASN and prefix."""
    api_url = f'https://stat.ripe.net/data/rpki-validation/data.json?resource=AS{asn}&prefix={prefix}'
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching RPKI validation information: {e}")
        return {}

def main():
    asn = input("Enter ASN (without 'AS' prefix): ")
    prefixes = fetch_prefixes_for_asn(asn)
    if prefixes:
        print("\nAvailable prefixes:")
        selected_prefix = select_prefix(prefixes)
        print(f"\nSelected prefix: {selected_prefix}")
        print("\nFetching RPKI validation data for ASN {asn} and prefix {selected_prefix}...")
        rpki_info = fetch_rpki_validation(asn, selected_prefix)
        print(rpki_info)  # Consider parsing this data for a user-friendly display.
    else:
        print("No prefixes found for this ASN.")

if __name__ == "__main__":
    main()
