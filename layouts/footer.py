from dash import html

layout = html.Footer(
    className='app-footer',
    children=[
        html.Div(
            className='app-footer-container',
            children=[
                html.P(
                    className='app-footer-info',
                    children='Copyright 2022, Paulo Chimelo'),
                html.P(
                    className='app-footer-info',
                    children='Powered by Dash'),
            ],
        )
    ]
)
