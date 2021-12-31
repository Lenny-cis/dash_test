# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 15:00:51 2021

@author: linjianing
"""

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
app.layout = html.Div([
    html.Div([
        html.Label('Dropdown'),
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC',
                 'label': u'Montreal', 'value': 'MTL',
                 'label': 'San Francisco', 'value': 'SF'}],
            value='MTL'),
        html.Br(),
        html.Label('Multi-Select Dropdown'),
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC',
                 'label': u'Montreal', 'value': 'MTL',
                 'label': 'San Francisco', 'value': 'SF'}],
            value=['MTL', 'SF'],
            multi=True),
        html.Br(),
        html.Label('Radio Items'),
        dcc.RadioItems(
            options=[
                {'label': 'New York City', 'value': 'NYC',
                 'label': u'Montreal', 'value': 'MTL',
                 'label': 'San Francisco', 'value': 'SF'}],
            value='MTL'),],
    style={'padding': 10, 'flex': 1}),
    html.Div([
        html.Label('checkboxes'),
        dcc.Checklist(
            options=[
                {'label': 'New York City', 'value': 'NYC',
                 'label': u'Montreal', 'value': 'MTL',
                 'label': 'San Francisco', 'value': 'SF'}],
            value=['MTL', 'SF']),
        html.Br(),
        html.Label('Text Input'),
        dcc.Input(value='MTL', type='text'),
        html.Br(),
        html.Label('Slider'),
        dcc.Slider(
            min=0, max=9,
            marks={i: 'Label {}'.format(i) if i == 1 else str(i)
                   for i in range(1, 6)}, value=5,),],
        style={'padding': 10, 'flex': 1})],
    style={'display': 'flex', 'flex-direction': 'row'})

if __name__ == '__main__':
    app.run_server(debug=True)
