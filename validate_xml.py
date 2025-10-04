#!/usr/bin/env python3
"""
XML validation script for Kaspi price list
"""

import xml.etree.ElementTree as ET
import sys
from datetime import datetime

def validate_kaspi_xml(xml_file):
    """Validate the Kaspi XML format."""
    try:
        # Parse XML
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        print(f"✅ XML file '{xml_file}' is well-formed")
        print(f"🔍 Root element tag: {root.tag}")
        
        # Check root element (handle namespaces)
        if root.tag.endswith('kaspi_catalog') or root.tag == 'kaspi_catalog':
            print("✅ Root element is correct")
        else:
            print(f"❌ Root element should be 'kaspi_catalog', got: {root.tag}")
            return False
        
        # Debug: print all child elements
        print(f"🔍 Root children: {[child.tag for child in root]}")
        
        # Check required attributes
        required_attrs = ['date']
        optional_attrs = ['xmlns', 'xmlns:xsi', 'xsi:schemaLocation']
        
        for attr in required_attrs:
            if attr not in root.attrib:
                print(f"❌ Missing required attribute: {attr}")
                return False
        
        present_attrs = 0
        for attr in optional_attrs:
            if attr in root.attrib:
                present_attrs += 1
        
        print("✅ All required attributes present")
        print(f"✅ {present_attrs}/{len(optional_attrs)} optional namespace attributes present")
        
        # Check company element (handle namespaces)
        company = root.find('.//{kaspiShopping}company')
        if company is None or not company.text:
            print("❌ Company name is missing")
            return False
        print(f"✅ Company: {company.text}")
        
        # Check merchant ID
        merchant_id = root.find('.//{kaspiShopping}merchantid')
        if merchant_id is None or not merchant_id.text:
            print("❌ Merchant ID is missing")
            return False
        print(f"✅ Merchant ID: {merchant_id.text}")
        
        # Check offers
        offers = root.find('.//{kaspiShopping}offers')
        if offers is None:
            print("❌ Offers section is missing")
            return False
        
        offer_count = len(offers.findall('.//{kaspiShopping}offer'))
        print(f"✅ Found {offer_count} offers")
        
        # Validate each offer
        valid_offers = 0
        for i, offer in enumerate(offers.findall('.//{kaspiShopping}offer')):
            if validate_offer(offer, i + 1):
                valid_offers += 1
        
        print(f"✅ {valid_offers}/{offer_count} offers are valid")
        
        # Check date format
        date_str = root.get('date')
        try:
            datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            print("✅ Date format is correct")
        except ValueError:
            print("⚠️  Date format might be incorrect")
        
        return True
        
    except ET.ParseError as e:
        print(f"❌ XML parsing error: {e}")
        return False
    except FileNotFoundError:
        print(f"❌ File '{xml_file}' not found")
        return False

def validate_offer(offer, offer_num):
    """Validate individual offer."""
    issues = []
    
    # Check SKU
    if 'sku' not in offer.attrib or not offer.attrib['sku']:
        issues.append("missing SKU")
    
    # Check model
    model = offer.find('.//{kaspiShopping}model')
    if model is None or not model.text:
        issues.append("missing model")
    
    # Check brand
    brand = offer.find('.//{kaspiShopping}brand')
    if brand is None or not brand.text:
        issues.append("missing brand")
    
    # Check price
    price = offer.find('.//{kaspiShopping}price')
    if price is None or not price.text:
        issues.append("missing price")
    else:
        try:
            float(price.text)
        except ValueError:
            issues.append("invalid price format")
    
    # Check availabilities
    availabilities = offer.find('.//{kaspiShopping}availabilities')
    if availabilities is None:
        issues.append("missing availabilities")
    else:
        avail = availabilities.find('.//{kaspiShopping}availability')
        if avail is None:
            issues.append("missing availability details")
        else:
            required_avail_attrs = ['available', 'storeId', 'stockCount']
            for attr in required_avail_attrs:
                if attr not in avail.attrib:
                    issues.append(f"missing {attr} in availability")
    
    if issues:
        print(f"⚠️  Offer {offer_num}: {', '.join(issues)}")
        return False
    else:
        print(f"✅ Offer {offer_num}: Valid")
        return True

def main():
    """Main validation function."""
    xml_file = "price.xml"
    
    if len(sys.argv) > 1:
        xml_file = sys.argv[1]
    
    print(f"🔍 Validating Kaspi XML: {xml_file}")
    print("=" * 50)
    
    if validate_kaspi_xml(xml_file):
        print("=" * 50)
        print("✅ XML validation completed successfully!")
        sys.exit(0)
    else:
        print("=" * 50)
        print("❌ XML validation failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
