# 📰 Web Scraper for News Headlines

Looking to stay updated with the latest headlines — straight from **BBC News** — in a neat and organized way? This simple Python script fetches fresh headlines and saves them for you, all within seconds!

## ✨ What This Script Does

* 🌐 Connects to the [BBC News homepage](https://www.bbc.com/news)
* 🔍 Extracts all `<h2>` tags (typically where headlines live)
* 🧹 Filters out duplicate or empty entries
* 💾 Saves the headlines into a text file: `headlines.txt`

Perfect for:

* Journalists or bloggers tracking news trends
* Developers learning web scraping
* Anyone who just loves clean news summaries

---

## 🧰 Requirements

Before you run the script, make sure you have Python installed along with the following packages:

```bash
pip install requests beautifulsoup4
```

---

## 🚀 How to Use

1. **Download** or **clone** this script to your machine.
2. Open a terminal or command prompt in the project folder.
3. Run the script using:

```bash
python WebScraper.py
```

> If your file is named differently, update the command accordingly.

4. Boom! 🎉 You'll find a fresh list of news headlines saved in `headlines.txt`.

---

## 📦 Sample Output

Here’s what the output might look like:

```
New UK Prime Minister sets out first steps
Wildfires spread across southern Europe
NASA plans new moon mission in 2026
```

Each headline is on its own line — ready for use in summaries, apps, dashboards, or daily reading.

---

## ⚠️ A Few Things to Note

* This script scrapes `<h2>` tags, which usually contain the main headlines — but websites change. If the output looks odd, the page structure might have been updated.
* This is for **educational or personal use only**. Respect website terms of service when scraping content.

---

## 🪪 License

Free to use, modify, and learn from — no strings attached!

---
