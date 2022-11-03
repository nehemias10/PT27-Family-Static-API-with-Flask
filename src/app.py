"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }
    return jsonify(members), 200

    
@app.route('/members/<int:member_id>', methods=['GET'])
def getOneMember(member_id):
    getMember = jackson_family.get_member(member_id)
    return getMember, 200

@app.route('/members/<int:member_id>', methods=['DELETE'])
def deleteOneMember(member_id):
    deleteMember = jackson_family.delete_member(member_id)
    return deleteMember, 200


@app.route('/members', methods=['POST'])
def add_member():
   member = request.get_json()
   if (member is None):
        return 'Falta información'
   if ('age' not in member):
        return 'Falta edad'
   if ('name' not in member):
        return 'Falta nombre'
   if ('lucky_numbers' not in member):
       return 'Falta lucky number'
   elif member["age"] and member["name"] and member["lucky_numbers"]:
        newMember = jackson_family.add_member(member)
        return newMember, 200
    
    
    
    

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)