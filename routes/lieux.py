from flask import current_app as app, jsonify
from domain.liste_de_lieux import liste_de_lieux


@app.route('/lieux', methods=['GET'])
def get_lieux():
    return jsonify(liste_de_lieux), 200
