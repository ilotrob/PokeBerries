from flask import Flask, Response
from processor import Processor
import json
import base64

URL = "https://pokeapi.co/api/v2/berry/?limit=200"

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

processor = Processor(URL)

@app.route('/')
def greeting_page():
    """
    Returns a basic explanation on how to use the API in html format.
    """

    message = """
    <!DOCTYPE html>
    <html>
    <body>

    <title>PokeBerries (How to use)</title>

    <h1>/allBerryStats</h1>
    <p>Use to get information from all the berries.</p>

    <br>
    <br>

    <h1>/growthTimesHistogram</h1>
    <p>Use to generate and show an image of the histogram of the growth times of the berries.</p>

    </body>
    </html>
    """
    return message

@app.route('/growthTimesHistogram')
def histogram_presentation():

    html = processor.get_histogram_html()    

    return html

@app.route('/allBerryStats')
def show_berries_info():

    response = processor.get_berries_info()
    
    return Response(json.dumps(response, indent=4), content_type="application/json")


if __name__ == '__main__':
    app.run()