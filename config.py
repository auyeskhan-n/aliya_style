"""
Configuration file for Kaspi Price List Generator
Update these values according to your setup
"""

# Company Information
COMPANY_NAME = "Aliya Style"
MERCHANT_ID = "30375992"

# Wipon API Configuration
WIPON_API_URL = "https://api.wipon.kz/v2/employee/46315/item"
EMPLOYEE_ID = "46315"
STOCK_ID = "81367"

# API Parameters
API_PARAMS = {
    "type": 0,
    "stock_id": STOCK_ID,
    "page": 1,
    "per_page": 500,
    "positive_balance": 1,
    "is_weighted": 0,
    "trashed": 0,
    "only_parents": 1
}

# Kaspi Store Configuration
STORE_ID = "PP1"

# Output Configuration
OUTPUT_FILE = "price.xml"
