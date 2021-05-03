# This code works in scrapy shell to create the same output of urls that the scrapy spider outputs

import re
import csv
a = 'https://freshairarchive.org/sitemap.xml?page='

for i in range(1,25):
  fetch(a + str(i))
  response.selector.register_namespace('n','http://www.sitemaps.org/schemas/sitemap/0.9')
  urllist = response.xpath('//n:loc/text()').extract()
  r = re.compile('.*guests')
  matchlist = list(filter(r.match,urllist))
  with open('method2.csv', 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows([value] for value in matchlist)

