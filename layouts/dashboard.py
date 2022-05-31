from dash import dcc, html

from constants.chart import intervals
from components import candlechart, datatable, dropdown, statisticstable

layout = html.Main(
    className='app-page',
    children=[
        html.Div(
            className='app-page-container',
            children=[
                html.Div(className='filters',
                         children=[
                             dropdown.generate(
                                 component_id='symbol', label_text='Sigla da ação'),

                             html.P(className='error-message',
                                    id='error-symbol'),

                             dropdown.generate(component_id='timeseries', label_text='Intervalo de tempo', options=list({
                                 'label': interval['title'],
                                 'value': interval['key']
                             } for interval in intervals)),

                             html.Button(
                                 className='button-primary',
                                 children=[
                                     html.I(className='icon fa-solid fa-arrow-rotate-right'),
                                     'Atualizar'
                                     ],
                                 n_clicks=0,
                                 id='refresh'),
                         ]),
                html.Div(className='dashboard',
                         children=[
                             candlechart.generate(
                                 'stock-close', 'Fechamento por período'),

                             candlechart.generate(
                                 'stock-open', 'Abertura por período'),

                             dcc.Store(id='df_store'),

                             statisticstable.generate(
                                 'table-open',
                                 'Estatísticas de abertura'),

                             statisticstable.generate(
                                 'table-close',
                                 'Estatísticas de fechamento'),

                             statisticstable.generate(
                                 'table-high',
                                 'Estatísticas de altas'),

                             statisticstable.generate(
                                 'table-low',
                                 'Estatísticas de baixas'),
                         ])
            ]
        )]
)
