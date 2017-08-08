from app import app
from flask import render_template, make_response
import datetime

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/stuff", methods=['GET'])
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
            'title' : ' Hello!',
            'time' : timeString
        }
    return render_template('main.html', **templateData)
@app.route("/simple.png")
def simple():
    from io import StringIO
    from io import BytesIO
    import random
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig = Figure()
    ax = fig.add_subplot(111)
    x=[]
    y=[]
    now = datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0,1000))
    ax.plot_date(x,y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas = FigureCanvas(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    response = make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response

@app.route("/companyList")
def companies():
    import csv
    from yahoo_finance import Share
    stocks = []
    with open('companyList.csv') as csvfile:
        stockreader = csv.reader(csvfile)
        for row in stockreader:
            sharename = str(row)[2:][:-2].upper()
            try:
                share = Share(str(row)[2:][:-2].upper())
                price = share.get_price()
            except:
                price = 0
            stocks.append({'name': sharename,
                           'price': price})
            
    return render_template("list.html", stocks=stocks)
