import logging

def add_manual_error_log(file):
    logging.basicConfig(filename=file, level=logging.INFO)

def report(e:Exception):
    logging.exception(str(e))
