import sqlite3


class WoolScraperPipeline:

    def __init__(self):
        self.connection = sqlite3.connect("Wools.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS wools_tb""")
        self.cursor.execute("""CREATE table wools_tb(name text, price text, needle_size text, composition text)""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.cursor.execute("""INSERT INTO wools_tb VALUES(?,?,?,?)""", (
            item["name"],
            item["price"],
            item["needle_size"],
            item["composition"]
        ))
        self.connection.commit()
