from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://api.calorieninjas.com/v1/nutrition?query="
API_KEY = "3fdD2REadhq6QgMnlasiEA==H2mLZVaADil1p0Ib" 

@app.route('/', methods=['GET', 'POST'])
def index():
    food = None
    error = None

    if request.method == 'POST':
        query = request.form.get('food_name')
        headers = {'X-Api-Key': API_KEY}
        params = {'query': query}
        response = requests.get(API_URL, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if data.get('items'):
                food = data['items'][0]
            else:
                error = "No se encontro información para ese alimento."
        else:
            error = f"Error al conectar con la API (código {response.status_code})"

    return render_template('nutrition.html', food=food, error=error)

if __name__ == '__main__':
    app.run(debug=True)