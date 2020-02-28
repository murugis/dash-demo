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
        dcc.Slider(
            id = "input1",
            min = 1,
            max = 5,
            value = 1,
            marks = {str(number) : str(number) for number in range(1,6,1)},
            step = None
        ),
        dcc.Slider(
            id = "input2",
            min = 7,
            max = 14,
            value = 7,
            marks = {str(number) : str(number) for number in range(7,15,1)},
            step = None
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
        html.P([], id="prediction")
    ])
])

layout = dbc.Row([element_1, element_2])

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
