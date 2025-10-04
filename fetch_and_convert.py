#!/usr/bin/env python3
"""
Script to fetch product data from Wipon API and convert to Kaspi XML format.
"""

import requests
import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime
import json
import sys
import os
from config import (
    COMPANY_NAME, MERCHANT_ID, WIPON_API_URL, API_PARAMS, 
    STORE_ID, OUTPUT_FILE
)

def fetch_wipon_data(use_sample=False):
    """Fetch product data from Wipon API or use sample data."""
    if use_sample:
        try:
            with open('sample_data.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Sample data file not found. Please create sample_data.json")
            sys.exit(1)
    
    url = WIPON_API_URL
    
    # Add authentication headers
    token = os.getenv('WIPON_API_TOKEN')
    headers = {
        'Accept': 'application/json'
    }
    if token:
        headers['Authorization'] = f'Bearer {token}'
    
    all_products = []
    page = 1
    
    try:
        while True:
            params = API_PARAMS.copy()
            params['page'] = page
            
            print(f"Fetching page {page}...")
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            
            # Debug: Print API response structure for first page
            if page == 1 and 'meta' in data:
                meta = data['meta']
                print(f"API Info: {meta.get('total', 'unknown')} total products across {meta.get('last_page', 'unknown')} pages")
            
            # Check if we have products in this page
            if 'data' not in data or not data['data']:
                print(f"No more products found on page {page}")
                break
                
            # Add products from this page
            page_products = data['data']
            all_products.extend(page_products)
            print(f"Found {len(page_products)} products on page {page}")
            
            # Check if this is the last page
            if 'meta' in data:
                meta = data['meta']
                if page >= meta.get('last_page', page):
                    print(f"Reached last page ({meta.get('last_page', page)})")
                    break
            else:
                # Fallback: if no meta, check if we got fewer products than expected
                if len(page_products) < 250:  # API seems to limit to 250 per page
                    print(f"Last page reached (got {len(page_products)} < 250)")
                    break
                
            page += 1
            
            # Safety limit to prevent infinite loops
            if page > 50:
                print("Reached safety limit of 50 pages")
                break
        
        print(f"Total products fetched: {len(all_products)}")
        
        # Return in the same format as the original API response
        return {
            'data': all_products,
            'meta': {
                'total': len(all_products),
                'pages_fetched': page - 1,
                'last_page': page - 1
            }
        }
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Wipon API: {e}")
        print("Falling back to sample data...")
        return fetch_wipon_data(use_sample=True)

def convert_to_kaspi_xml(data):
    """Convert Wipon JSON data to Kaspi XML format."""
    # Create root element
    root = ET.Element("kaspi_catalog")
    root.set("date", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    root.set("xmlns", "kaspiShopping")
    root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    root.set("xsi:schemaLocation", "kaspiShopping http://kaspi.kz/kaspishopping.xsd")
    
    # Add company and merchant ID
    company = ET.SubElement(root, "company")
    company.text = COMPANY_NAME
    
    merchant_id = ET.SubElement(root, "merchantid")
    merchant_id.text = MERCHANT_ID
    
    # Add offers
    offers = ET.SubElement(root, "offers")
    
    # Process each product
    if 'data' in data:
        for product in data['data']:
            # Skip products with negative quantity only (include zero quantity products)
            if float(product.get('quantity', 0)) < 0:
                continue
                
            offer = ET.SubElement(offers, "offer")
            offer.set("sku", product.get('vendor_code', ''))
            
            # Model (title)
            model = ET.SubElement(offer, "model")
            model.text = product.get('title', '')
            
            # Brand (first part of title before |)
            brand = ET.SubElement(offer, "brand")
            title = product.get('title', '')
            brand_text = title.split('|')[0].strip() if '|' in title else title
            brand.text = brand_text
            
            # Availabilities
            availabilities = ET.SubElement(offer, "availabilities")
            availability = ET.SubElement(availabilities, "availability")
            
            # Set availability based on quantity
            quantity = float(product.get('quantity', 0))
            if quantity > 0:
                availability.set("available", "yes")
            else:
                availability.set("available", "no")
                
            availability.set("storeId", STORE_ID)
            availability.set("stockCount", str(int(quantity)))
            
            # Price (must be integer according to XSD)
            price = ET.SubElement(offer, "price")
            price_value = float(product.get('selling_price', 0))
            price.text = str(int(price_value))
    
    return root

def format_xml(root):
    """Format XML with proper indentation."""
    rough_string = ET.tostring(root, encoding='utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ", encoding='utf-8')

def main():
    """Main function to fetch data and generate XML."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate Kaspi XML price list from Wipon API')
    parser.add_argument('--sample', action='store_true', help='Use sample data instead of API')
    args = parser.parse_args()
    
    if args.sample:
        print("Using sample data...")
        data = fetch_wipon_data(use_sample=True)
    else:
        print("Fetching data from Wipon API...")
        data = fetch_wipon_data()
    
    print(f"Found {len(data.get('data', []))} products")
    
    print("Converting to Kaspi XML format...")
    xml_root = convert_to_kaspi_xml(data)
    
    print("Formatting XML...")
    formatted_xml = format_xml(xml_root)
    
    # Save to file
    with open(OUTPUT_FILE, 'wb') as f:
        f.write(formatted_xml)
    
    print(f"XML price list saved to {OUTPUT_FILE}")
    
    # Print summary
    offers_count = len(xml_root.find('offers'))
    print(f"Generated XML with {offers_count} offers")

if __name__ == "__main__":
    main()
