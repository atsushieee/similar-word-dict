''' Word '''
from logging import getLogger
from flask_restful import Resource
from resources.wordList import WordList
from modules.wordNet import WordNet

log = getLogger('app')


class Word(Resource):
    '''
    Getting word information (for get API)
    '''
    @classmethod
    def get(cls, word):
        """
        Getting word information (for get API)
        :param db: selected database index
        :param word: input text from input field
        """
        wordNet = WordNet()
        wordArray = wordNet.getSynonym(word)
        wordList = WordList()
        wordCounter = wordList.get(wordArray)
        if wordCounter == {"message": "server error!!"}:
            log.error('!!!!!!server error!!!!!!!')
            return wordCounter, 500
        log.debug('response value from wordList class')
        return {'word': wordCounter}, 200
