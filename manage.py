#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template(("home.html"))

@app.route("/result",methods=["POST","GET"])
def result():
    output = request.form.to_dict()
    name = output["name"]
    return render_template("home.html",name = name)

def main():
    """Run administrative tasks.
    To run the program, create a configuration in your IDE to run this file
    with the parameter 'runserver'
    OR
    enter the following command in the Command Line:
                            python manage.py runserver
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)




if __name__ == '__main__':
    #main()
    app.run(debug=True, port=2000)

