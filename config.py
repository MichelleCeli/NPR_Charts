
import configparser
import json

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = config['Spreadsheet']['api_id']
api_hash = config['Spreadsheet']['api_hash']
document = config['Spreadsheet']['document_id']

def config_document():
    return document