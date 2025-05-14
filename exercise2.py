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

from dash import Dash, html, dcc, dash
import dash_mantine_components as dmc

# pinning react version to 18.2.0 as required by dash-mantine-components
dash._dash_renderer._set_react_version("18.2.0")

# App
app = Dash()

# Layout, to use dash mantine components, you need to wrap your app with MantineProvider,
# TODO: Replace the html.Div() with layout components
app.layout = dmc.MantineProvider(
    dmc.Container(
        [
            dmc.Title("Netflix Insights",order=1),
            dmc.Group(
                [
                    dmc.Paper("text 1", shadow="xs", p="xs"),
                    dmc.Paper("text 1", shadow="xs", p="xs"),
                    dmc.Paper("text 1", shadow="xs", p="xs"),
                ],
                grow=True,
            ),
            dmc.Title("Content Release Over Years", order=3, mt="xl"),
            dcc.Graph()
        ]
    )
)

if __name__ == "__main__":
    app.run(debug=True)
