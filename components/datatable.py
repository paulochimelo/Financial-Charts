from dash import html, dcc, dash_table

from constants.chart import colors


def generate(component_id, title_text = ''):
    layout = html.Div(className='dashboard-card', children=[
        dcc.Loading(
            parent_style={'height': '100%',
                          'width': '100%', 'overflow': 'hidden'},
            children=[
                html.Div(className='table',
                         style={'height': '100%', 'width': '100%'},
                         children=[
                             html.H2(title_text),
                             dash_table.DataTable(id=component_id,
                                                  page_size=25,
                                                  style_header={
                                                      'backgroundColor': colors['plot_bgcolor'],
                                                      'color': colors['font_color']
                                                  },
                                                  style_data={
                                                      'backgroundColor': 'var(--bg-card-color)',
                                                      'color': colors['font_color']
                                                  },
                                                  style_table={
                                                      'overflowY': 'auto',
                                                      'overflowX': 'hidden',
                                                      'height': '100%',
                                                      'width': '100%'},
                                                  style_cell={
                                                      'overflow': 'hidden',
                                                      'textOverflow': 'ellipsis',
                                                      'maxWidth': '1fr',
                                                  })
                         ])
            ])
    ]),

    return layout[0]
