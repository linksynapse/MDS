from flask import render_template, redirect, request, jsonify
from module import packmsg as pkm
from module import pymongo as mg
import json

def get_device_information():
	# Json Type Check
	if not request.is_json:
		raise ValueError("invalid parameter")

	# Parameter Exist Check
	data = json.loads(request.data)
	if 'DeviceId' not in data:
		raise ValueError("No DeviceId for target")

	if 'Version' not in data:
		raise ValueError("No Version for target")

	return pkm.GetRowsData(0, mg.find_serial(data['DeviceId']))

def get_initalize_information():
	# Json Type Check
	if not request.is_json:
		raise ValueError("invalid parameter")

	# Parameter Exist Check
	data = json.loads(request.data)
	if 'Serial' not in data:
		raise ValueError("No Serial for target")

	return pkm.GetRowsData(0, mg.find_gentry_information(data['Serial']))
	

def internal_server_error(e):
	return jsonify(pkm.GetErrorMsg(-2, 0x30FF, str(e))), 500

def not_found_page(e):
	return jsonify(pkm.GetErrorMsg(-2, 0x30FF, str(e))), 404

def bad_request(e):
	return jsonify(pkm.GetErrorMsg(-2, 0x30FF, str(e))), 400