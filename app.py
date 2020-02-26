# ========================================================================== #
#                                                                            #
#      @ AUTHOR : Brandon Mulas                                              #
#      @   DATE : 20200226114738                                             #
#      @  TITLE : demo-dash                                                  #
#                                                                            #
# ========================================================================== #
import dash
import dash-bootstrap-components as dbc
import dash-core-components as dcc
import dash-html-components as html


""" 
    External stylesheets is going to be linked to the bootstrap cdn
    bootswatch template. Use this template to give yourself fast styling
    options.
"""
ext_style = [dbc.themes.DARKLY,
             "https://use.fontawesome.com/a5d39b00dd.css"]

"""
    Meta tags are meta
"""
meta_tags = [{'name':'viewport', 
              'content':'width=device-width, 
                         initial-scale=1'}]

"""
    Define app as dash.Dash object. Set external stylesheets and meta tags.
"""
app = dash.Dash(__name__,
                external_stylesheets=ext_style, 
                meta_tags=meta_tags)
app.title = "My Awesome Title"
server = app.server
