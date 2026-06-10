# Google Maps Scraper

A Python-based web scraper that extracts business information from Google Maps search results using Selenium and saves the data to an Excel file.

## Features

- 🔍 Search for businesses by location and service type on Google Maps
- 📊 Extract detailed business information including:
  - Business name
  - Subtitle/category
  - Business type
  - Website URL
  - Phone number
  - Address
  - Plus Code
- 💾 Export results to Excel (.xlsx) format
- ⚙️ Automated scrolling and data collection

## Prerequisites

Before running this scraper, ensure you have:

- Python 3.7+
- Google Chrome browser installed
- ChromeDriver matching your Chrome version ([Download here](https://chromedriver.chromium.org/))

## Installation

1. **Clone or download this repository**

   ```bash
   git clone <repository-url>
   cd google-maps-scraper
   ```
2. **Install required dependencies**

   ```bash
   pip install selenium pandas pyautogui
   ```
3. **Download ChromeDriver**

   - Download ChromeDriver from [here](https://chromedriver.chromium.org/)
   - Make sure it matches your Chrome browser version
   - Place it in your system PATH or in the same directory as the script

## Usage

1. **Run the script**

   ```bash
   python scraper.py
   ```
2. **Follow the prompts**

   - Enter the location you want to search for (e.g., "New York")
   - Enter the service/business type you want to find (e.g., "restaurants", "coffee shops")
3. **Wait for results**

   - The script will open Google Maps in a browser
   - It will automatically search and collect data
   - Results will be saved to `data of {service} in {location}.xlsx`

## How It Works

1. Opens Google Maps in a Chrome browser
2. Searches for the specified service in the given location
3. Scrolls through the search results to load more entries
4. Clicks on each result to view detailed information
5. Extracts business information from the detail panel
6. Stores all data in a pandas DataFrame
7. Exports the data to an Excel file with timestamp

## Output

The scraper generates an Excel file named:

```
data of {service} in {location}.xlsx
```

The file contains the following columns:

- **Destination Name**: Business name
- **Destination subtitle**: Business category/subtitle
- **Destination type**: Type of business
- **Destination website**: Website URL
- **Destination phone**: Contact phone number
- **Destination address**: Full business address
- **Destination plus code**: Google Plus Code

## Important Notes

⚠️ **Disclaimer**: This scraper is for educational purposes only. Please respect Google Maps' Terms of Service and robots.txt. Excessive scraping may result in IP blocking.

### Known Issues & Limitations

- Depends on Google Maps UI structure - changes to Google Maps may break selectors
- Some fields may be unavailable for certain businesses (returns `None`)
- Requires manual interaction to avoid bot detection
- Slow execution is intentional (includes delays to be respectful)

## Requirements

```
selenium>=3.141.0
pandas>=1.0.0
pyautogui>=0.9.53
```

## Troubleshooting

**ChromeDriver errors:**

- Ensure ChromeDriver version matches your Chrome browser version
- Check that ChromeDriver is in your system PATH

**Element not found errors:**

- Google Maps UI may have changed - XPath selectors may need updating
- Some businesses may not have all information available

**Connection timeouts:**

- Increase sleep times in the script if experiencing timeout issues
- Check your internet connection

## Future Improvements

- [ ] Implement headless Chrome mode
- [ ] Add proxy support for better reliability
- [ ] Implement retry logic for failed data extraction
- [ ] Add filtering and sorting options
- [ ] Create a GUI for easier input

## License

This project is provided as-is for educational purposes.

## Contributing

Feel free to fork, modify, and improve this project. Please ensure any changes respect Google Maps' Terms of Service.

---

**Last Updated**: 2026-06-11
