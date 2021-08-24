from module import app
from module import views


# Secret key for session 
app.secret_key = ""

app.register_error_handler(400, views.bad_request)
app.register_error_handler(405, views.bad_request)
app.register_error_handler(404, views.not_found_page)
app.register_error_handler(500, views.internal_server_error)

"""
	add_url_rule(rule, endpoint=None, view_func=None, provide_automatic_options=None, **options)
	
	rule (str) – The URL rule string.
	endpoint (Optional[str]) – The endpoint name to associate with the rule and view function. Used when routing and building URLs. Defaults to view_func.__name__.
	view_func (Optional[Callable]) – The view function to associate with the endpoint name.
	provide_automatic_options (Optional[bool]) – Add the OPTIONS method and respond to OPTIONS requests automatically.
	options (Any) – Extra options passed to the Rule object. (Rule object refer : https://werkzeug.palletsprojects.com/en/2.0.x/routing/#werkzeug.routing.Rule)
"""

# Get Device information
app.add_url_rule('/2E1E9B5D6B3E378F81FB2706BDE8AE3D', methods=['POST',], view_func=views.get_device_information)

# Get Device initialze information
app.add_url_rule('/4CF2C6704161CB5C3DCB0FFE9A52B4EC', methods=['POST',], view_func=views.get_initalize_information)

# Get Device Account information
app.add_url_rule('/C8CDC5F3D46143B664D72D039B5832FC', methods=['POST',], view_func=views.get_device_information)

# Insert Device History information
app.add_url_rule('/57C5A9EEA786CD47EE17D720420493FA', methods=['POST',], view_func=views.get_device_information)

# Get Device KeepAlive Status
app.add_url_rule('/82D5984C2A2AD4C62CAF1DD073B1C91C', methods=['POST',], view_func=views.get_device_information)


"""
	run(host=None, port=None, debug=None, load_dotenv=True, **options)

	host (Optional[str]) – the hostname to listen on. Set this to '0.0.0.0' to have the server available externally as well. Defaults to '127.0.0.1' or the host in the SERVER_NAME config variable if present.
	port (Optional[int]) – the port of the webserver. Defaults to 5000 or the port defined in the SERVER_NAME config variable if present.
	debug (Optional[bool]) – if given, enable or disable debug mode. See debug.
	load_dotenv (bool) – Load the nearest .env and .flaskenv files to set environment variables. Will also change the working directory to the directory containing the first file found.
	options (Any) – the options to be forwarded to the underlying Werkzeug server. See werkzeug.serving.run_simple() for more information.
"""
app.run(host='127.0.0.1', port='8080', debug=False)