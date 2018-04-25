''' wordNet '''
from collections import namedtuple
from logging import getLogger
import sqlite3
import sys

log = getLogger('app')


class WordNet:
    """
    WordNet Class
    """
    def __init__(self):
        self.DB_PATH = "./db/wnjpn.db"

        self.wordInfo = namedtuple('Word', 'wordid lang lemma pron pos')
        self.senseInfo = namedtuple('Sense', 'synset wordid lang rank lexid freq src')
        self.synsetInfo = namedtuple('Synset', 'synset pos name src')
        # refer to wordNet DB
        self.conn = sqlite3.connect(self.DB_PATH)

    def getWords(self, lemma):
        """
        get words' information of wordNet
        :param lemma: word
        """
        cur = self.conn.execute("select * from word where lemma=?", (lemma,))
        return [self.wordInfo(*row) for row in cur]

    def getSense(self, wordid):
        """
        get sense' information of wordNet
        :param wordid: word's id of wordNet
        """
        cur = self.conn.execute("select * from sense where wordid=?", (wordid,))
        return [self.senseInfo(*row) for row in cur]

    def getSynset(self, synset):
        """
        get synsets' information of wordNet
        :param synset: synset's number of wordNet
        """
        cur = self.conn.execute("select * from synset where synset=?", (synset,))
        return self.synsetInfo(*cur.fetchone())

    def getWordsInfoFromSynset(self, synset, lang):
        """
        get words' information from a synset number
        :param synset: synset's number of wordNet
        :param lang: language
        """
        cur = self.conn.execute("select word.* from sense, word where synset=? and word.lang=? and sense.wordid = word.wordid;", (synset, lang))
        return [self.wordInfo(*row) for row in cur]

    def getWordsFromSenses(self, sense):
        """
        get words' information from a synset number
        :param sense
        """
        synonym = {}
        for s in sense:
            lemmas = []
            syns = self.getWordsInfoFromSynset(s.synset, s.lang)
            for syn in syns:
                lemmas.append(syn.lemma)
            synonym[self.getSynset(s.synset).name] = lemmas
        return synonym

    def getSynonym(self, word):
        """
        get array of synoym words
        :param word: base word
        """
        log.info('%s: search word', word)
        synonymDict = {}
        synonymArray = []
        wordsInfo = self.getWords(word)
        if wordsInfo:
            for w in wordsInfo:
                sense = self.getSense(w.wordid)
                s = self.getWordsFromSenses(sense)
                # synonymDict = dict(list(synonymDict.items()) + list(s.items()))
                for key, val in s.items():
                    synonymDict[key] = val if key not in synonymDict else synonymDict[key] + val
        for values in synonymDict.values():
            for val in values:
                synonymArray.append(val)
        synonymArray = list(set(synonymArray))
        log.info('%s: synonym words', synonymArray)
        return synonymArray


# Unit test
if __name__ == '__main__':
    wordnet = WordNet()
    if len(sys.argv) >= 2:
        synonymWords = wordnet.getSynonym(sys.argv[1])
        print(synonymWords)
    else:
        print("You need at least 1 argument as a word like below.\nExample:\n  $ python3 wordNet.py 楽しい")
