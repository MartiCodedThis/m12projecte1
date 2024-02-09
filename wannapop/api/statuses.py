from . import api_bp
from .errors import not_found, bad_request, forbidden_access
from ..models import Status
from .helper_json import json_request, json_response, json_error_response
from flask import current_app, request

url_head = "/api/v1.0/"

@api_bp.route('/statuses', methods=['GET'])
def list_statuses():
    statuses = Status.get_all()
    return json_response(statuses)
