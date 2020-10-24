import httplib
import xdrlib
import time
import math

AUTH_SERVER = "sensorcloud.microstrain.com"

#samplerate types
HERTZ = 1
SECONDS = 0

def authenticate_key(device_id, key):
	"""
	authenticate with sensorcloud and get the server and auth_key for all subsequent api requests
	"""
	conn = httplib.HTTPSConnection(AUTH_SERVER)

	headers = {"Accept": "application/xdr"}
	url = "/SensorCloud/devices/%s/authenticate/?version=1&key=%s"%(device_id, key)
	
	print "authenticating..."
	conn.request('GET', url=url, headers=headers)
	response =conn.getresponse()
	print response.status, response.reason
	
	#if response is 200 ok then we can parse the response to get the auth token and server
	if response.status is httplib.OK: 
		print "Credential are correct"
			
		#read the body of the response
		data = response.read()
		
		#response will be in xdr format. Create an XDR unpacker and extract the token and server as strings 
		unpacker = xdrlib.Unpacker(data)
		auth_token = unpacker.unpack_string()
		server = unpacker.unpack_string()
		
		print "unpacked xdr.  server:%s  token:%s"%(server, auth_token)
		
		return server, auth_token

def authenticate_alternate(device_id, username, password):
	"""
	authenticate with sensorcloud and get the server and auth_key for all subsequent api requests
	"""
	conn = httplib.HTTPSConnection(AUTH_SERVER)

	headers = {"Accept": "application/xdr"}
	url = "/SensorCloud/devices/%s/authenticate/?version=1&username=%s&password=%s"%(device_id, username, password)
	
	print "authenticating..."
	conn.request('GET', url=url, headers=headers)
	response =conn.getresponse()
	print response.status, response.reason
	
	#if response is 200 ok then we can parse the response to get the auth token and server
	if response.status is httplib.OK: 
		print "Credential are correct"
			
		#read the body of the response
		data = response.read()
		
		#response will be in xdr format. Create an XDR unpacker and extract the token and server as strings 
		unpacker = xdrlib.Unpacker(data)
		auth_token = unpacker.unpack_string()
		server = unpacker.unpack_string()
		
		print "unpacked xdr.  server:%s  token:%s"%(server, auth_token)
		
		return server, auth_token
