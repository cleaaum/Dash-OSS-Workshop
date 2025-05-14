"""
Exercise 6
Add a style sheet. Under assets/ you will find a styles.css style sheet. 
Comment out the style to see how it affects the app, and add any other styles to the app.
"""

from dash import Dash, dash, dcc, Input, Output, callback
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px
import dash_ag_grid as dag

dash._dash_renderer._set_react_version("18.2.0")
app = Dash()
server = app.server
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
            dmc.Select(data=df["type"].unique(), value=df["type"][0], id="dropdown"),
            dmc.Title("Content Release Over Years", order=3, mt="xl"),
            dcc.Graph(figure=line_fig, id="line-fig"),
            dmc.Title("Ratings Distribution", order=3),
            dcc.Graph(figure=bar_fig),
            dmc.Title("Top Countries", order=3, mt="xl"),
            dcc.Graph(figure=pie_fig),
            dag.AgGrid(
                # Using a list comprehension instead: [{"field": col} for col in df.columns],
                columnDefs=[
                    {"field": "title", "headerName": "Title"},
                    {"field": "type", "headerName": "Type"},
                    {"field": "director", "headerName": "Director"},
                    {"field": "cast", "headerName": "Cast"},
                    {"field": "country", "headerName": "Country"},
                    {"field": "date_added", "headerName": "Date Added"},
                    {"field": "release_year", "headerName": "Release Year"},
                    {"field": "rating", "headerName": "Rating"},
                    {"field": "duration", "headerName": "Duration"},
                    {"field": "listed_in", "headerName": "Listed In"},
                    {"field": "description", "headerName": "Description"},
                ],
                rowData=df.to_dict("records"),
            ),
        ],
        size="lg",
    )
)


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
