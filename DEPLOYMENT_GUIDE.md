# 🚀 Deployment Guide - Kaspi Price List Generator

## ✅ What's Been Created

Your automated Kaspi price list system is now ready! Here's what has been built:

### 📁 Project Structure
```
wipon-kaspi/
├── .github/workflows/
│   └── update-price-list.yml    # Automated updates every 6 hours
├── fetch_and_convert.py         # Main conversion script
├── config.py                    # Configuration settings
├── validate_xml.py             # XML validation tool
├── deploy.py                   # GitHub Pages deployment
├── setup.py                    # Interactive setup wizard
├── requirements.txt            # Python dependencies
├── sample_data.json           # Test data
├── Makefile                    # Common tasks
├── README.md                   # Documentation
└── gh-pages/                   # GitHub Pages files
    ├── index.html
    └── price.xml
```

### 🔧 Key Features
- ✅ **Automatic API Integration**: Fetches data from Wipon API
- ✅ **XML Conversion**: Converts JSON to Kaspi XML format
- ✅ **Automated Updates**: GitHub Actions runs every 6 hours
- ✅ **Free Hosting**: GitHub Pages provides public URL
- ✅ **Validation**: Built-in XML validation
- ✅ **Zero Cost**: Uses only free services

## 🚀 Quick Deployment Steps

### 1. Push to GitHub
```bash
git add .
git commit -m "Initial Kaspi price list setup"
git push origin main
```

### 2. Configure GitHub Secrets
1. Go to your repository on GitHub
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `WIPON_API_TOKEN`
5. Value: Your Wipon API authentication token
6. Click **Add secret**

### 3. Enable GitHub Pages
1. Go to **Settings** → **Pages**
2. Under **Source**, select **Deploy from a branch**
3. Branch: `gh-pages`
4. Folder: `/ (root)`
5. Click **Save**

### 4. Configure Kaspi
1. Log into your Kaspi partner account
2. Go to price list configuration
3. Set XML URL to: `https://YOUR_USERNAME.github.io/wipon-kaspi/price.xml`
4. Kaspi will automatically pull updates

## 🧪 Testing Your Setup

### Local Testing
```bash
# Test with sample data
make test

# Validate XML format
make validate

# Run complete pipeline
make all
```

### GitHub Actions Testing
1. Go to **Actions** tab in your repository
2. Click **Update Kaspi Price List**
3. Click **Run workflow**
4. Monitor the execution

## 📊 Your Price List URL

Once deployed, your price list will be available at:
```
https://YOUR_USERNAME.github.io/wipon-kaspi/price.xml
```

Example:
```
https://aliyastyle.github.io/wipon-kaspi/price.xml
```

## 🔄 Update Schedule

- **Automatic**: Every 6 hours
- **Manual**: Push to main branch
- **On-demand**: GitHub Actions interface

## 🛠️ Customization

### Update Configuration
```bash
# Run interactive setup
make setup

# Or edit config.py directly
nano config.py
```

### Key Settings in `config.py`:
- `COMPANY_NAME`: Your company name
- `MERCHANT_ID`: Your Kaspi merchant ID
- `EMPLOYEE_ID`: Your Wipon employee ID
- `STOCK_ID`: Your Wipon stock ID

## 🔍 Monitoring

### Check GitHub Actions
1. Go to **Actions** tab
2. View latest workflow runs
3. Check logs for any errors

### Validate XML
```bash
make validate
```

### View Generated XML
```bash
cat price.xml
```

## 🚨 Troubleshooting

### API Authentication Issues
- Verify `WIPON_API_TOKEN` secret is set
- Check token has correct permissions
- Test API endpoint manually

### XML Format Issues
- Run `make validate` to check format
- Compare with Kaspi documentation
- Test with small sample first

### GitHub Actions Failures
- Check **Actions** tab for error logs
- Verify all secrets are configured
- Ensure workflow file syntax is correct

### GitHub Pages Not Working
- Check **Pages** settings in repository
- Verify `gh-pages` branch exists
- Wait a few minutes for deployment

## 📈 Success Indicators

✅ **Setup Complete When:**
- GitHub Actions runs without errors
- XML file is generated and valid
- GitHub Pages URL is accessible
- Kaspi can fetch the XML file

## 🎯 Next Steps

1. **Monitor**: Check first few automated runs
2. **Test**: Verify Kaspi integration works
3. **Optimize**: Adjust update frequency if needed
4. **Scale**: Add more products or features

## 📞 Support

If you encounter issues:
1. Check the **Actions** logs first
2. Run local tests with `make all`
3. Verify configuration in `config.py`
4. Test API connectivity manually

## 🎉 Congratulations!

You now have a fully automated, zero-cost Kaspi price list system that:
- Updates automatically every 6 hours
- Hosts on free GitHub Pages
- Integrates seamlessly with Kaspi
- Requires no maintenance

Your price list will always be up-to-date and accessible at your GitHub Pages URL!
