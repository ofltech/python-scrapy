# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    """
    BookscraperPipeline class for data cleaning.
    """
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        # Strip all whitespaces from strings.
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name != "description":
                value = adapter.get(field_name)
                adapter[field_name] = value[0].strip()
        
        # Category and Product Type --> switch to lowercase.
        lowecase_keys = ["category", "product_type"]
        for lowecase_key in lowecase_keys:
            value = adapter.get(lowecase_key)
            adapter[lowecase_key] = value.lower()

        # Price --> convert to float.
        price_keys = ["price", "price_excl_tax", "price_incl_tax", "tax"]
        for price_key in price_keys:
            value = adapter.get(price_key)
            value = value.replace("£", "")
            adapter[price_key] = float(value)
        
        # Availability --> extract number of books in stock.
        availability_string = adapter.get("availability")
        split_string_array = availability_string.split("(")
        if len(split_string_array) < 2:
            adapter["availability"] = 0
        else:
            availability_array = split_string_array[1].split(" ")
            adapter["availability"] = int(availability_array[0])
        
        # Reviews --> convert string to number.
        num_reviews_string = adapter.get("num_reviews")
        adapter["num_reviews"] = int(num_reviews_string)

        # Stars --> convert text to number.
        stars_string = adapter.get("stars")
        split_stars_array = stars_string.split(" ")
        stars_text_value = split_stars_array[1].lower()
        if stars_text_value == "zero":
            adapter["stars"] = 0
        elif stars_text_value == "one":
            adapter["stars"] = 1
        elif stars_text_value == "two":
            adapter["stars"] = 2
        elif stars_text_value == "three":
            adapter["stars"] = 3
        elif stars_text_value == "four":
            adapter["stars"] = 4
        elif stars_text_value == "five":
            adapter["stars"] = 5

        return item
