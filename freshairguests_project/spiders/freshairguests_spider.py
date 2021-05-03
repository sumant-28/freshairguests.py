from scrapy.spiders import SitemapSpider

import scrapy


class FreshairguestsSpiderSpider(SitemapSpider):
    name = 'freshairguests_spider'

    sitemap_urls = ['https://freshairarchive.org/sitemap.xml']
    sitemap_rules = [('guests', 'parse_article')]

    def parse_article(self, response):
        print('parse_article url:', response.url)

        yield {'url': response.url}

# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',

    # save in file as CSV, JSON or XML
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'method1.csv', # 
})
c.crawl(FreshairguestsSpiderSpider)
c.start()
