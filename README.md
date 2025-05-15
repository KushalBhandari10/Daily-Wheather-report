# 📰 Daily Report Bot

A Python bot that scrapes daily weather data, saves it in a report folder, and emails it to you every morning — fully automated.

---

## 🔧 Features

- ✅ Scrapes weather data using `requests` + `BeautifulSoup`
- ✅ Saves data as a JSON file in a timestamped folder
- ✅ Sends report via email (SMTP with Gmail)
- ✅ Runs daily at 7:00 AM using `schedule`

---

## 📦 Requirements

```bash
pip install requests beautifulsoup4 schedule
```

---

## 📁 Directory Structure

```
Daily-Report-Bot/
├── wheather_report.py
├── Reports/
│   └── YYYY-MM-DD/
│       └── weather_report.json
└── README.md
```

---

## ⚙️ Configuration

Edit the following in `weather_report.py`:

```python
sender = "your-email@gmail.com"
receiver = "your-email@gmail.com"
password = "your-app-password"  # Generate from Gmail settings
```

Replace the URL in `scrape_weather()` with your location URL from [weather.com](https://weather.com/).

---

## 🧪 Run Manually

```python
daily_bot()
```

---

## ▶️ Run Automatically

```bash
python daily_bot.py
```

The script runs continuously and sends the report every day at **7:00 AM**.

---

## 🔐 Security Note

Use [Gmail App Passwords](https://support.google.com/accounts/answer/185833) instead of your actual Gmail password.

---

## 📬 Sample Output

```json
{
  "temperature": "25°C",
  "condition": "Sunny"
}
```

---

## 💡 Future Improvements

- Add support for news and stock reports  
- Export as CSV  
- Telegram bot integration  

---

Enjoy automated daily updates! 🌤️
