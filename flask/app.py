from flask import Flask, request, render_template, jsonify, send_from_directory
import os
from joblib import load
import numpy as np

#############################################
# Définition minimale de la classe LSTMClassifier
#############################################
# IMPORTANT : Cette définition doit être identique à celle utilisée lors de la sauvegarde du modèle.
class LSTMClassifier:
    def __init__(self, *args, **kwargs):
        pass

    def predict(self, X):
        # Exemple simulé de prédiction :
        # Retourne 1 si la somme des valeurs d'entrée > 100, sinon 0.
        if np.sum(X) > 100:
            return np.array([1])
        else:
            return np.array([0])

#############################################
# Chargement des objets sauvegardés
#############################################
# Ici, nous ne chargeons plus le scaler ni le PCA puisque nous souhaitons supprimer la transformation.
model = load('model/LSTMClassifier.pkl')  # Modèle de prédiction sauvegardé via joblib

#############################################
# Création de l'application Flask
#############################################
app = Flask(__name__)

# Route pour servir le favicon (facultatif)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')

# Route d'accueil
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title="Prédiction des Arrêts de Protection d’un Cobot")

# Route de prédiction (POST)
@app.route('/predict', methods=['POST'])
def predict_route():
    # Récupérer les données du formulaire (type form-data)
    data = request.form

    # Définition de l'ordre des 5 features importantes
    feature_order = [
        "Current_J0", "Temperature_T0", "Speed_J0", "Tool_current", "cycle"
    ]
    
    try:
        # Extraction et conversion en float des valeurs
        input_features = [float(data[feat]) for feat in feature_order]
    except KeyError as e:
        return render_template('index.html', title="Prédiction des Arrêts de Protection d’un Cobot", error=f"Champ manquant : {e}")
    except ValueError as ve:
        return render_template('index.html', title="Prédiction des Arrêts de Protection d’un Cobot", error=f"Erreur de format : {ve}")

    # Conversion en array NumPy de forme (1, 5)
    input_array = np.array(input_features).reshape(1, -1)

    # Nous n'appliquons aucune normalisation ni réduction de dimension,
    # on passe directement l'input au modèle.
    prediction = model.predict(input_array)
    predicted_label = int(prediction[0])
    
    # Interprétation de la prédiction
    if predicted_label == 1:
        message = "Pas d'arrêt de machine"
    else:
        message = "Arrêt de machine"

    return render_template('index.html', title="Prédiction des Arrêts de Protection d’un Cobot", prediction=message)

# Route de test simple
@app.route('/test', methods=['GET'])
def test():
    return "bonjour"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
