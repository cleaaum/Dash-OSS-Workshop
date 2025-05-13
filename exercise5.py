"""
Exercise 5
Add an Ag Grid
"""
from dash import Dash, dash, html, dcc, Input, State, Output, callback
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px
import dash_ag_grid as dag

app = Dash()

# Read Data
df = pd.read_csv("data/netflix_titles.csv")

# Make fig1: Line chart
year_counts = (
    df["release_year"].value_counts().reset_index().sort_values(by="release_year")
)
line_fig = px.line(
    x=year_counts["release_year"],
    y=year_counts["count"],
    labels={"x": "Year", "y": "Releases"},
)

# Make fig 2: Bar chart
rating_counts = df["rating"].value_counts().reset_index()
bar_fig = px.bar(
    x=rating_counts["rating"],
    y=rating_counts["count"],
    labels={"x": "Rating", "y": "Count"},
)
# Make fig 3: Pie chart
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
            # Add a Dropdown
            dmc.Select(data=df["type"].unique(), value=df["type"][0], id="dropdown"),
            dmc.Title("Content Release Over Years", order=3, mt="xl"),
            dcc.Graph(figure=line_fig, id="line-fig"),
            dmc.Title("Ratings Distribution", order=3),
            dcc.Graph(figure=bar_fig),
            dmc.Title("Top Countries", order=3, mt="xl"),
            dcc.Graph(figure=pie_fig),
            # Add Grd Here
            dag.AgGrid(),
        ],
        size="lg",
    )
)


# Add a callback
@callback(
    Output("line-fig", "figure"),
    Input("dropdown", "value"),
)
def update_graph(value):
    df = pd.read_csv("data/netflix_titles.csv")
    df = df.loc[df["type"] == value]
    year_counts = (
        df["release_year"].value_counts().reset_index().sort_values(by="release_year")
    )
    line_fig = px.line(
        x=year_counts["release_year"],
        y=year_counts["count"],
        labels={"x": "Year", "y": "Releases"},
    )
    return line_fig


if __name__ == "__main__":
    app.run(debug=True)
