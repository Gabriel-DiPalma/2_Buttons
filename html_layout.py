#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 00:09:19 2021

@author: gabriel
"""


import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_daq as daq

center_class = {
      'display': 'flex',
  'flexDirection': 'column',
  'justify-content':  'center',
  'alignItems': 'center',
  'text-align': 'center',
  'minHeight': '100vh',
    
    }

gauge = daq.Gauge(
    id = "gauge",
    color={"gradient":True,"ranges":{"green":[0,6],"yellow":[6,8],"red":[8,10]}},
    showCurrentValue=True,
    value=0,
    label= {'label':'The Gauge','style':{'fontSize':28}},
    max=10,
    min=0,
)  


button1 = html.Div(
    [
        dbc.Button("button 1", id="button1", className="mr-2"),
        html.Span(id="example-output1", style={"vertical-align": "middle"}),
    ]
)

button2 = html.Div(
    [
        dbc.Button("button 2", id="button2", color="info", className="mr-2"),
        html.Span(id="example-output2", style={"vertical-align": "middle"}),
    ]
)

layout = html.Div([
    
    dbc.Row(children = [html.Div(button1), html.Div(button2)]
        ,justify = 'center', align = 'center'),
    dbc.Row(html.Hr()),
    dbc.Row(gauge,justify = 'center', align = 'center')
      
])



html_layout = dbc.Container([layout], style = center_class, fluid = True)


