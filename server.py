import os, sys
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response
import json
import logging


tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
conf_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'conf')
app = Flask(__name__, template_folder=tmpl_dir)
sys.path.insert(1, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app'))
import application.doctors
import application.nurses
import application.appointments
import application.medicines
import application.patient
import application.admin


# Import login details from configuration file.
with open(conf_dir + '/configuration.json') as f:
  config = json.load(f)

DATABASEURI = "postgresql://" + config['user'] + ":" + config['passphrase'] + "@35.211.155.104 /project1" 

engine = create_engine(DATABASEURI)

@app.before_request
def before_request():
  try:
    logging.debug("In-flight request: Attempting to establish connection to DB")
    g.conn = engine.connect()
    logging.debug("In-flight request: Connection established!")
  except:
    logging.ERROR("In-flight request: Error connectiong to database!")
    import traceback; traceback.print_exc()
    g.conn = None

@app.teardown_request
def teardown_request(exception):
  try:
    g.conn.close()
  except Exception as e:
    pass

@app.route('/')
def index():
  return render_template("home.html")


@app.route("/appointments/", methods=["GET"])
def appointments_render():
  return render_template("appointments.html")

@app.route("/search_appointments", methods=["POST"])
def search_appointments():
  rows = ["Date", "Time", "Duration", "Tutor Name", "Tutor ID", "Client Name", "Client ID"]
  cursor = g.conn.execute(query)
  result = []
  for c in cursor:
    result.append(dict(zip(rows, c)))
  return render_template("appointments.html", **dict(apt = result))

@app.route("/client/", methods=["GET"])
def appointments_render():
  return render_template("client.html")

@app.route("/search_tutors", methods=["POST"])
def search_tutors():
  rows = ["ID", "Name", "Email", "Location", "Gender", "Rating", "Vax Status"]
  cursor = g.conn.execute(query)
  result = []
  for c in cursor:
    result.append(dict(zip(rows, c)))
  return render_template("client.html", **dict(apt = result))

@app.route("/tutor/", methods=["GET"])
def appointments_render():
  return render_template("tutor.html")

@app.route("/search_clients", methods=["POST"])
def search_clients():
  rows = ["ID", "Name", "Email", "Location", "Gender", "Day Available", "Time Available", "Gender Preference", "Vaccination Preference"]
  cursor = g.conn.execute(query)
  result = []
  for c in cursor:
    result.append(dict(zip(rows, c)))
  return render_template("tutor.html", **dict(apt = result))

@app.route("/supervisor/", methods=["GET"])
def appointments_render():
  return render_template("supervisor.html")

@app.route("/search_supervisorinfo", methods=["POST"])
def search_supervisorinfo():
  rows = ["Date", "Time", "Duration", "Tutor Name", "Tutor ID", "Client Name", "Client ID", "Tutor Session Rating", "Client Session Rating", "Tutor Overall Rating"]
  cursor = g.conn.execute(query)
  result = []
  for c in cursor:
    result.append(dict(zip(rows, c)))
  return render_template("supervisor.html", **dict(apt = result))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()


if __name__ == "__main__":
  import click
  logging.basicConfig(filename='server.log', format= '%(asctime)s %(message)s', level=logging.DEBUG)
  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using:
        python server.py
    Show the help text using:
        python server.py --help
    """

    HOST, PORT = host, port
    print("running on %s:%d" % (HOST, PORT))
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)

  run()