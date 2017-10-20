import sys
import re
import csv
import requests
from bs4 import BeautifulSoup as bs

if __name__=='__main__':
    tickers_file = sys.argv[1]
    csv_file = sys.argv[2]

    
def scrape_data(ticker):
   
    with open(tickers_file) as fin:
        for line in fin:
            ticker = line.strip()
            url = "https://www.sec.gov/cgi-bin/browse-edgar?CIK=%s" % (ticker)
            resp = requests.get(url)
            soup = bs(resp.text, "html.parser")
            company_tag = soup.find('span', attrs={'class' : 'companyName'})
            company_name = company_tag.text.split('CIK#')[0].strip()
            ident_tag = soup.find('p', attrs={'class':'identInfo'})
            sic = ident_tag.find('a')
            
            return(company_name, )
