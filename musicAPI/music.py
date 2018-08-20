from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

musics = [
    {
        "name": "Bohemian Rapsody",
        "artist": "Queen",
    },
    {
        "name": "We are the Champions",
        "artist": "Queen",
    },
    {
        "name": "Bad love",
        "artist": "Bon Jovi",
    }
]

class Music(Resource):
	def get(self):
		return musics

class Music_Name(Resource):
    def get(self, name):
        for music in musics:
            if(name == music["name"]):
                return music, 200
        return "Music not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("artist")
        args = parser.parse_args()

        for music in musics:
            if(name == music["name"]):
                return "Music with name {} already exists".format(name), 400

        music = {
            "name": name,
            "artist": args["artist"]
        }
        musics.append(music)
        return music, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for music in musics:
            if(name == music["name"]):
                music["artist"] = args["artist"]
                return music, 200
        
        music = {
            "name": name,
            "artist": args["artist"]
        }
        musics.append(music)
        return music, 201

    def delete(self, name):
        global musics
        musics = [music for music in musics if music["name"] != name]
        return "{} is deleted.".format(name), 200
     
api.add_resource(Music, "/music")
api.add_resource(Music_Name, "/music/<string:name>")

app.run(host='0.0.0.0', port=80)