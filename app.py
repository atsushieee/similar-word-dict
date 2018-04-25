''' Flask '''
import os
from logging import getLogger, config
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import yaml
from resources.word import Word

# logger setup
root_file_path = os.path.abspath(os.path.dirname(__file__))
conf_params = yaml.load(open("./log/log_conf.yml").read())
conf_params['handlers']['fileHandler']['filename'] = root_file_path + conf_params['handlers']['fileHandler']['filename']
config.dictConfig(conf_params)
log = getLogger('app')

# app setup
app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(Word, '/word/<string:word>')

if __name__ == '__main__':
    log.debug('app start')
    app.run(port=5000, debug=False, threaded=True)
