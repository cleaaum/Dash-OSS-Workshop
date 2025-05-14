"""
Exercise 3
Add data to the application and make 3 plotly charts! https://plotly.com/python/plotly-express/
- Read in the csv using pandas, store in a df variable
- filter and shape the data as needed
- create three plotly figures (bar, line, pie charts, or anything else you like)
"""

from dash import Dash, dash, dcc
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px

dash._dash_renderer._set_react_version("18.2.0")
app = Dash()

# Pandas is a library for tabular data manipulation and analysis, offering fast,
# flexible data structures like DataFrames and Series.
# Insert the path to the CSV file to read the data from teh csv and put into a dataframe
# TODO: df = pd.read_csv("")
# print(df)

# Manipulate the data as needed
# TODO: df = ...

# TODO: Make fig1: Line chart
line_fig = px.line()

# TODO: Make fig 2: Bar chart
bar_fig = px.bar()

# TODO: Make fig 3: Pie chart
pie_fig = px.pie()

app.layout = dmc.MantineProvider(
    dmc.Container(
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
            dmc.Title("Content Release Over Years", order=3, mt="xl"),
            dcc.Graph(figure=line_fig),
            dmc.Title("Ratings Distribution", order=3),
            dcc.Graph(),
            dmc.Title("Top Countries", order=3, mt="xl"),
            dcc.Graph(),
        ],
        size="lg",
    )
)


if __name__ == "__main__":
    app.run(debug=True)
