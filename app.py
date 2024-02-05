from flask import Flask, render_template, request
from bubble_sort_algo import bubble_sort
from selection_sort_algo import selection_sort
from insertion_sort_algo import insertion_sort
from merge_sort_algo import merge_sort
from quick_sort_algo import quick_sort

app = Flask(__name__, static_url_path='', static_folder='C:\Sort Algorithm\static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort', methods=['POST'])
def sort():
    input_array = request.form.get('inputArray')
    input_array = list(map(int, input_array.split(',')))

    selected_algorithm = request.form.get('algorithm')

    if selected_algorithm == 'bubble':
        sorted_array = bubble_sort(input_array)
    elif selected_algorithm == 'selection':
        sorted_array = selection_sort(input_array)
    elif selected_algorithm == 'insertion':
        sorted_array = insertion_sort(input_array)
    elif selected_algorithm == 'merge':
        sorted_array = merge_sort(input_array)
    elif selected_algorithm == 'quick':
        sorted_array = quick_sort(input_array)
    else:
        sorted_array = input_array  # Default to the input array if no algorithm is selected

    return render_template('index.html', result=sorted_array)

if __name__ == "__main__":
    app.run(debug=True)