import scrapy

# Spider subclass to scrape quotes from URLs
class QuotesSpider(scrapy.Spider): 
    name = "quotes" #unique name for scrapy to identify
    start_urls = [ # define URLs to crawl
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/'
    ]
    
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first()
                'author': quote.css('small.text::text').extract_first()
                'tags': quote.css('a.tags::text').extract_first()
            }