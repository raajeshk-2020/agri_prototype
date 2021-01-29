import pandas as pd
from flask import Flask, request, render_template, url_for
import urllib.request
import logging

def get_typeahead_products():
	product_data = pd.read_csv("final_products_data.csv")
	return list(product_data['Product_Name'].str.capitalize())

agrimacy_prototype_app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@agrimacy_prototype_app.route('/')
@agrimacy_prototype_app.route('/home')
def home():
	agrimacy_prototype_app.logger.info('Processing home request started')
	# Display the movies as user types in the name of a movie 
	type_ahead_products = get_typeahead_products()
	return render_template('index.html', type_ahead_products=type_ahead_products)
	agrimacy_prototype_app.logger.info('processing home request completed')

if __name__ == "__main__":
	agrimacy_prototype_app.run(debug=True, use_reloader=False)
