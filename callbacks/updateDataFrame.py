from dash import Output, Input, callback, exceptions
import pandas as pd
import requests

from repositories.fetchSymbolData import fetchSymbolData

@callback(
    Output(component_id='df_store', component_property='data'),
    Input(component_id='timeseries', component_property='value'),
    Input(component_id='symbol', component_property='value'),
    Input(component_id='refresh', component_property='n_clicks'))
def update_data_frame(timeseriesValue, symbolValue, n_clicks):
    if not timeseriesValue or not symbolValue:
        raise exceptions.PreventUpdate

    try:
        data = fetchSymbolData(symbolValue, timeseriesValue)
        if data is None:
            raise exceptions.PreventUpdate

        dataKeys = list(data.keys())
        timeSeriesDataSet = data[dataKeys[1]]

        df = pd.DataFrame({
            'timestamp': timeSeriesDataSet.keys(),
            'open': [float(timeSeriesDataSet[timeSeries]['1. open']) for timeSeries in timeSeriesDataSet],
            'high': [float(timeSeriesDataSet[timeSeries]['2. high']) for timeSeries in timeSeriesDataSet],
            'low': [float(timeSeriesDataSet[timeSeries]['3. low']) for timeSeries in timeSeriesDataSet],
            'close': [float(timeSeriesDataSet[timeSeries]['4. close']) for timeSeries in timeSeriesDataSet],
        })

        return df.to_json()
    except requests.HTTPError:
        return None