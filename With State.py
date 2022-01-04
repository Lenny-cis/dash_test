# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 14:10:22 2022

@author: linjianing
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
# import dash_design_kit as ddk

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Input(id='input-1', type='text', value='Montreal'),
    dcc.Input(id='input-2', type='text', value='Canada'),
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
    ])


@app.callback(
    Output('output-state', 'children'),
    Input('submit-button-state', 'n_clicks'),
    State('input-1', 'value'),
    State('input-2', 'value'))
def update_output(n_clicks, input1, input2):
    return f'''The Button has been pressed {n_clicks} times,
        Input 1 is "{input1}" and Input 2 is "{input2}"'''


if __name__ == '__main__':
    app.run_server(debug=True)
