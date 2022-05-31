from dash import Dash, html, Input, Output, exceptions
import plotly.graph_objects as go
import pandas as pd
import functools
import requests_cache
import requests
from dotenv import load_dotenv
import os

from constants.api import APP_TITLE, BASE_URL, CACHE_EXPIRATION
from callbacks import (
    updateCandleClose,
    updateOpenTable,
    updateDataFrame,
    updateCloseTable,
    updateHighTable,
    updateLowTable,
    updateCandleOpen,
    updateSymbols)
from layouts import dashboard, footer, header
from constants.chart import intervals, EmptyFigure, colors
from constants.env import ICONS_CDN_SCRIPT_URL, APPLICATION_MODE, APPLICATION_MODE_DEBUG

load_dotenv()

external_scripts = [
    {
        'src': os.getenv(ICONS_CDN_SCRIPT_URL),
        'crossorigin': 'anonymous'
    }
]

app = Dash(__name__,
           external_scripts=external_scripts)
app.title = APP_TITLE

requests_cache.install_cache(expire_after=CACHE_EXPIRATION)

app.layout = html.Div(
    className='app',
    children=[
        html.Link(
            rel='preconnect',
            href='https://fonts.googleapis.com'
        ),
        html.Link(
            rel='preconnect',
            href='https://fonts.gstatic.com',
            crossOrigin='1',
        ),
        html.Link(
            href='https://fonts.googleapis.com/css2?family=Poppins:wght@100;400;500;700&display=swap',
            rel='stylesheet',
        ),

        header.layout,

        dashboard.layout,

        footer.layout
    ]
)


@app.callback(
    Output(component_id='timeseries', component_property='value'),
    Input(component_id='symbol', component_property='value'))
def update_default_timeseries(symbolValue):
    if not symbolValue:
        raise exceptions.PreventUpdate

    return intervals[0]['key']


if __name__ == '__main__':
    debug = False
    if os.getenv(APPLICATION_MODE) == APPLICATION_MODE_DEBUG:
        debug = True

    app.server.run(debug=debug, host='0.0.0.0', port=8050)