import requests
from bs4 import BeautifulSoup
import os
import json
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
import schedule
import time


def scrape_weather():
    url = "https://weather.com/weather/today/l/6f8bc8d6316bee49727306c168026d1a60704f23c83a36a11243aaab0f3fe651"
    response = requests.get(url)

    
    # Let requests auto-detect encoding based on response headers
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")

    temp_tag = soup.find("span", class_="CurrentConditions--tempValue--zUBSz")
    condition_tag = soup.find("div", class_="CurrentConditions--phraseValue---VS-k")

    if temp_tag and condition_tag:
        temp = temp_tag.text
        condition = condition_tag.text
        return {
            "temperature": temp,
            "condition": condition,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    else:
        return {
            "error": "Weather data not found. The structure may have changed."
        }


def save_report(data):
    folder_name = datetime.now().strftime("Reports/%Y-%m-%d")
    os.makedirs(folder_name,exist_ok=True)

    report_path = os.path.join(folder_name,"Weather_report.json")
    try:
     with open(report_path,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=2,ensure_ascii=False)
     return report_path
    except (FileExistsError, FileNotFoundError):
       print("File not found or not exist")

def send_email(report_path):
    # Load config
    with open("final_projects/config.json", "r") as file:
        config = json.load(file)

    sender = config["sender"]
    receiver = config["receiver"]
    password = config["password"]

    msg = MIMEMultipart()
    msg["Subject"] = "Daily weather report"
    msg["From"] = sender
    msg["To"] = receiver

    with open(report_path,"r") as report_file:
        report_data = report_file.read()
    body = f"Today's weather report is attached. Data:\n\n{report_data}"
    msg.attach(MIMEText(body,"plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
        server.login(sender,password)
        server.sendmail(sender,receiver,msg.as_string())

def daily_bot():
   wheater_data = scrape_weather()
   report_path = save_report(wheater_data)
   send_email(report_path)
   print("Report Send!")

schedule.every(10).seconds.do(daily_bot)

while True:
    schedule.run_pending()
    time.sleep(1)


