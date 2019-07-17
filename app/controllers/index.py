"""
Blueprints
"""
from flask import Blueprint, jsonify, redirect, url_for, render_template
from config.config import Config

bp_index = Blueprint('index', __name__, url_prefix='/') # pylint: disable=invalid-name


@bp_index.route('/', methods=['GET'])
def index():
    """
    Main route
    """
    return redirect(url_for('index.api_index'))

@bp_index.route('/' + Config.API_BASE_PATH, methods=['GET'])
def api_index():
    """
    API Main route
    """
    #return jsonify("Welcome to Dipp's Python Challenge")
    return render_template('index.html')
	


