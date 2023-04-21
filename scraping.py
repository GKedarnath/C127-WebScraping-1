from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

start_url = "https://en.wikipedia.org/wiki/list_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("chromedriver.exe")

browser.get(start_url)

time.sleep(10)

def scrape():
    headers = ["Name", "Distance", "Mass", "Radius"]
    planet_data = []
    for i in range(0, 5):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        tr_tags = soup.find_all("tr", attrs={"class", "wikipedia"})
        for tr_tag in tr_tags:
            td_tags = tr_tag.find_all("td")
            temp_list = []
            for index, td_tag in enumerate(td_tags):
                if index == 0:
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
 
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()
 