from config import api
from constants.chart import intervals

def fetchSymbolData(symbol, timeSeries):
    params = {
        'function': [interval['key'] for interval in intervals if interval['key'] == timeSeries][0],
        'symbol': symbol.lower(),
        'outputsize': 'compact',
        'datatype': 'json',
    }

    data = api.get('/query', params)

    return data