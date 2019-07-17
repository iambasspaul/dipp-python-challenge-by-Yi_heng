"""
Text Blueprint
"""
from flask import Blueprint, jsonify, Flask, render_template
from config.config import Config
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import json

bp_text = Blueprint('text', __name__, url_prefix='/') # pylint: disable=invalid-name

#Load origen text.json
with open('./text.json', 'r') as rf:
  data = json.load(rf)

textbox = data["facebook-header"]["copy"]
box_xstart = data["facebook-header"]["x_start"]
box_ystart = data["facebook-header"]["y_start"]
box_mwidth = data["facebook-header"]["max_width"]
box_mhight = data["facebook-header"]["max_height"]
box_font = data["facebook-header"]["font_url"]

#Load after split.json
with open('./split.json', 'r') as sp:
  splitdata = json.load(sp)

splitcontent0 = splitdata["facebook-header"]["splits"][0]["content"]
splitcontent1 = splitdata["facebook-header"]["splits"][1]["content"]
splitcontent2 = splitdata["facebook-header"]["splits"][2]["content"]
splitcontent3 = splitdata["facebook-header"]["splits"][3]["content"]
splitfont_size0 = splitdata["facebook-header"]["splits"][0]["font_size"]
splitfont_size1 = splitdata["facebook-header"]["splits"][1]["font_size"]
splitfont_size2 = splitdata["facebook-header"]["splits"][2]["font_size"]
splitfont_size3 = splitdata["facebook-header"]["splits"][3]["font_size"]
splitx0 = splitdata["facebook-header"]["splits"][0]["x"]
splitx1 = splitdata["facebook-header"]["splits"][1]["x"]
splitx2 = splitdata["facebook-header"]["splits"][2]["x"]
splitx3 = splitdata["facebook-header"]["splits"][3]["x"]
splity0 = splitdata["facebook-header"]["splits"][0]["y"]
splity1 = splitdata["facebook-header"]["splits"][1]["y"]
splity2 = splitdata["facebook-header"]["splits"][2]["y"]
splity3 = splitdata["facebook-header"]["splits"][3]["y"]
coordinatesheight = splitdata["facebook-header"]["coordinates"]["height"]
coordinateswidth = splitdata["facebook-header"]["coordinates"]["width"]
coordinatesx = splitdata["facebook-header"]["coordinates"]["x"]
coordinatesy = splitdata["facebook-header"]["coordinates"]["y"]
font_url = splitdata["facebook-header"]["splits"][0]["font_url"]

class MyForm(FlaskForm):
   name = StringField("import text:", validators=[DataRequired()],
           default=textbox)
   submit = SubmitField("split")


@bp_text.route('/' + Config.API_BASE_PATH + '/boxfit', methods=['GET', 'POST'])
def api_box_fit():
    """
    API Fit the text inside the box route
    """
    html=""
    #return jsonify("This should be your output")
    form = MyForm()
    if form.validate_on_submit():
       outStr = '<html><head><title>dipp challenge splits</title>'
       outStr += '<style>@font-face {font-family: dippfont; src: url('+font_url+');}'
       outStr += ' .coordinates{height: '+str(coordinatesheight)+'px; width: '+str(coordinateswidth)+'px; top: '+str(coordinatesx)+'px; left: '+str(coordinatesy)+';px}'
       outStr += ' .coordinates.splits1 {font_size: '+str(splitfont_size0)+'px; font-family: dippfont, serif; top: '+str(splitx0)+'px; left: '+str(splity0)+'px}'
       outStr += ' .coordinates.splits2 {font_size: '+str(splitfont_size1)+'px; font-family: dippfont, serif; top: '+str(splitx1)+'px; left: '+str(splity1)+'px}'
       outStr += ' .coordinates.splits3 {font_size: '+str(splitfont_size2)+'px; font-family: dippfont, serif; top: '+str(splitx2)+'px; left: '+str(splity2)+'px}'
       outStr += ' .coordinates.splits4 {font_size: '+str(splitfont_size3)+'px; font-family: dippfont, serif; top: '+str(splitx3)+'px; left: '+str(splity3)+'px}'
       outStr += ' </style></head><body>'
       outStr += '<h1>input text：{}'.format(form.name.data) + '</h1><BR>'
       outStr += 'split result：<BR><div class="coordinates">'
       outStr += '<div class="coordinates splits1">'+splitcontent0+'</div>'
       outStr += '<div class="coordinates splits2">'+splitcontent1+'</div>'
       outStr += '<div class="coordinates splits3">'+splitcontent2+'</div>'
       outStr += '<div class="coordinates splits4">'+splitcontent3+'</div>'
       outStr += '</div></body></html>'
       return outStr
    else:
       return render_template('submit.html', runForm=form)
