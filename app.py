from dash import Dash, html 
from dash_bootstrap_components.themes import BOOTSTRAP
from components.layout import create_layout

app = Dash(__name__, external_stylesheets=[BOOTSTRAP])
app.layout = create_layout(app)

if __name__ == "__main__":
    # app.run_server(debug=True, host="0.0.0.0", port=8050) -- This is for the railway server
    app.run_server(debug=True) # This is for the dev local server

