from . import api_bp
from ..models import Status
from .helper_json import json_response

url_head = "/api/v1.0/"

@api_bp.route('/statuses', methods=['GET'])
def list_statuses():
    statuses = Status.get_all()
    return json_response(statuses)
