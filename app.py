from app_config import configure_app
from layout import get_dashboard1_layout, get_dashboard2_layout, get_dashboard3_layout
from dash import dcc, Input, Output, html

app = configure_app()

# Layout
dashboard1_layout = get_dashboard1_layout
dashboard2_layout = get_dashboard2_layout
dashboard3_layout = get_dashboard3_layout

# Callbacks
app.layout = html.Div([
    dcc.Tabs(id='dashboard-tabs', value='dashboard1_tab', children=[
        dcc.Tab(label='Dashboard 1', value='dashboard1_tab'),
        dcc.Tab(label='Dashboard 2', value='dashboard2_tab'),
        dcc.Tab(label='Dashboard 3', value='dashboard3_tab')
    ]),
    html.Div(id='dashboard-content')
])

@app.callback(
    Output('dashboard-content', 'children'),
    [Input('dashboard-tabs', 'value')]
)
def update_dashboard_content(selected_tab):
    if selected_tab == 'dashboard1_tab':
        return dashboard1_layout()
    elif selected_tab == 'dashboard2_tab':
        return dashboard2_layout()
    elif selected_tab == 'dashboard3_tab':
        return dashboard3_layout()

if __name__ == '__main__':
    app.run_server(debug=True)
