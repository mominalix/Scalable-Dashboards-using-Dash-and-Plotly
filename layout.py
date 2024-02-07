# layout.py
from dash import html, dcc
from algorithms import (update_dashboard_1, update_dashboard_2, update_dashboard_3)

csv_file_path = 'data/dummy_data.csv'

def get_dashboard1_layout():
    
    graphs = update_dashboard_1(csv_file_path)
    return html.Div([
        html.H1('Dashboard 1'),
        html.Div(graphs),
        html.Div(id='dashboard1-content')
    ], style={'text-align': 'center'})

def get_dashboard2_layout():
    graphs = update_dashboard_2(csv_file_path)
    return html.Div([
        html.H1('Dashboard 1'),
        html.Div(graphs),
        html.Div(id='dashboard2-content')
    ], style={'text-align': 'center'})

def get_dashboard3_layout():
    graphs = update_dashboard_3(csv_file_path)
    return html.Div([
        html.H1('Dashboard 1'),
        html.Div(graphs),
        html.Div(id='dashboard3-content')
    ], style={'text-align': 'center'})
