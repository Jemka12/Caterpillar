import requests, re
# import urlparse
import csv
from bs4 import BeautifulSoup


class Scanner:
    def __init__(self, url, inquiry, headers):
        self.session = requests.Session()
        self.target_url = url
        self.target_dict = []
        self.headers = headers
        self.inquiry = inquiry

    def extract_html(self, url):
        response = self.session.get(url, headers=self.headers)
        return BeautifulSoup(response.content, features="lxml")

    def extract_links_from(self, url):
        response = self.session.get(url)
        return re.findall(r'(?:href=")(.*?)"', response.content)

    def extract_info_google_searchs(self, url, pages=1):
        for page in range(pages):
            start = "&start=" + str(pages*10)
            self.extract_info_google_search(url+start)

    def extract_info_google_search(self, url):
        parsed_html = self.extract_html(url)
        div = parsed_html.find_all("div", attrs={'class': 'g'})
        for element in div:
            name = element.find('h3').text
            href = element.find('a')['href']
            tel = self.extract_info_sites(href)
            self.target_dict.append({'name': name, 'href': href, 'tel': tel})
        print(self.target_dict)

    def extract_info_sites(self, url):
        parsed_html = self.extract_html(url)
        for element in parsed_html.find_all('a'):
            href = re.search(r'(?:href="tel:)(.*?)"', str(element))
            try:
                return href.group(1)
            except AttributeError:
                pass

    def record_excel(self, city, inquiries):
        file_name = city + '.csv'
        with open(file_name, 'a', newline='') as file_excel:
            a_pen = csv.writer(file_excel, delimiter=';')
            a_pen.writerow(('Запрос=', inquiries))
            a_pen.writerow(('Название компании', 'URL', 'Телефон',))
            for sel in self.target_dict:
                a_pen.writerow((sel['name'], sel['href'], str(sel['tel']) + '`'))
