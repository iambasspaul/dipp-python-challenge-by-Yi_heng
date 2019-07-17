"""
Scripts
"""
from flask_script import Manager
from flask import current_app
from app import create_app

from PIL import Image
from PIL import ImageDraw
from PIL import ImageChops
from PIL import ImageFont
import requests
import json

def create_my_app():
    """
    Method to create the Flask application
    """
    app = create_app()
    return app

APP = create_my_app()
manager = Manager(APP)

@manager.command
def run():
    """
    Command to run the API locally.
    """
    port = int(current_app.config['PORT'])
    host = current_app.config['HOST']
    debug = current_app.config['DEBUG']
    current_app.run(host=host, port=port, debug=debug)

@manager.command
def make_image():
    """
    Command to make the API request and use the output to create an image
    """
    payload = """
    {
        "facebook-header": {
            "copy": "dipp inc, thinking out of the box.",
            "x_start": 250,
            "y_start": 250,
            "max_width": 200,
            "max_height": 200,
            "font_url": "https://fonts.gstatic.com/s/cinzeldecorative/v7/daaHSScvJGqLYhG8nNt8KPPswUAPniZQa-lDQzCLlQXE.ttf"
        }
    }
    """

    dimensions = (700, 700)

    # Please insert your code here

    imgdata = json.loads(payload)
    imgtext = imgdata["facebook-header"]["copy"]
    imgx_start = imgdata["facebook-header"]["x_start"]
    imgy_start = imgdata["facebook-header"]["y_start"]
    imgmax_width = imgdata["facebook-header"]["max_width"]
    imgmax_height = imgdata["facebook-header"]["max_height"]
    imgfont_url = imgdata["facebook-header"]["font_url"]

    #url = 'https://fonts.gstatic.com/s/cinzeldecorative/v7/daaHSScvJGqLYhG8nNt8KPPswUAPniZQa-lDQzCLlQXE.ttf'
    r = requests.get(imgfont_url, allow_redirects=True)
    open('dippfont.ttf', 'wb').write(r.content)

    font = ImageFont.truetype("dippfont.ttf", 27 )
    im = Image.new('RGB', dimensions, (255,0,0))
    draw = ImageDraw.Draw(im)
    draw.text( (250,250), "dipp inc,", font=font )
    draw.text( (250,277), "thinking ", font=font )
    draw.text( (250,304), "out of the", font=font )
    draw.text( (250,331), "box.", font=font )
    draw.polygon([((imgx_start),(imgy_start)),((imgx_start+imgmax_width),(imgy_start)),((imgx_start+imgmax_width),(imgy_start+imgmax_height)),((imgx_start),(imgy_start+imgmax_height))], outline=(255,255,255))
    im.save( "dippoutput.png" )

if __name__ == "__main__":
    manager.run()
