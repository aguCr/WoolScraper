import scrapy
from ..items import WoolsScraperItem


# this function adds into dict
# formats brand and name of wool to create the query string
# strips leading/ending spaces (if you dont, the url formatter will escape those spaces and the query would fail)
def add_wool_for_scraper(wools, brand, names):
    f_names = []
    for name in names:
        name = name.lower().lstrip(" ").rstrip(" ").replace(" ", "-")
        f_names.append(name)
    wools[brand.lower().lstrip(" ").rstrip(" ")] = f_names


# creates search queries for all values inside the lists in the dict. (all names of wool products)
def create_search_queries(wools, url) -> [str]:
    query = []
    for wool in wools:
        for brand in wools[wool]:
            query.append((url.format("wolle/" + wool + "/" + wool + "-" + brand)))
    return query


class WoolSpider(scrapy.Spider):
    name = "wool"
    url = "https://www.wollplatz.de/{}"
    wools = {}

    # you could add more brands + wools to the dict
    add_wool_for_scraper(wools, "DMC", ["Natura XL"])
    add_wool_for_scraper(wools, "Drops", ["Safran", "Baby Merino Mix"])
    add_wool_for_scraper(wools, "Hahn", ["Alpacca Speciale"])
    add_wool_for_scraper(wools, "Stylecraft", ["Special dk"])

    # runs all get request parallel
    def start_requests(self):
        for query in create_search_queries(self.wools, self.url):
            yield scrapy.Request(query)

    # scraps desired content into dict
    def parse(self, response, **kwargs):
        name = response.css("div.variants-title span.variants-title-txt::text").get()
        price = response.css("div#ContentPlaceHolder1_upPricePanel span.product-price-amount::text").get()
        table = response.css("div#pdetailTableSpecs table")
        description = table.css("tr td::text").extract()
        # yield {"tabelle": description}

        item = WoolsScraperItem()
        item['name'] = name
        item['price'] = price

        for index, element in enumerate(description):
            if element == "Nadelstärke":
                item['needle_size'] = description[index + 1]
            if element == "Zusammenstellung":
                item['composition'] = description[index + 1]
        yield item
