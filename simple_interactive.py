# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 17:49:54 2021

@author: linjianing
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H6('change the value in the text box to see call backs in action!'),
    html.Div([
        'Input', dcc.Input(id='my-input', value='initial value', type='text')]),
    html.Br(),
    html.Div(id='my-output'),])
@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value'))
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
