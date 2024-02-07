from dash import dcc
import pandas as pd
import plotly.express as px


def update_dashboard_1(csv_file_path):
    # Add code to update Dash 1 dashboard content
    # For illustration purposes, adding different dummy graphs
    return [
        dcc.Graph(figure={'data': [{'x': [1, 2, 3], 'y': [3, 4, 5], 'type': 'bar', 'name': 'Dash 1 Dummy Chart 1'}], 'layout': {'title': 'Dash 1 Dummy Chart 1'}},style={'width': '23%', 'display': 'inline-block','border-radius': '5px', 'background-color': '#1869c3', 'margin': '5px', 'padding': '5px', 'position': 'relative'}),
        dcc.Graph(figure={'data': [{'x': [1, 2, 3], 'y': [7, 4, 7], 'type': 'bar', 'name': 'Dash 1 Dummy Chart 2'}], 'layout': {'title': 'Dash 1 Dummy Chart 2'}},style={'width': '23%', 'display': 'inline-block','border-radius': '5px', 'background-color': '#1869c3', 'margin': '5px', 'padding': '5px', 'position': 'relative'})
    ]

def update_dashboard_2(csv_file_path):
    # Add code to update Dash 2 dashboard content
    # For illustration purposes, adding different dummy graphs
    return [
        dcc.Graph(figure={'data': [{'x': [1, 2, 3], 'y': [2, 5, 3], 'type': 'bar', 'name': 'Dash 2 Dummy Chart 1'}], 'layout': {'title': 'Dash 2 Dummy Chart 1'}},style={'width': '23%', 'display': 'inline-block','border-radius': '5px', 'background-color': '#1869c3', 'margin': '5px', 'padding': '5px', 'position': 'relative'}),
        dcc.Graph(figure={'data': [{'x': [1, 2, 3], 'y': [4, 1, 6], 'type': 'bar', 'name': 'Dash 2 Dummy Chart 2'}], 'layout': {'title': 'Dash 2 Dummy Chart 2'}},style={'width': '23%', 'display': 'inline-block','border-radius': '5px', 'background-color': '#1869c3', 'margin': '5px', 'padding': '5px', 'position': 'relative'})
    ]

def update_dashboard_3(csv_file_path):
    # Add code to update Dash 3 dashboard content
    # For illustration purposes, adding different dummy graphs
    return [
        dcc.Graph(figure={'data': [{'x': [1, 2, 3], 'y': [3, 6, 1], 'type': 'bar', 'name': 'Dash 3 Dummy Chart 1'}], 'layout': {'title': 'Dash 3 Dummy Chart 1'}},style={'width': '23%', 'display': 'inline-block','border-radius': '5px', 'background-color': '#1869c3', 'margin': '5px', 'padding': '5px', 'position': 'relative'}),
        dcc.Graph(figure={'data': [{'x': [1, 2, 3], 'y': [7, 2, 4], 'type': 'bar', 'name': 'Dash 3 Dummy Chart 2'}], 'layout': {'title': 'Dash 3 Dummy Chart 2'}},style={'width': '23%', 'display': 'inline-block','border-radius': '5px', 'background-color': '#1869c3', 'margin': '5px', 'padding': '5px', 'position': 'relative'})
    ]
