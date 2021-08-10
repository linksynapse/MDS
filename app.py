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
app.add_url_rule('/', methods=['POST',], view_func=views.view_hello_information)


"""
	run(host=None, port=None, debug=None, load_dotenv=True, **options)

	host (Optional[str]) – the hostname to listen on. Set this to '0.0.0.0' to have the server available externally as well. Defaults to '127.0.0.1' or the host in the SERVER_NAME config variable if present.
	port (Optional[int]) – the port of the webserver. Defaults to 5000 or the port defined in the SERVER_NAME config variable if present.
	debug (Optional[bool]) – if given, enable or disable debug mode. See debug.
	load_dotenv (bool) – Load the nearest .env and .flaskenv files to set environment variables. Will also change the working directory to the directory containing the first file found.
	options (Any) – the options to be forwarded to the underlying Werkzeug server. See werkzeug.serving.run_simple() for more information.
"""
app.run(host='127.0.0.1', port='8080', debug=False)