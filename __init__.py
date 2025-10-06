from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"

@app.route("/contacts/")
def MaSecondeAPI():
    return """
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>Formulaire de contact</title>
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <style>
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 2rem; }
    h2 { margin-bottom: 1rem; }
    form { max-width: 720px; }
    fieldset { border: 1px solid #ddd; border-radius: 8px; padding: 1rem; margin-bottom: 1rem; }
    legend { padding: 0 .5rem; color: #444; }
    label { display: block; font-size: .95rem; margin: .5rem 0 .25rem; }
    input { width: 100%; padding: .6rem .7rem; border: 1px solid #ccc; border-radius: 6px; }
    .row { display: grid; grid-template-columns: 1fr 2fr; gap: .75rem; }
    .row-2 { display: grid; grid-template-columns: 1fr 2fr; gap: .75rem; }
    button { margin-top: .5rem; padding: .7rem 1rem; border: 0; border-radius: 8px; cursor: pointer; }
    .primary { background: #1a73e8; color: #fff; }
    .muted { color: #666; font-size: .9rem; margin-left: .5rem; }
  </style>
</head>
<body>
  <h2>Formulaire de contact</h2>

  <form id="contact-form" action="#" method="post" onsubmit="event.preventDefault(); alert('Soumission inactive pour le moment.');">
    <fieldset>
      <legend>Identité</legend>
      <label for="last_name">Nom</label>
      <input id="last_name" name="last_name" type="text" placeholder="DURAND" required />

      <label for="first_name">Prénom</label>
      <input id="first_name" name="first_name" type="text" placeholder="Alice" required />
    </fieldset>

    <fieldset>
      <legend>Adresse</legend>

      <div class="row">
        <div>
          <label for="street_number">N° de rue</label>
          <input id="street_number" name="street_number" type="text" inputmode="numeric" pattern="[0-9]{1,6}" placeholder="12" />
        </div>
        <div>
          <label for="street_name">Rue</label>
          <input id="street_name" name="street_name" type="text" placeholder="Rue de la Paix" required />
        </div>
      </div>

      <div class="row-2" style="margin-top:.75rem;">
        <div>
          <label for="postal_code">Code postal</label>
          <input id="postal_code" name="postal_code" type="text"
                 inputmode="numeric" pattern="[0-9A-Za-z\\- ]{3,10}" placeholder="75002" required />
        </div>
        <div>
          <label for="city">Ville</label>
          <input id="city" name="city" type="text" placeholder="Paris" required />
        </div>
      </div>

      <label for="country" style="margin-top:.75rem;">Pays</label>
      <input id="country" name="country" type="text" list="countries" placeholder="France" />
      <datalist id="countries">
        <option value="France"></option>
        <option value="Belgique"></option>
        <option value="Suisse"></option>
        <option value="Canada"></option>
        <option value="Luxembourg"></option>
      </datalist>
    </fieldset>

    <button type="submit" class="primary">Envoyer</button>
    <span class="muted">(inactif pour le moment)</span>
  </form>
</body>
</html>
"""


@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

@app.route("/histogramme/")
def monhistogramme():
    return render_template("histogramme.html")


  
if __name__ == "__main__":
  app.run(debug=True)
