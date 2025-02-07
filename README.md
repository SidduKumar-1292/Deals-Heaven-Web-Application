# 🛍️ DealsHeaven Web Application

**DealsHeaven Web Application** is a project that scrapes product deals from [DealsHeaven](https://dealsheaven.in) and displays them in an interactive web interface using Streamlit.

---

## 📌 **Project Overview**

### **🔹 Components:**
1. **Async Web Scraper:**
   - Uses `aiohttp` and `BeautifulSoup` for fast, concurrent scraping.
   - Extracts product details such as **title, price, discount, and link**.
   - Saves data in **CSV format** for further use.

2. **Streamlit UI:**
   - Provides an interactive interface for users to **search and view deals**.
   - Filters deals by **store, category, and deal type**.
   - Displays deals in a visually appealing grid with images and links.

---

## 🚀 **Features**
✅ **Asynchronous Scraping** for faster performance.  
✅ **Interactive UI** with search and filtering options.  
✅ **Supports multiple eCommerce stores** (Flipkart, Amazon, Paytm, etc.).  
✅ **Saves scraped data** for future reference.  
✅ **Easy to deploy** and run locally or on the cloud.  

---

## 📂 **Project Structure**
```
dealsheaven-webapp/
│── scraper/
│   │── async_scraper.py      # Async web scraper
│── streamlit_app/
│   │── app.py                # Streamlit UI
│── data/
│   │── scraped_deals.csv     # Example scraped data
│── README.md                 # Project documentation
```

---

## 🛠 **Installation**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/SidduKumar-1292/dealsheaven-webapp.git
cd Deals-Heaven-Web-Application
```

---

## 🔄 **Running the Async Scraper**
To scrape data and save it to a CSV file:
```bash
cd Scraper
python Hunter.py
```

---

## 🌍 **Running the Streamlit App**
To launch the Streamlit web interface:
```bash
cd streamlit_app
streamlit run app.py
```
This will open the application in your web browser.

---

## 🛠 **Technologies Used**
- **Python** (for scraping and backend processing)
- **aiohttp** (for asynchronous HTTP requests)
- **BeautifulSoup** (for parsing HTML data)
- **Streamlit** (for building the web UI)
- **Pandas** (for data processing and CSV handling)

---

## 🎉 **Contributions & Issues**
- Contributions are welcome! Feel free to fork and submit a pull request.
- If you find any issues, please create a GitHub issue.

---

## 📧 **Contact**
- **GitHub:** https://github.com/SidduKumar-1292
- **Email:** siddukumar1292@gmail.com

🚀 **Enjoy exploring the best deals!** 🛍️

