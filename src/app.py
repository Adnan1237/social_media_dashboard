from dash import Dash, html 
from dash_bootstrap_components.themes import BOOTSTRAP
from dashboard.components.layout import create_layout
from dashboard.data.loader import load_insta_data

def main() -> None: 
    sc_data = load_insta_data()
    app = Dash(external_stylesheets=[BOOTSTRAP]) 
    server = app.server
    app.layout = create_layout(app, sc_data)
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
