''' .csv -> .db '''
import csv
import sqlite3

CSV_FILE_PATH = '../csv/word_ranking/all.csv'
DB_FILE_PATH = CSV_FILE_PATH.replace('csv', 'db')


def create_table(dbFile):
    """
    Create table if there is not 'words' table in database
    :param dbFile: Name of database
    """
    conn = sqlite3.connect(dbFile)
    cur = conn.cursor()
    query = 'CREATE TABLE IF not EXISTS words (id INTEGER PRIMARY KEY, name text, frequency INTEGER)'
    cur.execute(query)
    conn.commit()
    conn.close()


def retrieve_csv_data(csvFile):
    """
    retrieve csv data
    :param csvFile: Name of csv file
    """
    words_list = []
    with open(csvFile, newline='', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            words_list.append(row)
    return words_list


def add_dict(dbFile, words_counter):
    """
    insert records of (word, counter) list
    :param dbFile: Name of database
    :param words_counter: List of word's name and frequency
    """
    conn = sqlite3.connect(dbFile)
    cur = conn.cursor()
    for counter in words_counter:
        query = 'INSERT INTO words VALUES (NULL, ?, ?)'
        cur.execute(query, counter)
    conn.commit()
    conn.close()


# Unit test
if __name__ == '__main__':
    create_table(DB_FILE_PATH)
    words_counter_test = retrieve_csv_data(CSV_FILE_PATH)
    add_dict(DB_FILE_PATH, words_counter_test)
