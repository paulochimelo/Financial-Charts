from dash import html


def generate(id, data_frame):
    statistics = data_frame.describe()

    statistics['mode'] = data_frame.mode()[0]
    statistics['median'] = data_frame.median()

    firstValue = data_frame.iloc[0]
    lastValue = data_frame.iloc[-1]

    percChange = (firstValue/lastValue - 1) * 100

    percChangeStyling = 'field__value--gain'
    percChangeTrendDirection = 'up'
    if firstValue < lastValue:
        percChangeStyling = 'field__value--loss'
        percChangeTrendDirection = 'down'

    statistics['perc_change'] = percChange

    statisticsKeys = list(statistics.keys())

    labelNameMappings = {
        'count': {
            'text': 'Número de cotações',
        },
        'mean': {
            'text': 'Média',
        },
        'mode': {
            'text': 'Moda'
        },
        'median': {
            'text': 'Mediana'
        },
        'std': {
            'text': 'Desvio padrão'
        },
        'min': {
            'text': 'Mínimo'
        },
        '25%': {
            'text': '25%'
        },
        '50%': {
            'text': '50%'
        },
        '75%': {
            'text': '75%'
        },
        'max': {
            'text': 'Máximo'
        },
        'perc_change': {
            'text': 'Resultado percentual',
            'className': percChangeStyling,
            'left': html.I(className='icon fa-solid fa-arrow-trend-{direction}'.format(direction=percChangeTrendDirection))
        }
    }

    rows = [html.Div(
        className='field',
        children=[
            html.Span(id='table-{id}-{key}-label'.format(id=id, key=key),
                      className='field__label',
                      children=labelNameMappings[key]['text']),

            html.Span(id='table-{id}-{key}'.format(id=id, key=key),
                      className='field__value {valueStyling}'.format(valueStyling=labelNameMappings[key].get('className', '')),
                      children=[
                          labelNameMappings[key].get('left', ''),
                          '{:.2f}'.format(statistics[key])
                          ])
        ]
    ) for key in statisticsKeys]

    return rows
