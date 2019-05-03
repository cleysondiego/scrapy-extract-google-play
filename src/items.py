from scrapy.item import Item, Field


class ScrapyextractgoogleplayItem(Item):
    name = Field()
    developer = Field()
    link_developer = Field()
    category = Field()
    rate = Field()
    rating = Field()
    downloads = Field()
