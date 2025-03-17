import dash
from dash import html

app = dash.Dash(__name__)
server = app.server  # Expose the server variable

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''Dash: A new web application framework for Python.''')
])

if __name__ == "__main__":
    app.run_server(debug=False, host='0.0.0.0', port=8050)