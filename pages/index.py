import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from app import app


"""
    Build application index (landing) page. This will be the first page
    a visitor will see upon hitting your app.
"""

top = dbc.Col([
    dcc.Markdown(
        """
            # This is a markdown header!
        """
    )],
    md=12)

column_1 = dbc.Col([
    dcc.Markdown(
        """
            ## Column 1
        """
    )],
    md=6)

column_2 = dbc.Col([
    dcc.Markdown(
        """
            ## Column 2
        """
    )],
    md=6)

# Build the grid using these elements
layout = dbc.Row([top]), dbc.Row([column_1, column_2])


# END
