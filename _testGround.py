import logging

logging.basicConfig(format='%(asctime)s [line:%(lineno)d] - %(levelname)s: %(message)s',
 level=logging.DEBUG)

logging.debug('debug information')
logging.info('info')
logging.warning('warning information')
logging.error('error information')
logging.critical('critical information')
