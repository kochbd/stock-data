import requests
import csv
from bs4 import BeautifulSoup

def stock_spider(max_pages):
    page = 65
    squares = []
    while page <= max_pages:
        url = 'http://www.nasdaq.com/screening/companies-by-name.aspx?letter=' + str(chr(page))
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html5lib")
        for link in soup.findAll('a', href=True):
            blah = str(link['href'][:-4])
            if blah == 'http://www.nasdaq.com/symbol/' or blah == 'http://www.nasdaq.com/symbol':
                squares.append(link['href'][len('http://www.nasdaq.com/symbol/'):])
        page += 1
    squares.sort()
    seen = {}
    with open('companyList.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        for stock in squares:
            if stock in seen: continue
            seen[stock] = 1
            print(stock)
            csvwriter.writerow([stock])


stock_spider(90)
