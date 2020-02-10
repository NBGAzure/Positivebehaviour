from flask import Flask, render_template, make_response
import pdfkit

app = Flask(__name__)
import pdfkit

app = Flask(__name__)


@app.route('/<name>/<location>')
def pdf_template(naem, Location):
    rendered = render_template('fbabase.html', )
