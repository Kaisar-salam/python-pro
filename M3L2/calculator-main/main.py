from flask import Flask, render_template, request

app = Flask(__name__)

def result_calculate(size, lights, device, eco):
    # Переменные для энергозатратности приборов
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5
    
    # Если включено энергосбережение, уменьшаем потребление энергии от ламп
    if eco:
        light_coef -= 0.01  # уменьшаем коэффициент на 0.01, например

    # Расчет результата
    return size * home_coef + lights * light_coef + device * devices_coef

# Первая страница
@app.route('/')
def index():
    return render_template('index.html')

# Вторая страница
@app.route('/<size>')
def lights(size):
    return render_template('lights.html', size=size)

# Третья страница
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template('electronics.html', size=size, lights=lights)

# Расчет с учетом энергосбережения
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    eco = int(request.args.get('eco', 0))  # eco = 1 если включено, иначе 0
    result = result_calculate(int(size), int(lights), int(device), eco)
    return render_template('end.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
