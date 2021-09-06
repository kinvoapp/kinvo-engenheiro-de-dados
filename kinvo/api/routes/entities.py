from flask import Blueprint


entitybp = Blueprint("entitybp", __name__)


@entitybp.route('/list', methods=['GET'])
def list_entities(self):
    return {}, 200
