from dash import html

layout = html.Header(children=[
    html.Div(
        className='app-header',
        children=[
            html.Div(
                className='app-logo',
                children=[
                    html.I(className='icon fa-solid fa-fan'),
                    'Financial Charts'
                    ])
        ])
])
