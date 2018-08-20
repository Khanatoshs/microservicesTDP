from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

artists = [
    {
        "name": "Queen",
        "age": 42,
    },
    {
        "name": "Bon Jovi",
        "age": 32,
    },
    {
        "name": "U2",
        "age": 22,
    }
]

class artist(Resource):
	def get(self):
		return artists

class artist_Name(Resource):
    def get(self, name):
        for artist in artists:
            if(name == artist["name"]):
                return artist, 200
        return "artist not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        args = parser.parse_args()

        for artist in artists:
            if(name == artist["name"]):
                return "artist with name {} already exists".format(name), 400

        artist = {
            "name": name,
            "age": args["age"]
        }
        artists.append(artist)
        return artist, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for artist in artists:
            if(name == artist["name"]):
                artist["age"] = args["age"]
                return artist, 200
        
        artist = {
            "name": name,
            "age": args["age"]
        }
        artists.append(artist)
        return artist, 201

    def delete(self, name):
        global artists
        artists = [artist for artist in artists if artist["name"] != name]
        return "{} is deleted.".format(name), 200
     
api.add_resource(artist, "/artist")
api.add_resource(artist_Name, "/artist/<string:name>")

app.run(host='0.0.0.0', port=80)