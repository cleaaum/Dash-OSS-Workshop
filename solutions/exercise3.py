"""
Exercise 2
Add interactivity
- Add a dcc.Graph()
- read in the data
- add a dropdown 
- link the dropdown to the graph
"""
from dash import Dash, dash, html, dcc, Input, State, Output, callback
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px

app = Dash()
df = pd.read_csv("netflix_titles.csv")
year_counts = df["release_year"].value_counts().sort_index()
fig = px.bar(
    x=year_counts.index,
    y=year_counts.values,
    title="Yearly Releases",
    labels={"x": "Year", "y": "Releases"},
)

options = df["type"].unique()

app.layout = dmc.MantineProvider(
    [
        dmc.Select(data=options, value=options[0], id="dropdown"),
        dcc.Graph(figure=fig, id="graph"),
    ]
)


@callback(
    Output("graph", "figure"),
    Input("dropdown", "value"),
)
def update_graph(value):
    type_counts = df[df["type"] == value]["release_year"].value_counts().sort_index()
    fig = px.bar(
        x=type_counts.index,
        y=type_counts.values,
        title=f"{value} Releases",
        labels={"x": "Year", "y": "Releases"},
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
