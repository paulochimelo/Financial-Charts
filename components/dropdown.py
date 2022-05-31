from dash import html, dcc


def generate(component_id, label_text, options=[]):
    return html.Div(className='filter',
        children=[
        html.Label(
            children=label_text),
        dcc.Dropdown(
            id=component_id,
            options=options
        )])
