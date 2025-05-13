import pandas as pd
from dash import Dash, html, dcc, dash
import dash_mantine_components as dmc
import plotly.express as px

# Load data
df = pd.read_csv("data/netflix_titles.csv")
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# App
dash._dash_renderer._set_react_version("18.2.0")
app = Dash(__name__)


# Metrics
type_counts = df["type"].value_counts()
country_counts = df["country"].dropna().value_counts()
rating_counts = df["rating"].value_counts()
year_counts = df["release_year"].value_counts().sort_index()

# Layout
app.layout = dmc.MantineProvider(
    dmc.Container(
        [
            dmc.Title("Netflix Content Insights", order=1, my="md"),
            dmc.Group(
                [
                    dmc.Paper(
                        dmc.Text(f"{type_counts.get('Movie', 0)} Movies"),
                        shadow="md",
                        p="md",
                        withBorder=True,
                        radius="md",
                    ),
                    dmc.Paper(
                        dmc.Text(f"{type_counts.get('TV Show', 0)} TV Shows"),
                        shadow="md",
                        p="md",
                        withBorder=True,
                        radius="md",
                    ),
                    dmc.Paper(
                        dmc.Text(f"{df['country'].nunique()} Countries"),
                        shadow="md",
                        p="md",
                        withBorder=True,
                        radius="md",
                    ),
                    dmc.Paper(
                        dmc.Text(
                            f"{df['release_year'].min()} - {df['release_year'].max()}"
                        ),
                        shadow="md",
                        p="md",
                        withBorder=True,
                        radius="md",
                    ),
                ],
                grow=True,
                mb="xl",
            ),
            dmc.Title("Ratings Distribution", order=3),
            dcc.Graph(
                figure=px.bar(
                    x=rating_counts.index,
                    y=rating_counts.values,
                    labels={"x": "Rating", "y": "Count"},
                    title="Ratings",
                )
            ),
            dmc.Title("Content Release Over Years", order=3, mt="xl"),
            dcc.Graph(
                figure=px.line(
                    x=year_counts.index,
                    y=year_counts.values,
                    labels={"x": "Year", "y": "Releases"},
                    title="Yearly Releases",
                )
            ),
            dmc.Title("Top Countries", order=3, mt="xl"),
            dcc.Graph(
                figure=px.pie(
                    names=country_counts.head(5).index,
                    values=country_counts.head(5).values,
                    title="Top 5 Countries",
                )
            ),
            dmc.Space(h=40),
            dmc.Alert(
                title="Fun Fact 🎬",
                children=f"The longest title is '",
                color="teal",
                variant="light",
            ),
        ],
        size="md",
    )
)

if __name__ == "__main__":
    app.run(debug=True)
