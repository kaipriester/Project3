from flask import Blueprint, render_template, request
from website.scripts.sort import sort_array
from website.scripts.minheap import min_heap


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/sort', methods=['GET', 'POST'])
def sort():
    if request.method == 'POST':
        k = request.form.get('k')
        date_time, wind_speeds, timer = sort_array(k)
        print(date_time)
        print(wind_speeds)
        print(timer)
        return render_template("sort_results.html", k=k, date_time=date_time, wind_speeds=wind_speeds, timer=timer)
    return render_template("sort.html")

@views.route('/minheap', methods=['GET', 'POST'])
def minheap():
    if request.method == 'POST':
        k = request.form.get('k')
        date_time, wind_speeds, timer = min_heap(k)
        return render_template("minheap_results.html", k=k, date_time=date_time, wind_speeds=wind_speeds, timer=timer)
    return render_template("minheap.html")    