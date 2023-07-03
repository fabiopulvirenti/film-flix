import sqlite3 as sql
import logging

class sql_handling():

    cursor=" "
    my_conn=" "

    def __init__(self,database):

      with sql.connect(database) as self.my_conn:
          # print(self.my_conn)
          self.cursor=self.my_conn.cursor()


    def sql_execute(self,query):
        self.cursor.execute(query)
        self.my_conn.commit()


    def select_data(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def select_data_one(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchone()

def retrieve_all_movies():
    connector = sql_handling("filmflix.db")
    all_record=connector.select_data("SELECT * FROM tblFilms")

    for i in all_record:
        print(i)

    return all_record

def retrieve_one_movie(id):
    connector = sql_handling("filmflix.db")
    one_record=connector.select_data_one(f"SELECT * FROM tblFilms WHERE filmID={id}")

    logging.info('Record retrieved: %s', one_record)

    return one_record


def insert_movie(title,yearReleased,rating,duration,genre):
    connector = sql_handling("filmflix.db")

    insert_command=f"INSERT INTO tblFilms (title,yearReleased,rating,duration,genre) VALUES ('{title}',{yearReleased},'{rating}',{duration},'{genre}');"

    connector.sql_execute(insert_command)

def delete_record(filmID):
    connector = sql_handling("filmflix.db")
    delete_one_record= f"DELETE FROM tblFilms WHERE filmID={filmID}"

    connector.sql_execute(delete_one_record)


def update_record(title, yearReleased, rating, duration, genre,filmId):
    connector = sql_handling("filmflix.db")
    update_command = f"UPDATE tblFilms SET title='{title}',yearReleased={yearReleased},rating='{rating}',duration={duration},genre='{genre}' WHERE filmID={filmId}"
    connector.sql_execute(update_command)

