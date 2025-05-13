"""
Exercise 4
Add interactivity to the application by adding callbacks
- add a dropdown 
- link the dropdown to the graph via the provided callback below
"""
from dash import Dash, dash, html, dcc, Input, State, Output, callback
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px

app = Dash()

# Read Data
df = pd.read_csv("data/netflix_titles.csv")

# Line chart
year_counts = (
    df["release_year"].value_counts().reset_index().sort_values(by="release_year")
)
line_fig = px.line(
    x=year_counts["release_year"],
    y=year_counts["count"],
    labels={"x": "Year", "y": "Releases"},
)

# Bar chart
rating_counts = df["rating"].value_counts().reset_index()
bar_fig = px.bar(
    x=rating_counts["rating"],
    y=rating_counts["count"],
    labels={"x": "Rating", "y": "Count"},
)
# Pie chart
country_counts = df["country"].dropna().value_counts()
pie_fig = px.pie(
    names=country_counts.head(5).index,
    values=country_counts.head(5).values,
)


app.layout = dmc.MantineProvider(
    children=dmc.Container(
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
            # TODO: Add a Dropdown
            dmc.Select(),
            dmc.Title("Content Release Over Years", order=3, mt="xl"),
            dcc.Graph(figure=line_fig),
            dmc.Title("Ratings Distribution", order=3),
            dcc.Graph(figure=bar_fig),
            dmc.Title("Top Countries", order=3, mt="xl"),
            dcc.Graph(figure=pie_fig),
        ],
        size="lg",
    )
)


# TODO: Add a callback
# @callback(
#     Output("", ""),
#     Input("", ""),
# )
# def update_graph():
#     pass


if __name__ == "__main__":
    app.run(debug=True)
