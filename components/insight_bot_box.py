from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from functions.InsightBot.user_queries_mapping import user_query_mapping

def render(app: Dash) -> html.Div:

   # Define the layout
        layout = html.Div([
            # Title of the app
            html.H1("Interactive Question and Answer", style={'textAlign': 'center'}),
            
            # Input box for the question
            dcc.Input(id='input-question', type='text', placeholder='Enter your question here', style={'width': '80%', 'padding': '10px'}),
            
            # Submit button
            html.Button('Submit', id='submit-button', n_clicks=0, style={'padding': '10px 20px', 'margin': '10px'}),
            
            # Div to display the answer (empty at first)
            html.Div(id='output-answer', style={'fontSize': '20px', 'marginTop': '20px'})
        ])

        # Define the callback
        @app.callback(
            Output('output-answer', 'children'),
            Output('input-question', 'value'),  # This will reset the input field after submit
            Input('submit-button', 'n_clicks'),
            State('input-question', 'value')   # Get the current value of the input
        )
        def update_answer(n_clicks, question):
            if n_clicks == 0 or not question:
                return 'Please enter a question and press submit.', ''  # No answer and clear input
            
            # Example logic for answering (customize as needed)
            # answer = f"Your question was: '{question}'. This is a placeholder answer."

            answer = user_query_mapping(question)

            # Return the answer and clear the input box
            return answer, ''

        # Return the layout to be inserted into the app
        return layout
