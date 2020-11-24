#%%
from loguru import logger

#%%

logger.add('logfile.log', level='INFO', format='{name}: {level} & {time} -- {message}')


logger.debug('some log')
logger.info('another log')

import os

os.getcwd()
