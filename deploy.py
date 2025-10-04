#!/usr/bin/env python3
"""
Deployment script for GitHub Pages
This script prepares the files for GitHub Pages deployment
"""

import os
import shutil
from datetime import datetime

def deploy_to_gh_pages():
    """Prepare files for GitHub Pages deployment."""
    
    # Create gh-pages directory
    gh_pages_dir = "gh-pages"
    if os.path.exists(gh_pages_dir):
        shutil.rmtree(gh_pages_dir)
    os.makedirs(gh_pages_dir)
    
    # Copy XML file to gh-pages directory
    if os.path.exists("price.xml"):
        shutil.copy2("price.xml", gh_pages_dir)
        print("✅ Copied price.xml to gh-pages directory")
    else:
        print("❌ price.xml not found. Please run fetch_and_convert.py first.")
        return False
    
    # Create index.html for GitHub Pages
    index_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kaspi Price List</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #333;
            text-align: center;
        }}
        .info {{
            background-color: #e8f4f8;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }}
        .xml-link {{
            display: inline-block;
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            margin: 10px 0;
        }}
        .xml-link:hover {{
            background-color: #0056b3;
        }}
        .timestamp {{
            color: #666;
            font-size: 0.9em;
            text-align: center;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🛍️ Kaspi Price List</h1>
        
        <div class="info">
            <h3>📋 Price List Information</h3>
            <p>This page provides the XML price list for Kaspi marketplace integration.</p>
            <p>The price list is automatically updated every 6 hours from the Wipon API.</p>
        </div>
        
        <h3>🔗 Download XML Price List</h3>
        <a href="price.xml" class="xml-link" download>Download price.xml</a>
        
        <h3>🔧 Integration Instructions</h3>
        <ol>
            <li>Copy the XML URL: <code>https://YOUR_USERNAME.github.io/wipon-kaspi/price.xml</code></li>
            <li>Log into your Kaspi partner account</li>
            <li>Go to price list configuration</li>
            <li>Paste the XML URL in the appropriate field</li>
            <li>Kaspi will automatically pull updates from this URL</li>
        </ol>
        
        <div class="timestamp">
            Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")}
        </div>
    </div>
</body>
</html>"""
    
    with open(os.path.join(gh_pages_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_content)
    
    print("✅ Created index.html for GitHub Pages")
    print(f"✅ Deployment files ready in {gh_pages_dir}/ directory")
    print("\n📝 Next steps:")
    print("1. Commit and push your changes")
    print("2. Enable GitHub Pages in repository settings")
    print("3. Set source to 'gh-pages' branch")
    print("4. Your price list will be available at:")
    print("   https://YOUR_USERNAME.github.io/wipon-kaspi/price.xml")
    
    return True

if __name__ == "__main__":
    deploy_to_gh_pages()
