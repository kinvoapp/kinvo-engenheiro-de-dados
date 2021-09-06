from flask import Blueprint


heartbp = Blueprint("heartbp", __name__)


@heartbp.route("/alive", methods=['GET'])
def alive():
    return {'is_alive': True}, 200
