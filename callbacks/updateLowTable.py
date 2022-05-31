from dash import Input, Output, State, callback, dash, html
import pandas as pd

from components import statisticsrows

@callback(
    Output(component_id='table-low-rows', component_property='children'),
    Input(component_id='df_store', component_property='data')
)
def update_low_avg(df):
    if not df:
        raise dash.exceptions.PreventUpdate

    dff = pd.read_json(df)
    lowCol = dff['low']

    return statisticsrows.generate('low', lowCol)