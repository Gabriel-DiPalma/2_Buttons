#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 21:10:45 2021

@author: gabriel
"""

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from random import randrange

import dash_daq as daq
from dash_extensions.enrich import DashProxy, MultiplexerTransform


from html_layout import html_layout


app = DashProxy(__name__,transforms=[MultiplexerTransform()],external_stylesheets= [dbc.themes.BOOTSTRAP])


application = app.server

hidden = html.Div(children = [
                              html.Div(id = "hidden")
                              ],style = {'display': 'none'}
    )


app.layout = html.Div([html_layout,hidden])

@app.callback(
    Output("gauge", "value"), [Input("hidden", "children")]
)
def gauge_value(n):
    if n is None:
        return 0
    else:
        return n


@app.callback(
    Output("example-output1","children"),Output("hidden", "children"), [Input("button1", "n_clicks")]
)
def on_button_click_1(n):
    if n is None:
        return "Not clicked.",n
    else:
        n = randrange(10)
        return f"Random number is: {n} .",n
    
@app.callback(
    Output("example-output2","children"),Output("hidden", "children"),[Input("button2", "n_clicks")]
)
def on_button_click_2(n):
    if n is None:
        return "Not clicked.",n
    else:
        n = randrange(10)
        return f"Random number is: {n} .", n

    
if __name__ == "__main__":
    app.run_server(port=8080, debug= False, use_reloader = True)