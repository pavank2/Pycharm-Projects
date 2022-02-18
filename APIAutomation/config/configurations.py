import configparser
def getconfig():
    config = configparser.ConfigParser()
    config.read('properties.ini')
    return config

def getPassword():
    return "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"