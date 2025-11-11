thonimport json
from extractors.facebook_parser import parse_facebook_marketplace
from outputs.exporters import export_to_json
from config.settings import get_config

def run_scraper():
    config = get_config()
    marketplace_url = config['marketplace_url']
    listings = parse_facebook_marketplace(marketplace_url)
    export_to_json(listings, 'output.json')

if __name__ == "__main__":
    run_scraper()