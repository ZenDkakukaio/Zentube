import sqlite3 as sql3


class MyDataLink(object):
    def __init__(self, name_db="Zentube_Database"):

        self.name_db = name_db

    def insert_database(self, link):
        try:

            entity_db = sql3.connect("media/zentube.db")
            print(f"connexion réussie avec --->{self.name_db}")
            entity_cursor = entity_db.cursor()

            query_create_table = """CREATE TABLE IF NOT EXITS link(
                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                                 link TEXT,
                                 

                                 )"""
            entity_db.commit()

            query_insert = """
                            INSERT INTO link(link) VALUES(?)
            """



            value = (link)
            entity_cursor.execute(query_insert, value)

            entity_db.commit()

        except Exception as E:
            print(f"erreur de type--->{E}")
            entity_db.rollback()

        finally:
            entity_db.close()





