from dash import Output, Input, callback, dash
import pandas as pd
import plotly.graph_objects as go

from constants.chart import colors

@callback(
    Output(component_id='stock-close', component_property='figure'),
    Output(component_id='error-stock-close', component_property='children'),
    Input(component_id='df_store', component_property='data'))
def update_graph(data):
    if not data:
        raise dash.exceptions.PreventUpdate

    df = pd.read_json(data)

    fig = go.Figure(data=[go.Candlestick(
        x=df['timestamp'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close'],
    )])

    fig.update_layout(colors)

    return fig, ''