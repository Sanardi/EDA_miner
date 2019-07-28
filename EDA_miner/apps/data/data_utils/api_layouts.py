"""
This module collects the layouts for connecting to the various APIs.

Functions:
    - success_message: Notify the user for successful connection.

Global variables:
    - twitter_layout: 4 input fields and a button.
    - gsheets_layout: 2 input fields and a button.
    - reddit_layout: 2 input fields and a button.
    - quandl_layout: 2 input fields and a button.
    - spotify_layout: 2 input fields and a button.

Notes to others:
    You should probably not write code here, unless adding \
    a new API connection.

    IMPORTANT: When designing layouts ALWAYS pre-append the input \
    elements with the API name, and ALWAYS name each input id \
    according to the names of the variables of the respective API \
    connector.
"""

import dash_core_components as dcc
import dash_html_components as html

from apps.data.data_utils.ganalytics_metrics import metrics


def success_message(api):
    """
    Utility to provide feedback on successful connections.

    Args:
        api (str): Name / key of the API.

    Returns:
        list: A list of Dash elements.
    """

    return [
        html.H4(f"Successfully connected to the {api} API."),
        html.Br(),
    ]


# TODO: DATA WITH METHODS (see api_connectors) MEANS CLASSES!
#       Consider refactoring the code in these two files to make
#       everything a class for better & cleaner interface

twitter_login = [

    html.Div(id="twitter_login_form", children=[
        html.H5("Consumer key"),
        dcc.Input(id="twitter_consumer_key", type="text"),

        html.H5("Consumer Secret"),
        dcc.Input(id="twitter_consumer_secret", type="text"),

        html.H5("Access Token"),
        dcc.Input(id="twitter_access_token_key", type="text"),

        html.H5("Access Token Secret"),
        dcc.Input(id="twitter_access_token_secret", type="text"),

        html.Button("Connect!", id="twitter_connect_button",
                    style={"display": "inline"}, n_clicks=0),
    ]),

    html.Div(id="twitter_UI"),
]

twitter_success = [
    html.Br(),
    dcc.Input(id="twitter_account_name", placeholder="Enter a twitter handle name"),
    html.Button("Fetch tweets!", id="get_tweets_username", n_clicks=0),
    html.Div(id="twitter_results"),
]

gsheets_login = [

    html.Div(id="gsheets_login_form", children=[
        html.H5("Credentials file path"),
        dcc.Input(id="gsheets_credentials_file", type="text"),

        html.H5("Secret Key"),
        dcc.Input(id="gsheets_gspread_key", type="text"),

        html.Button("Connect!", id="gsheets_connect_button",
                    style={"display": "inline"}, n_clicks=0),
    ]),

    html.Div(id="gsheets_UI"),
]

reddit_login = [

    html.Div(id="reddit_login_form", children=[
        html.H5("Client id"),
        dcc.Input(id="reddit_client_id", type="text"),

        html.H5("Client secret"),
        dcc.Input(id="reddit_client_secret", type="text"),

        html.Button("Connect!", id="reddit_connect_button",
                    style={"display": "inline"}, n_clicks=0)
    ]),

    html.Div(id="reddit_UI")
]

spotify_login = [

    html.Div(id="quandl_login_form", children=[
        html.H5("Client id"),
        dcc.Input(id="spotify_client_id", type="text"),

        html.H5("Client secret"),
        dcc.Input(id="spotify_client_secret", type="text"),

        html.Button("Connect!", id="spotify_connect_button",
                    style={"display": "inline"}, n_clicks=0)
    ]),

    html.Div(id="spotify_UI"),
]

quandl_login = [

    html.Div(id="quandl_login_form", children=[
        html.H5("Quandl API key"),
        dcc.Input(id="quandl_api_key", type="text"),

        html.Button("Connect!", id="quandl_connect_button",
                    style={"display": "inline"}, n_clicks=0)
    ]),

    html.Div(id="quandl_UI"),
]

ganalytics_login = [

    html.Div(id="ganalytics_login_form", children=[
        html.H5("Client email"),
        dcc.Input(id="ganalytics_client_email", type="text"),

        html.H5("Private key"),
        dcc.Textarea(id="ganalytics_private_key"),

        html.Button("Connect!", id="ganalytics_connect_button",
                    style={"display": "inline"}, n_clicks=0)
    ]),

    html.Div(id="ganalytics_UI"),
]

ganalytics_success = [
    html.Br(),
    dcc.Dropdown(id="ganalytics_metrics", placeholder="Select metrics to fetch",
                 options=[{"value": metric["id"], "label": metric["name"]}
                          for metric in metrics["metrics"]],
                 multi=True),
    html.Button("Fetch metrics!", id="get_ganalytics_metrics", n_clicks=0),
    html.Div(id="ganalytics_results"),
]


# API: [ Forms for login, UI after login ]
logins_ui_mapping = {
    "twitter": [twitter_login, twitter_success],
    "gsheets": [gsheets_login, success_message("Google Sheets")],
    "reddit": [reddit_login, success_message("Reddit")],
    "quandl": [quandl_login, success_message("Quandl")],
    "spotify": [spotify_login, success_message("Spotify")],
    "ganalytics": [ganalytics_login, ganalytics_success]
}
