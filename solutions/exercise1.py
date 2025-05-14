"""
Exercise 1
Make a Dash app, Just run this. Install the dependencies using pip install -r requirements.txt
"""

from dash import Dash, dash, html


# App
# This line is known as the Dash constructor and is responsible for initializing your app. It is almost always the same for any Dash app you create.
app = Dash()

# Layout
app.layout = html.Div()

# Start the flask server in local mode, you should not run this on a production server, use gunicorn instead.
if __name__ == "__main__":
    app.run(debug=True)
