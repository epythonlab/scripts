"""
Create an Interactive Data visualization using Plotly
"""
# pip install plotly

import plotly.express as px

data = px.data.gapminder()

fig = px.scatter(
    data_frame=data,
    x='gdpPercap',
    y='lifeExp',
    size='pop',
    color='continent',
    hover_name='country',
    log_x=True,
    range_x=[300, 100000],
    range_y=[20, 90],
    title='GDP per Capita VS Life Expetancy',
    labels={'gdpPercap':'GDP per Capita',
            'lifeExp':'Life Expetancy'},
    template='plotly_dark'
    )
# update the axis
fig.update_xaxes(title_text='GDP per Capita(log scale)')
fig.update_yaxes(title_text='Life Expetancy')

# show the graph
fig.show()