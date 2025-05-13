"""
Exercise 1
Run an empty Dash app.
- make an environment (optional) 
- Install dependencies with $ pip install -r requirements.txt
- Run the app with $ python exercise1.py
- You should see the dev tools on the bottom right of the app in your browser
"""
from dash import Dash, html


# App
# This line is known as the Dash constructor and is responsible for initializing your app. It is almost always the same for any Dash app you create.
app = Dash()

# Layout
app.layout = html.Div()

# Start the flask server in local mode, you should not run this on a production server, use gunicorn instead.
if __name__ == "__main__":
    app.run(debug=True)
