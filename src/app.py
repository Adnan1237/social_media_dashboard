from dash import Dash, html 
from dash_bootstrap_components.themes import BOOTSTRAP
from components.layout import create_layout
from data.loader import load_insta_data, load_follower_data

# DATA_PATH = './data/transactions.csv'
SC_DATA_PATH = './datasets/sc_social_media_master.csv'
TARGET_DATA_PATH = './datasets/followers_target.csv'

def main() -> None: 
    sc_data = load_insta_data(SC_DATA_PATH)
    app = Dash(external_stylesheets=[BOOTSTRAP]) 
    server = app.server
    app.layout = create_layout(app, sc_data)
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
