from flask import Flask, render_template, request
from StandardDeviation import StdDev

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result=None,)

@app.route('/stddev', methods=['POST'])
def calculate_stddev():
    numbers = request.form.get('numbers')  # Fetch the input data from an HTML form
    if not numbers:
        return render_template('index.html', result=None)

    numbers_list = list(map(float, numbers.split(',')))  # Convert string to a list of floats

    # Calculate standard deviation
    try:
        result = StdDev(numbers_list)
        return render_template('index.html', result=result, numbers='')
    except ValueError as e:
        return render_template('index.html', result=str(e), numbers=numbers)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')