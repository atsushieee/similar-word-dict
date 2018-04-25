''' Word List '''
from logging import getLogger
import sqlite3

DB_FILE_PATH = './db/word_ranking/all.db'
log = getLogger('app')


class WordList():
    '''
    Extracting frequency of words
    '''
    def __init__(self):
        self.counterDict = {}
        self.DB_PATH = DB_FILE_PATH
        self.conn = sqlite3.connect(self.DB_PATH)

    def find_by_name(self, name):
        """
        Extract the record applied to word from database
        :param name: word of which you would like to know the frequency.
        """
        cur = self.conn.cursor()

        query = "select name, frequency from words where name=?"
        result = cur.execute(query, (name,))
        word = result.fetchone()
        log.debug('%s: fetch the record', name)
        return word

    def get(self, wordArray):
        """
        Get the records of word's information(name, frequency)
        :param wordArray: Array of words which you would like to know the frequency of.
        """
        counters = []
        for word in wordArray:
            try:
                counter = self.find_by_name(word)
            except RuntimeError:
                return {"message": "server error!!"}, 500

            if counter is not None:
                counters.append({'name': counter[0], 'frequency': counter[1]})

        self.conn.close()
        log.info('%s: matched results', counters)
        return counters


if __name__ == '__main__':
    testArray = ['夏', '素材', '鮮やかな']
    wordList = WordList()
    wordCount = wordList.get(testArray)
    print(wordCount)
