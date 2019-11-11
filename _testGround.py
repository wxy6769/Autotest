import logging

logging.basicConfig(
    filename='sample.log',
    format='%(asctime)s [line:%(lineno)d] - %(levelname)s: %(message)s',
    level=logging.DEBUG)

x = 'this is a test.'

logging.debug('debug information: ' + x)
logging.info('info')
logging.warning('warning information')
logging.error('error information')
logging.critical('critical information')
