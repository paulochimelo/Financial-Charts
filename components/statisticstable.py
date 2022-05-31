from dash import html, dcc, dash_table

from constants.chart import colors


def generate(component_id, title_text=''):
    layout = html.Div(id=component_id, className='dashboard-card', children=[
        dcc.Loading(
            parent_style={'height': '100%',
                          'width': '100%',
                          'overflowX': 'hidden',
                          'overflowY': 'auto',
                          'padding': '1rem'},
            children=[
                html.Div(style={'height': '100%', 'width': '100%'},
                         children=[
                             html.H2(title_text),

                             html.Div(id=component_id+'-rows', className='table__rows')
                ])
            ])
    ]),

    return layout[0]
