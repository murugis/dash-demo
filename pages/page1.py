import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from app import app


"""
    Page 1
"""

column_1 = dbc.Col([
    dcc.Markdown(
        """
            This is Column One!
        """
    )],
    md=4)

column_2 = dbc.Col([
    dcc.Markdown(
        """
            This is Column Two!
        """
    )],
    md=4)

column_3 = dbc.Col([
    dcc.Markdown(
        """
            This is Column Three!
        """
    )],
    md=4)

# Create the grid layout with these elements
layout = dbc.Row([column_1,
                  column_2,
                  column_3])

# END

