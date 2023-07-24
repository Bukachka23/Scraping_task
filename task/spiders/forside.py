import scrapy


class ForsideSpider(scrapy.Spider):
    name = "forside"
    allowed_domains = ["djursbo.dk"]
    start_urls = ["https://djursbo.dk/"]

    async def parse(self, response):

        print("procesing:"+response.url)
        # Data extraction using CSS selectors
        description=response.css('p::text').extract()
        title=response.css('h::text').extract()

        # Data extraction using xpath
        order=response.xpath("//span[pull-left]/text()").extract()
        price=response.xpath("//span[@pull-right and rend bg-binding]/text()").extract()

        row_data=zip(description,title,order,price)

        # Extracting string data
        for item in row_data:
            # Create a dictionary to store the extracted information
            scraped_info = {
                'page': response.url,
                'description': item[0],
                'title': item[1],
                'order': item[2],
                'price': item[3],
            }

            # Generate cleared information for scraping
            yield scraped_info
