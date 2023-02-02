import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
from dash import dcc
import dash_html_components as html
from dash import html
from calendar import monthrange

app = dash.Dash()

app.layout = html.Div(
    [
        html.H4('Year:',style={'display':'inline-block','margin-right':10}),
        dcc.Input(id="dfalse", type="number", value = 2022, placeholder="Debounce False"),

        html.H4('Month:', style={'display': 'inline','margin-right':50, 'margin': 10}),
        dcc.Input(
            id="dtrue", type="number", value= 2,
            min=1, max=12, step=1,
            debounce=True, placeholder="Debounce True",
        ),

        html.H4('Hours out:', style={'display': 'inline-block', 'margin-right': 40, 'margin': 15}),
        dcc.Input(
            id="input_range_2", type="number",value= 0, placeholder="input with range",
            style={'width': '4%'},
            min=0, max=100, step=0.1,

        ),

        html.H4('Hours per day:', style={'display': 'inline-block', 'margin-right': 40, 'margin': 15}),
        dcc.Input(
            id="per_day", type="number", value= 7.5,  placeholder="input with range",
            min=0, max=24, step=0.1,
        ),

        html.Hr(),
        html.Div(id="number-out"),
    ]
)


@app.callback(
    Output("number-out", "children"),
    [Input("dfalse", "value"),
    Input("dtrue", "value"),
    Input("input_range_2", "value"),
    Input("per_day", "value")
     ],
)
def number_render(fval, tval, rangeval,day):
    #return "dfalse: {}, dtrue: {}, range: {}".format(fval, tval, rangeval,day)
     number_days = (monthrange(fval, tval)[1])* day - rangeval
     return ( 'Total hours worked for this month is {}').format(number_days)


if __name__ == "__main__":
    app.run_server(debug=True)