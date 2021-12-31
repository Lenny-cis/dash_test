# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 11:02:18 2021

@author: linjianing
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)
colors = {'background': '#111111', 'text': '#7FDBFF'}
df = pd.DataFrame({
    'Fruit': ['苹果', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],
    'Amount': [4, 10, 2, 2, 4, 5],
    'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']})
fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')
fig.update_layout(plot_bgcolor=colors['background'],
                  paper_bgcolor=colors['background'],
                  font_color=colors['text'])
app.layout = html.Div(
    children=[
        html.H1(children='Hello Dash',
                style={'textAlign': 'center', 'color': colors['text']}),
        html.Div(children='Dash: A web application framework for your data.',
                 style={'textAlign': 'center', 'color': colors['text']}),
        dcc.Graph(id='example-graph', figure=fig)],
    style={'backgroundColor': colors['background']})
if __name__ == '__main__':
    app.run_server(debug=True)
