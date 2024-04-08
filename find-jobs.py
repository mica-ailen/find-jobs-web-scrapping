import requests 
from bs4 import BeautifulSoup
import csv

def find_jobs():
    html_text = requests.get('https://www.jobindex.dk/jobsoegning/koebenhavn?q=python').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_='PaidJob')

    #Open the CSV file in write mode
    with open('jobs.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Company Name', 'Location', 'Publish date', 'More info'])

        for job in jobs:
            published_date = job.find('time').text
            if "04" in published_date:
                company_name = job.find('div', class_='jix-toolbar-top__company').text.strip()
                location_company = job.find('span', class_='jix_robotjob--area').text.strip()
                more_info = job.h4.a['href']

                writer.writerow([company_name, location_company, published_date, more_info])

                print(f'Company Name: {company_name}')
                print(f'Location: {location_company}')
                print(f'Publish date: {published_date}')
                print(f'More info: {more_info}')
                print('')

find_jobs()
