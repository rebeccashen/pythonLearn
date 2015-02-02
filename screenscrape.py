__author__ = 'rebeccas'

import os
import time
import csv
import urllib2


from bs4 import BeautifulSoup

field_order = ['date', 'last_trade', 'change', 'ah_price', 'ah_change']

fields = {'date': 'Date',
          'last_trade': 'Last Trade',
          'change': 'Change',
          'ah_price': 'After Hours Price',
          'ah_change': 'After Hours Change'}

def write_row(ticker_name, stock_values):
    print "stock_values @ write_row", stock_values

    file_name = "stocktracker -" + ticker_name + ".csv"
    if os.access(file_name, os.F_OK):
        file_mode = 'ab'
    else:
        file_mode = 'wb'

    csv_writer = csv.DictWriter(
        open(file_name, file_mode),
        fieldnames =field_order,
        extrasaction = 'ignore')

    if file_mode == 'wb':
        csv_writer.writerow(fields)
    csv_writer.writerow(stock_values)

def get_web_html(site_name):
    opener = urllib2.build_opener(
        urllib2.HTTPRedirectHandler(),
        urllib2.HTTPHandler(debuglevel=0),
        )

    opener.addheaders = [
        ('User-agent', "Mozilla/4.0 (compatible; MSIE 7.0; "
                       "Windows NT 5.1; .NET CLR 2.0.50727; "
                       ".NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)")
    ]

    url = "http://www.emenar.com"
    response = opener.open(url)
    return ''.join(response.readlines())


def get_stock_html(ticker_name):
    opener = urllib2.build_opener(
        urllib2.HTTPRedirectHandler(),
        urllib2.HTTPHandler(debuglevel=0),
)

    opener.addheaders = [
        ('User-agent', "Mozilla/4.0 (compatible; MSIE 7.0; "
        "Windows NT 5.1; .NET CLR 2.0.50727; "
        ".NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)")
    ]

    url = "http://finance.yahoo.com/q?2=" + ticker_name
    response = opener.open(url)
    return ''.join(response.readlines())


def find_quote_section(html):
   #  soup = BeautifulSoup(html)
   #
   # ## quote = soup.find('div', attrs = {'class':'yfi_quote_summary'})
   #  print "at class yfi quote summary"
   #
   #  quote = soup.findAll('div', attrs = {'class':'yfi_quote_summary'})
   #  print quote
   #
   #  return quote


   soup = BeautifulSoup(html)
   print "soup is tasty"
   quote = soup._find_all('div')
   quote = soup.find_all('div', "class")

##   quote = soup.find_all('class')
##   quote = soup.find_all('div', attrs = {'class': 'yfi_quote_summary'})

   return quote

def parse_stock_html(html, ticker_name):
    quote = find_quote_section(html)
    result = {}
    tick = ticker_name.lower()

    print tick

    #<h2>Google Inc.</h2>
    result['stock_name'] = quote.find('h2')
    print "Quote --"
    print quote

    ### After hours value
    #<span id= "yfs_l91_goog">329.94</span>
    result['ah_price'] = quote.find('span',
        attrs={'id': 'yfs_l91_'+tick}).string
    #<span id = "yfs_z08_goog">
    #   <span class="yfi-price-change-down">0.22</span>
    result['ah_change'] = quote.find(
        attrs= {'id': 'yfs_z08_'+tick}).contents[1]

    ### Current Values
    #<span id="yfs_l10_goog">330.16</span>
    result['last_trade'] = quote.find(
        'span', attrs={'id': 'yfs_l10_'+tick}).string

    #<span id+'yfs_c0_goog" class="yfi_quote_price">
    #   <span class= "yfi-price-change-down">1.06</span>
    return result

def is_price_change(value):
    return(value is not None and
        value.strip().lower()
        .startswith('yfi-price-change'))


if __name__ == '__main__':
    html = get_stock_html('GOOG')
    ##html = get_web_html('emenar')
    quote = find_quote_section(html)
    print "Hello"
    print quote


##    write_row('GOOG', quote)


##    stock = parse_stock_html(html, 'GOOG')
##    write_row('GOOG', stock)
##    print "Hello"
##    print stock


# result['change'] = (
#     quote.find(attrs={'id':'yfs_c10_'+tick})
#     .find(attrs={'class': is_price_change})
#     .string)
# return result

