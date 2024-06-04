from flask import Flask, render_template, request
from app import calculate_volume

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        shape = request.form.get('shape')
        if not shape:
            return 'Не указана фигура', 400

        try:
            a = float(request.form['a'].replace(',', '.')) if request.form['a'] != '' else 0
            b = float(request.form['b'].replace(',', '.')) if request.form['b'] != '' else 0
            c = float(request.form['c'].replace(',', '.')) if request.form['c'] != '' else 0
            precision = int(request.form['precision'])
        except ValueError:
            return 'Некорректные параметры', 400

        volume = calculate_volume(shape, a, b, c, precision)
        return render_template('index.html', volume=volume)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
