# Kaspi Price List Generator

This project automatically generates and updates a price list for the Kaspi online store based on products from the Wipon API.

## Features

- ✅ Fetches product data from Wipon API
- ✅ Converts JSON data to Kaspi XML format
- ✅ Automated updates via GitHub Actions (every 6 hours)
- ✅ Free hosting on GitHub Pages
- ✅ Public URL for Kaspi integration

## Setup Instructions

### 1. Fork this Repository

1. Fork this repository to your GitHub account
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/wipon-kaspi.git
   cd wipon-kaspi
   ```

### 2. Configure Wipon API Authentication

1. Go to your repository settings on GitHub
2. Navigate to "Secrets and variables" > "Actions"
3. Add a new repository secret named `WIPON_API_TOKEN`
4. Set the value to your Wipon API authentication token

### 3. Update Configuration

Edit `fetch_and_convert.py` and update the following values:

- **Company Name**: Change "Aliya Style" to your company name
- **Merchant ID**: Change "30375992" to your Kaspi merchant ID
- **API URL**: Update the Wipon API URL if needed
- **Employee ID**: Update the employee ID in the API URL

### 4. Enable GitHub Pages

1. Go to your repository settings
2. Scroll down to "Pages" section
3. Under "Source", select "Deploy from a branch"
4. Choose "gh-pages" branch and "/ (root)" folder
5. Click "Save"

### 5. Test the Setup

1. Push your changes to the main branch
2. The GitHub Action will automatically run
3. Check the "Actions" tab to see the workflow status
4. Once complete, your price list will be available at:
   `https://YOUR_USERNAME.github.io/wipon-kaspi/price.xml`

## Local Testing

To test the script locally with sample data:

```bash
python fetch_and_convert.py --sample
```

To test with real API data (requires valid token):

```bash
python fetch_and_convert.py
```

## File Structure

```
├── .github/workflows/
│   └── update-price-list.yml    # GitHub Actions workflow
├── fetch_and_convert.py         # Main script
├── requirements.txt             # Python dependencies
├── sample_data.json            # Sample data for testing
├── price.xml                   # Generated XML file (updated automatically)
└── README.md                   # This file
```

## Workflow Schedule

The GitHub Action runs:
- Every 6 hours automatically
- On every push to main branch
- Manually via "Actions" tab

## Kaspi Integration

1. Log into your Kaspi partner account
2. Go to the price list configuration
3. Set the XML URL to: `https://YOUR_USERNAME.github.io/wipon-kaspi/price.xml`
4. Kaspi will automatically pull updates from this URL

## Troubleshooting

### API Authentication Issues
- Verify your `WIPON_API_TOKEN` secret is set correctly
- Check that the token has the necessary permissions
- Ensure the API URL and parameters are correct

### XML Format Issues
- Check the generated `price.xml` file format
- Verify it matches Kaspi's required schema
- Test with a small sample of products first

### GitHub Actions Failures
- Check the "Actions" tab for error messages
- Verify all secrets are properly configured
- Ensure the workflow file syntax is correct

## Support

For issues or questions:
1. Check the GitHub Actions logs
2. Verify your configuration matches the requirements
3. Test locally with sample data first

## Cost

This solution is completely free:
- ✅ GitHub repository (free)
- ✅ GitHub Actions (free for public repos)
- ✅ GitHub Pages (free)
- ✅ No server costs
- ✅ No maintenance required
