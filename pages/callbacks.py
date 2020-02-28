# Dash component imports
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# App import
from app import app
# Imports for model
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression


# Instantiate the model
infile = open("./assets/model.pkl", "rb")
model = pickle.load(infile)
infile.close()

"""
    Basic Callbacks:

        The goal of this page will be to outline the basic steps for creating
        callback functions. These allow users to interact with your graphs and
        page elements.
"""


element_1 = dbc.Col([
    html.Div([
        html.P([
            "Here lies Input 1 (Not sure what this is)"
        ],
        style = {"text-align" : "center"}),
        dcc.Dropdown(
            id = "input1",
            options = [
                {"label" : str(x), "value" : x} for x in range(1,6,1)
            ],
            value = 1
        ),
        html.P([
            "This here be Input 2 (I don't know)"
        ],
        style = {"text-align" : "center"}
        ),
        dcc.Slider(
            id = "input2",
            min = 7,
            max = 14,
            value = 7,
            marks = {str(number) : str(number) for number in range(7,15,1)},
            step = None
        ),
        html.P([
            "Last one, no idea."
        ],
        className = "text-center"
        ),
        dcc.Slider(
            id = "input3",
            min = 10,
            max = 50,
            value = 26,
            marks = {str(number) : str(number) for number in range(10,52,2)},
            step = None
        )
    ])
])

element_2 = dbc.Col([
    html.Div([
        html.P([
            "The model says..."
        ]),
        html.P(id="prediction"),
        html.P(id="dropdown-value"),
        dcc.Graph(
            id = "my_graph",
            figure = {
                "data" : [
                    {"x" : [1,2,3,4,5], "y" : [2,4,8,4,2], "type" : "bar", "name" : "awesome_graph"}
                ],
                "layout" : {"title":"Mah awesome graph"}
            }
        )
    ])
])

@app.callback(
    Output("prediction", "children"),
    [Input("input1", "value"),
     Input("input2", "value"),
     Input("input3", "value")]
)
def get_prediction(input1, input2, input3):
    """
        Return prediction for given inputs
    """
    return model.predict(np.array([[input1, input2, input3]]))

@app.callback(
    Output("dropdown-value", "children"),
    [Input("input1", "value")]
)
def dropdown_selection(input1):
    return f"You selected {input1} for input1."

layout = dbc.Row([element_1, element_2])
