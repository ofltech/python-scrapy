# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscraperItem(scrapy.Item):
    """
    Default class for scraped items.
    """

    # define the fields for your item here like:
    name = scrapy.Field()
    pass


def serialize_price(value):
    """
    Serialize price function for fixing the price symbol.
    """
    return f"£ {str(value)}"


class BookItem(scrapy.Item):
    """
    BookItem class for scraped items.
    """

    url = scrapy.Field()
    title = scrapy.Field()
    upc = scrapy.Field()
    product_type = scrapy.Field()
    price_excl_tax = scrapy.Field()
    price_incl_tax = scrapy.Field()
    tax = scrapy.Field()
    availability = scrapy.Field()
    num_reviews = scrapy.Field()
    stars = scrapy.Field()
    category = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
