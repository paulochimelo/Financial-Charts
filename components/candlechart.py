from dash import html, dcc

from constants.chart import EmptyFigure


def generate(component_id, title_text):
    return html.Div(className='dashboard-card',
                children=[
                html.Div(className='chart',
                    children=[
                        html.H2(
                            children=title_text),

                        dcc.Loading(
                            id='loading-' + component_id,
                            parent_style={
                                'overflow': 'hidden', 'display': 'flex'},
                            children=[
                                dcc.Graph(
                                    id=component_id,
                                    style={'flex': 1},
                                    figure=EmptyFigure),
                            ]
                        ),

                        html.P(className='error-message',
                               id='error-' + component_id),
                ])
            ])
