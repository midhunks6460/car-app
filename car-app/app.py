from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

cars = [
    {'id': 1, 'make': 'Toyota', 'model': 'Camry', 'year': 2020},
    {'id': 2, 'make': 'Honda', 'model': 'Civic', 'year': 2019},
    {'id': 3, 'make': 'Ford', 'model': 'Mustang', 'year': 2021},
]

@app.route('/')
def index():
    return render_template('index.html', cars=cars)

@app.route('/add_car', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = int(request.form['year'])
        car = {'id': len(cars) + 1, 'make': make, 'model': model, 'year': year}
        cars.append(car)
        return redirect(url_for('index'))
    return render_template('add_car.html')

if __name__ == '__main__':
    app.run(debug=True)
