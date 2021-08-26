from flask import render_template, redirect, request, jsonify
from module import packmsg as pkm
from module import pymongo as mg
from uuid import uuid4
import json

def get_initalize_information():
	# Json Type Check
	if not request.is_json:
		raise ValueError("invalid parameter")

	# Parameter Exist Check
	data = json.loads(request.data)

	if 'cpu_id' not in data:
		raise ValueError("No DeviceId for target")

	return pkm.GetRowsData(0, mg.find_gentry_information(data['cpu_id']))

def set_inout_history():
	if not request.is_json:
		raise ValueError("invalid parameter")

	data = json.loads(request.data)
	if 'serial' not in data:
		raise ValueError("No Serial for target")

	if 'proj_id' not in data:
		raise ValueError("No ProjectSiteCode for target")

	if 'data' not in data:
		raise ValueError("No Data for target")

	histories = []
	for x in data['data']:
		x['rcd_id'] = str(uuid4())
		x['gant_id'] = data['gant_id']
		x['gant_name'] = data['gant_name']
		x['serial'] = data['serial']
		x['proj_id'] = data['proj_id']
		x['proj_name'] = data['proj_name']
		x['desc'] = ""
		x['status'] = data['status']
		histories.append(x)

	data = [{
		"MsgCode":(0x2000 + len(mg.insert_history_information(histories))),
		"Message":"Update succeed."
	}]
	return pkm.GetRowsData(0, data)

	

def internal_server_error(e):
	return jsonify(pkm.GetErrorMsg(-2, 0x30FF, str(e))), 500

def not_found_page(e):
	return jsonify(pkm.GetErrorMsg(-2, 0x30FF, str(e))), 404

def bad_request(e):
	return jsonify(pkm.GetErrorMsg(-2, 0x30FF, str(e))), 400