from flask import render_template, redirect, request, jsonify

"""
	Print out to user "hello, world" message format by string

	view_home(void)
	
	Parameters: void
	Return type: string

"""
def view_txt_home():
	return "Hello, world"

"""
	Print out to user index page format by html

	view_home(void)
	
	Parameters: void
	Return type: string

"""
def view_render_home():
	return render_template('index.html')

def view_hello_information():
	if not request.is_json:
		raise Exception("invalid parameter")

def internal_server_error(e):
	return jsonify(str(e)), 500

def not_found_page(e):
	return jsonify(str(e)), 404

def bad_request(e):
	return jsonify(str(e)), 400