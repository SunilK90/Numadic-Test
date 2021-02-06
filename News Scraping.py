import scrapy
class PostSpider(scrapy.Spider):
    name = "posts"
    start_url = [
        'www.theguardian.com/au'
    ]

    def parse(self,response):
        page = response.url.split('/')[-1]
        filename = 'posts-%s.html' %page
        with open(filename,'wb') as f:
            f.write(response.body)