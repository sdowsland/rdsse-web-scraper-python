
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'staff profile spider'
    start_urls = [
        "http://www.ncl.ac.uk/apl/staff/",
        "http://www.ncl.ac.uk/sacs/staff/",
        "http://www.ncl.ac.uk/nubs/staff/"
    ]

    def parse(self, response):
        for title in response.css('h2.entry-title'):
            yield {'title': title.css('a ::text').extract_first()}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)
