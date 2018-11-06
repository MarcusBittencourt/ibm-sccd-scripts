'''
    Esse script tem como objetivo criar logs automaticamente.
'''
import sys
sys.path.append('__pyclasspath__/Lib')

from psdi.mbo import MboConstants
from psdi.server import MXServer
from datetime import datetime, timedelta
from psdi.util.logging import MXLoggerFactory

logger = MXLoggerFactory.getLogger("maximo.script")

def create_worklog(logtype, summary, message, attributes, clientviewable):
    worklogset = mbo.getMboSet('WORKLOG')
    worklogentry = worklogset.add()
    logger.debug('Criando o registro do worklog ...')
    worklogentry.setValue('clientviewable', clientviewable, MboConstants.NOACCESSCHECK)
    worklogentry.setValue('logtype', logtype)
    worklogentry.setValue('description', summary.decode("utf-8"), MboConstants.NOACCESSCHECK)
    values = [mbo.getString(attribute) for attribute in attributes]
    send = message.decode('utf-8') % (tuple(values))
    logger.debug('Montando mensagem principal do registro de log ...')
    worklogentry.setValue('DESCRIPTION_LONGDESCRIPTION', send, MboConstants.NOACCESSCHECK)
    logger.debug('Registro automático do worklog de realizado!')

def init():
    logger.debug('Inicializando registro automático do worklog de realizado')
    by = {
    'LPEXAMPLE1': 
        lambda: create_worklog('CLIENTNOTE', 'Observação do Cliente', 'Solicito a analise preliminar para a referida demanda.', [], 1)
    'LPEXAMPLE2': 
        lambda: create_worklog('UPDATE', 'Atualização', 'Formalizo o encaminhamento do orçamento para análise', [], 1)
    'LPEXAMPLE3': 
        lambda: create_worklog('WORK', 'Atualização', 'O serviço foi inicializado', [], 1)
    }
    by[launchPoint]()

init()