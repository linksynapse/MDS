from flask import render_template, redirect, request, jsonify
from module import packmsg as pkm
from module import pymongo as mg
from uuid import uuid4
import datetime
import json

def get_initalize_information():
	# Json Type Check
	if not request.is_json:
		raise ValueError("invalid parameter")

	# Parameter Exist Check
	data = json.loads(request.data)

	if 'cpu_id' not in data:
		raise ValueError("No cpu_id for target")

	if 'pubaddr' not in data:
		raise ValueError("No pubaddress for target")

	if 'nataddr' not in data:
		raise ValueError("No nataddress for target")

	if 'macaddr' not in data:
		raise ValueError("No macaddress for target")

	records = mg.find_gentry_information(data['cpu_id'],data['nataddr'],data['pubaddr'],data['macaddr'])
	if(len(records) > 0):
		return pkm.GetRowsData(0, mg.find_gentry_information(data['cpu_id'],data['nataddr'],data['pubaddr'],data['macaddr']))
	else:
		return pkm.GetRowsMsg(-1, 0x0100, 'No records')

	

def get_device_account():
	if not request.is_json:
		raise ValueError("invalid parameter")

	data = json.loads(request.data)
	if 'proj_id' not in data:
		raise ValueError("No Project id for target")

	return pkm.GetRowsData(0, mg.find_users_information(data['proj_id']))

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
		x['created_on'] = datetime.datetime.strptime(x['created_on'], "%Y-%m-%dT%H:%M:%S.%fZ")
		histories.append(x)

	print(histories)

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