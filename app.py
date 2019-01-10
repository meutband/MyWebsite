from flask import Flask, render_template
from math import pi
import pandas as pd
from bokeh.plotting import figure
from bokeh.transform import cumsum
from bokeh.layouts import gridplot
from bokeh.embed import components
from bokeh.models.sources import ColumnDataSource

app = Flask(__name__)


@app.route("/")
def home():
    plot1 = getBarGraph()
    plot2 = getPieCharts()

    script1, div1 = components(plot1)
    script2, div2 = components(plot2)

    return render_template('home.html', script1=script1, div1=div1, script2=script2, div2=div2)


# Not being used yet.
@app.route("/blog")
def blog():
    return render_template('blog.html')


# Not being used yet
@app.route("/projects")
def projects():
    return render_template('projects.html')


def getBarGraph():

    focus = ['Programming', 'DataScience', 'WebDevelopment', 'DataVisualization', 'Mathematics']
    percent = [90, 80, 50, 70, 80]
    colors = ['darkorange', 'chocolate', 'sandybrown', 'orange', 'lightsalmon']

    source = ColumnDataSource(data=dict(focus=focus, percent=percent, color=colors))

    bar = figure(x_range=focus, plot_height=400, plot_width=500, sizing_mode='scale_width', title="Skills Focus",
                 y_axis_label='Percent', tools="hover", tooltips=[('', '@percent%')], toolbar_location=None)

    bar.vbar(x='focus', top='percent', width=0.6, color='color', source=source)
    bar.xgrid.grid_line_color = None
    bar.background_fill_color = "gainsboro"
    bar.border_fill_color = "gainsboro"
    bar.title.text_font_size = "13pt"
    bar.yaxis.axis_label_text_font_size = "12pt"
    bar.xaxis.major_label_text_font_size = "10pt"
    bar.xaxis.major_label_orientation = pi/5
    bar.ygrid.grid_line_color = 'black'
    bar.outline_line_color = 'black'

    return bar


def getPieCharts():
    programming = {'Python': [70, .8], 'SQL': [25, .6], 'Other': [5, .4]}
    datascience = {'Python': [40, .8], 'Numpy': [25, .6], 'Sklearn': [25, .5], 'Other': [10, .4]}
    webdevelopment = {'HTML/CSS': [40, .9], 'Django': [30, .7], 'Flask': [30, .5]}
    datavisualization = {'Matplotlib': [75, .8], 'Bokeh': [10, .6], 'Seaborn': [10, .5], 'Other': [5, .4]}
    mathematics = {'Probability': [35, .9], 'Statistics': [35, .7], 'Linear Algegra': [30, .5]}

    data1 = pd.DataFrame.from_dict(programming, orient='index').rename(
        columns={0: 'percent', 1: 'alpha', 'index': 'tech'})
    data2 = pd.DataFrame.from_dict(datascience, orient='index').rename(
        columns={0: 'percent', 1: 'alpha', 'index': 'tech'})
    data3 = pd.DataFrame.from_dict(webdevelopment, orient='index').rename(
        columns={0: 'percent', 1: 'alpha', 'index': 'tech'})
    data4 = pd.DataFrame.from_dict(datavisualization, orient='index').rename(
        columns={0: 'percent', 1: 'alpha', 'index': 'tech'})
    data5 = pd.DataFrame.from_dict(mathematics, orient='index').rename(
        columns={0: 'percent', 1: 'alpha', 'index': 'tech'})

    data1['angle'] = data1['percent'] / data1['percent'].sum() * 2 * pi

    p1 = figure(plot_height=175, plot_width=250, sizing_mode='stretch_both', title="Programming", x_range=(-0.5, 1.5),
                tools="hover", tooltips='@index: @percent%')

    p1.wedge(x=0, y=1, radius=0.25,
             start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
             line_color="white", fill_color='darkorange', alpha='alpha', legend='index', source=data1)

    # p1.axis.axis_label = None
    p1.axis.visible = False
    p1.grid.grid_line_color = None
    p1.background_fill_color = "gainsboro"
    p1.border_fill_color = "gainsboro"
    p1.outline_line_color = 'black'

    data2['angle'] = data2['percent'] / data2['percent'].sum() * 2 * pi

    p2 = figure(plot_height=175, plot_width=250, sizing_mode='stretch_both', title="DataScience", x_range=(-0.5, 1.5),
                tools="hover", tooltips='@index: @percent%')

    p2.wedge(x=0, y=1, radius=0.25,
             start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
             line_color="white", fill_color='chocolate', alpha='alpha', legend='index', source=data2)

    p2.axis.axis_label = None
    p2.axis.visible = False
    p2.grid.grid_line_color = None
    p2.background_fill_color = "gainsboro"
    p2.border_fill_color = "gainsboro"
    p2.outline_line_color = 'black'

    data3['angle'] = data3['percent'] / data3['percent'].sum() * 2 * pi

    p3 = figure(plot_height=175, plot_width=250, sizing_mode='stretch_both', title="WebDevelopment", x_range=(-0.5, 1.5),
                tools="hover", tooltips='@index: @percent%')

    p3.wedge(x=0, y=1, radius=0.25,
             start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
             line_color="white", fill_color='sandybrown', alpha='alpha', legend='index', source=data3)

    p3.axis.axis_label = None
    p3.axis.visible = False
    p3.grid.grid_line_color = None
    p3.background_fill_color = "gainsboro"
    p3.border_fill_color = "gainsboro"
    p3.outline_line_color = 'black'

    data4['angle'] = data4['percent'] / data4['percent'].sum() * 2 * pi

    p4 = figure(plot_height=175, plot_width=250, sizing_mode='stretch_both', title="DataVisualization", x_range=(-0.5, 1.5),
                tools="hover", tooltips='@index: @percent%')

    p4.wedge(x=0, y=1, radius=0.25,
             start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
             line_color="white", fill_color='orange', alpha='alpha', legend='index', source=data4)

    p4.axis.axis_label = None
    p4.axis.visible = False
    p4.grid.grid_line_color = None
    p4.background_fill_color = "gainsboro"
    p4.border_fill_color = "gainsboro"
    p4.outline_line_color = 'black'

    data5['angle'] = data5['percent'] / data5['percent'].sum() * 2 * pi

    p5 = figure(plot_height=175, plot_width=250, sizing_mode='stretch_both', title="Mathematics", x_range=(-0.5, 1.5),
                tools="hover", tooltips='@index: @percent%')

    p5.wedge(x=0, y=1, radius=0.25,
             start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
             line_color="white", fill_color='lightsalmon', alpha='alpha', legend='index', source=data5)

    p5.axis.axis_label = None
    p5.axis.visible = False
    p5.grid.grid_line_color = None
    p5.background_fill_color = "gainsboro"
    p5.border_fill_color = "gainsboro"
    p5.outline_line_color = 'black'

    p = gridplot([[p1, p2], [p3, p4], [p5, None]], toolbar_location=None)

    return p


if __name__ == '__main__':
    app.run(debug=False)