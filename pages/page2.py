import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from app import app


"""
    Page 2
"""

some_thing = dbc.Col([
    dcc.Markdown(
        """
            This is all I have on this page. Pretty barren right now!
        """
    )],
    md=12)

layout = dbc.Row([some_thing])
