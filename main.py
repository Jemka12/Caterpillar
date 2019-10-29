import scaner
import csv

proxy_headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                               'Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36',
                 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                 'Accept-Encoding': 'gzip, deflate, br',
                 'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                 'Cache-Control': 'no-cache',
                 'Connection': 'keep-alive',
                 'Pragma': 'no-cache',
                 'Upgrade-Insecure-Requests': '1',
                 'DNT': '1',
                 'Sec-Fetch-Mode': 'navigate',
                 'Sec-Fetch-User': '?1',
                 'Sec-fetch-site': 'same-origin'
                 }




with open('cities.txt', 'r', encoding='utf-8') as file_city:
    for city in file_city:
        with open('inquiries.txt', 'r', encoding='utf-8') as file:
            for inquiry in file:
                print(str(inquiry))
                target_url = "https://www.google.ru/search?q=" + city + inquiry #https://www.google.ru/search?q=&tbm=lcl;start:40
                vuln = scaner.Scanner(target_url, inquiry, proxy_headers)
                print(vuln.extract_html("https://www.google.ru/search?q=диваны ОМск&tbm=lcl"))
                vuln.extract_info_google_searchs(target_url,2)
                vuln.record_excel(city.rstrip(),inquiry)

