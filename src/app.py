from dash import Dash, html 
from dash_bootstrap_components.themes import BOOTSTRAP
from dashboard.components.layout import create_layout
from dashboard.data.loader import load_insta_data

# Define your Dash app
app = Dash(__name__, external_stylesheets=[BOOTSTRAP])

# Define your server instance
server = app.server

# Create your Dash layout
sc_data = load_insta_data()
app.layout = create_layout(app, sc_data)

# Entry point for running the app
if __name__ == "__main__":
    app.run_server(debug=True)

