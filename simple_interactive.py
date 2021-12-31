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
