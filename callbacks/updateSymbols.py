import functools
from dash import Output, Input, exceptions, callback
from config import api

@functools.lru_cache(maxsize=32)
@callback(
    Output(component_id='symbol', component_property='options'),
    Output(component_id='error-symbol', component_property='children'),
    Input(component_id='symbol', component_property='search_value'))
def update_symbol(symbolValue):
    if symbolValue is None or len(symbolValue) < 1:
        raise exceptions.PreventUpdate

    params = {
        'function': 'SYMBOL_SEARCH',
        'keywords': symbolValue,
        'datatype': 'json',
    }

    data = api.get('/query', params=params)

    if 'bestMatches' not in data:
        errors = list(data.values())
        return [], 'Error: ' + errors[0]

    bestMatches = data['bestMatches']

    options = list([
        {
            'label': symbol['1. symbol'] + ' - ' + symbol['2. name'],
            'value': symbol['1. symbol']
        } for symbol in bestMatches])

    return options, ''