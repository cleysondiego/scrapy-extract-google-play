from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
import items


class ScrapyExtractGooglePlaySpider(CrawlSpider):
    name = "ScrapyExtractGooglePlay_crawler"
    allowed_domains = ['play.google.com']
    start_urls = ['https://play.google.com/store/apps']

    NAME_SELECTOR = '.AHFaub span::text'
    DEVELOPER_SELECTOR = '.i4sPve a::text'
    DEVELOPER_LINK_SELECTOR = '//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/span[1]/a/@href'
    CATEGORY_SELECTOR = '//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/span[2]/a//text()'
    RATE_SELECTOR = '//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div/div[2]/c-wiz/div/div/@aria-label'
    RATING_SELECTOR = '//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div/div[2]/c-wiz/span/span[1]/@aria-label'
    DOWNLOADS_SELECTOR = '//*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/div/div[1]/div/c-wiz[3]/div[1]/div[2]/div/div[3]/span/div/span/text()'

    rules = (
        Rule(LinkExtractor(allow=('store/apps/details')), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info(f'Extracting ... {response.url}')
        item = items.ScrapyextractgoogleplayItem()
        item['name'] = response.css('.AHFaub span::text').get()
        item['developer'] = response.css('.i4sPve a::text').get()
        item['link_developer'] = response.xpath(
            '//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/span[1]/a/@href').get()
        item['category'] = response.xpath(
            '//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/span[2]/a//text()').get()
        item['rate'] = response.xpath(
            '//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div/div[2]/c-wiz/div/div/@aria-label').get()
        item['rating'] = response.xpath(
            '//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div/div[2]/c-wiz/span/span[1]/@aria-label').get()
        item['downloads'] = response.xpath(
            '//*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/div/div[1]/div/c-wiz[3]/div[1]/div[2]/div/div[3]/span/div/span/text()').get()
        return item
