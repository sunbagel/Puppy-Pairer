import psycopg2
import os
import json
from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS, cross_origin

load_dotenv()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
url = os.getenv("DATABASE_URL")

# connection = psycopg2.connect(
#     host="localhost",
#     database="flask_db",
#     user=os.environ['DB_USERNAME'],
#     password=os.environ['DB_PASSWORD'])


# @app.route("/")
# def index():
#     connection = psycopg2.connect(url)
#     return 'it works'


# GET_COL = ("""SELECT * FROM dog_profile WHERE name = %s;""")
GET_COL = ("""SELECT * FROM dog_profile;""")


connection = psycopg2.connect(url)


@app.get("/")
def home():
    return "hello world"


@app.get("/api/puppy_db")
def get_data():
    # data = request.get_json()
    # name = data["name"]
    name = 'Lulu'
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_COL)

            row_headers = [x[0] for x in cursor.description]

            row = cursor.fetchall()

            json_data = []
            # appending headers to each col value
            for result in row:
                json_data.append(dict(zip(row_headers, result)))

    return json.dumps(json_data)

# def get_colour():
#     # data = request.get_json()
#     # name = data["name"]
#     name = 'doge'
#     with connection:
#         with connection.cursor() as cursor:
#             cursor.execute(GET_COLOUR, (name,))
#             colour = cursor.fetchone()[0]

#     return {"colour": colour}
