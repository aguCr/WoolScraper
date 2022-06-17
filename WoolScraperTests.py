import unittest
import WoolScraper.WoolScraper.spiders.WoolSpider as Ws


class TestWoolSpider(unittest.TestCase):

    # tests if the passed arguments for the dict are processed correctly
    def test_add_wool_for_scrapper(self):
        wools = {}
        expected_result = {"durable": ["durable-colour-cake", "durable-norwool-plus"]}  # lowercase and hyphen
        unexpected_result = {"Durable": ["Durable colour Cake", " Durable- norwool plus "]}  # upper cases, whitespaces
        # at start/end, between words

        Ws.add_wool_for_scraper(wools, "DURABLE",
                                ["Durable Colour Cake", "Durable-Norwool-Plus"])  # uppercase
        self.assertEqual(wools, expected_result)

        Ws.add_wool_for_scraper(wools, "Durable",
                                ["Durable colour cake",
                                 " Durable norwool plus "])  # whitespaces between words
        self.assertEqual(wools, expected_result)

        Ws.add_wool_for_scraper(wools, " Durable ",
                                [" durable-colour-cake ",
                                 " durable-norwool-plus "])  # whitespaces at beginning and end
        self.assertEqual(wools, expected_result)

        Ws.add_wool_for_scraper(wools, " DUrable ",
                                [" durable colour cake ",
                                 "durable norwool Plus "])  # everithing wrong
        self.assertEqual(wools, expected_result)

        Ws.add_wool_for_scraper(wools, "Durable",
                                ["Durable colour Cake", " Durable- norwool plus "])  # unexpected
        self.assertNotEqual(wools, unexpected_result)

    def test_create_search_query(self):
        wools = {}
        url = "https://www.wollplatz.de/{}"
        Ws.add_wool_for_scraper(wools, "DMC", ["Natura XL"])
        Ws.add_wool_for_scraper(wools, "Drops", ["Safran", "Baby Merino Mix"])
        Ws.add_wool_for_scraper(wools, "Hahn", ["Alpacca Speciale"])
        Ws.add_wool_for_scraper(wools, "Stylecraft", ["Special dk"])

        expected_result = ["https://www.wollplatz.de/wolle/dmc/dmc-natura-xl",
                           "https://www.wollplatz.de/wolle/drops/drops-safran",
                           "https://www.wollplatz.de/wolle/drops/drops-baby-merino-mix",
                           "https://www.wollplatz.de/wolle/hahn/hahn-alpacca-speciale",
                           "https://www.wollplatz.de/wolle/stylecraft/stylecraft-special-dk"]

        result = list(Ws.create_search_queries(wools, url))
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
