#!/usr/bin/env python3
"""
Setup script for Kaspi Price List Generator
This script helps configure the system for your specific setup
"""

import os
import sys
from pathlib import Path

def update_config():
    """Update configuration with user input."""
    print("🔧 Kaspi Price List Generator Setup")
    print("=" * 50)
    
    # Read current config
    config_file = Path("config.py")
    if not config_file.exists():
        print("❌ config.py not found!")
        return False
    
    with open(config_file, 'r', encoding='utf-8') as f:
        config_content = f.read()
    
    print("\n📝 Please provide the following information:")
    print("(Press Enter to keep current values)")
    
    # Get company information
    current_company = "Aliya Style"
    company = input(f"\n1. Company Name [{current_company}]: ").strip()
    if not company:
        company = current_company
    
    current_merchant = "30375992"
    merchant_id = input(f"2. Kaspi Merchant ID [{current_merchant}]: ").strip()
    if not merchant_id:
        merchant_id = current_merchant
    
    # Get Wipon API information
    current_employee = "46315"
    employee_id = input(f"3. Wipon Employee ID [{current_employee}]: ").strip()
    if not employee_id:
        employee_id = current_employee
    
    current_stock = "81367"
    stock_id = input(f"4. Wipon Stock ID [{current_stock}]: ").strip()
    if not stock_id:
        stock_id = current_stock
    
    # Update config file
    config_content = config_content.replace(f'COMPANY_NAME = "{current_company}"', f'COMPANY_NAME = "{company}"')
    config_content = config_content.replace(f'MERCHANT_ID = "{current_merchant}"', f'MERCHANT_ID = "{merchant_id}"')
    config_content = config_content.replace(f'EMPLOYEE_ID = "{current_employee}"', f'EMPLOYEE_ID = "{employee_id}"')
    config_content = config_content.replace(f'STOCK_ID = "{current_stock}"', f'STOCK_ID = "{stock_id}"')
    config_content = config_content.replace(f'"https://api.wipon.kz/v2/employee/{current_employee}/item"', f'"https://api.wipon.kz/v2/employee/{employee_id}/item"')
    
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write(config_content)
    
    print("\n✅ Configuration updated!")
    return True

def test_setup():
    """Test the setup with sample data."""
    print("\n🧪 Testing setup with sample data...")
    
    try:
        # Run the script with sample data
        result = os.system("python fetch_and_convert.py --sample")
        if result != 0:
            print("❌ Script execution failed!")
            return False
        
        # Validate the generated XML
        result = os.system("python validate_xml.py")
        if result != 0:
            print("❌ XML validation failed!")
            return False
        
        print("✅ Setup test completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def show_next_steps():
    """Show next steps for deployment."""
    print("\n🚀 Next Steps for Deployment:")
    print("=" * 50)
    
    print("\n1. 🔐 Configure GitHub Secrets:")
    print("   - Go to your GitHub repository settings")
    print("   - Navigate to 'Secrets and variables' > 'Actions'")
    print("   - Add secret: WIPON_API_TOKEN = your_api_token")
    
    print("\n2. 📄 Enable GitHub Pages:")
    print("   - Go to repository settings > Pages")
    print("   - Source: Deploy from a branch")
    print("   - Branch: gh-pages, Folder: / (root)")
    
    print("\n3. 🔄 Push to GitHub:")
    print("   git add .")
    print("   git commit -m 'Initial setup'")
    print("   git push origin main")
    
    print("\n4. 🔗 Your price list will be available at:")
    print("   https://YOUR_USERNAME.github.io/wipon-kaspi/price.xml")
    
    print("\n5. 🛍️ Configure Kaspi:")
    print("   - Log into Kaspi partner account")
    print("   - Set XML URL to your GitHub Pages URL")
    print("   - Kaspi will automatically pull updates")

def main():
    """Main setup function."""
    print("Welcome to Kaspi Price List Generator Setup!")
    
    if not update_config():
        sys.exit(1)
    
    if not test_setup():
        print("\n❌ Setup test failed. Please check your configuration.")
        sys.exit(1)
    
    show_next_steps()
    
    print("\n🎉 Setup completed successfully!")
    print("Your system is ready for deployment to GitHub.")

if __name__ == "__main__":
    main()
