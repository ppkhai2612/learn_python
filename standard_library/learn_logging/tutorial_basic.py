import logging

# 1. Log events to the console
# logging.warning('Watch out!') # will print a message to the console
# logging.info('I told you so') # will not print anything

# 2. Log events to a file
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

# logger = logging.getLogger(__name__)
# logger.debug('This message should go to the log file')
# logger.info('So should this')
# logger.warning('And this, too')
# logger.error('And non-ASCII stuff, too, like Øresund and Malmö')

# 3. Change the log message format
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
# logging.debug('This message should appear on the console')
# logging.info('So should this')
# logging.warning('And this, too')

# 4. Displaying the date/time in messages
logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')
