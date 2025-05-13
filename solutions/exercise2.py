"""
Exercise 2
Add a layout to the app. Using Dash Mantine Components (https://www.dash-mantine-components.com/)
and Dash Core Components (https://dash.plotly.com/dash-core-components), create a layout that contains:
- Container (DMC)
- Title (DMC)
- Group (DMC)
- Paper (DMC)
- Graph (DCC)
"""
import pandas as pd
from dash import Dash, html, dcc, dash
import dash_mantine_components as dmc
import plotly.express as px

# App
dash._dash_renderer._set_react_version("18.2.0")
app = Dash()


# Layout
app.layout = dmc.MantineProvider(
    children=dmc.Containdser(
        [
            dmc.Title("Netflix Content Insights", order=1, my="md"),
            dmc.Group(
                [
                    dmc.Paper("Text 1", shadow="xs", p="xs"),
                    dmc.Paper("Text 1", shadow="xs", p="xs"),
                    dmc.Paper("Text 1", shadow="xs", p="xs"),
                ],
                grow=True,
            ),
            dmc.Title("Ratings Distribution", order=3),
            dcc.Graph(figure=px.bar()),
            dmc.Title("Content Release Over Years", order=3, mt="xl"),
            dcc.Graph(figure=px.line()),
            dmc.Title("Top Countries", order=3, mt="xl"),
            dcc.Graph(figure=px.pie()),
        ],
        size="lg",
    )
)

if __name__ == "__main__":
    app.run(debug=True)
