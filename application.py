import dash
import dash_html_components as html
import dash_core_components as dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.scripts.config.serve_locally = True
# app.css.config.serve_locally = True

app.layout = html.Div(children=[
    html.H1(children='Hello DS4A Medellin Team 4!'),

    html.Div(children='''
        Team 4: Here's the first version for Python app.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Data Visualization'
            }
        }
    )
])

application = app.server

if __name__ == '__main__':
    application.run(debug=True, port=3000)
