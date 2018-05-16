#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import *
from modeles import modeleGNS


app = Flask( __name__ )
app.secret_key = 'GNS'


@app.route( '/parties/', methods = [ 'GET' ] )
def getLesParties() :
	
	lesParties = modeleGNS.getLesParties()
	print lesParties
	if lesParties != None :
		corpsReponse = json.dumps(lesParties)
		print corpsReponse
		reponse = make_response (corpsReponse)
		reponse.mimetype = 'application/json'
		reponse.status_code = 200
		
	else :
		reponse = make_response ()
		reponse.status_code = 404


	return reponse
	
	
@app.route( '/parties/<numeroPartie>/', methods = [ 'GET' ] )
def consulterPartie(numeroPartie) :
	
	laPartie = modeleGNS.getPartie(numeroPartie)
	print laPartie
	
	if laPartie != None :
		corpsReponse = json.dumps(laPartie)
		print corpsReponse
		reponse = make_response (corpsReponse)
		reponse.mimetype = 'application/json'
		reponse.status_code = 200
		
	else :
		reponse = make_response ()
		reponse.status_code = 404 

	return reponse


@app.route( '/parties/<numeroPartie>/', methods = [ 'DEL' ] )
def annulerPartie(numeroPartie) :
	
	laPartie = modeleGNS.supprimerPartie(numeroPartie)
	print laPartie
	
	if laPartie != None :
		corpsReponse = json.dumps(lesParties)
		print corpsReponse
		reponse = make_response (corpsReponse)
		reponse.mimetype = 'application/json'
		reponse.status_code = 200
		
	else :
		reponse = make_response ()
		reponse.status_code = 404 

	return reponse
	
@app.route( '/parties/', methods = [ 'POST' ] )
def initierPartie() :
	
	donneesJSON = request.data
	print donneesJSON
	donneesDict = json.loads(donneesJSON)
	print donneesDict
	
	#laPartie = modeleGNS.creerPartie(numeroInitiateur, numeroCouleurInitiateur)
	#print laPartie
	
	if "Imane" != None :
		#corpsReponse = json.dumps(lesParties)
		#print corpsReponse
		#reponse = make_response (corpsReponse)
		reponse = make_response ()
		reponse.mimetype = 'application/json'
		reponse.status_code = 201
		
	else :
		reponse = make_response ()
		reponse.status_code = 404 

	return reponse
	


if __name__ == '__main__' :
	app.run( debug = True , host = '0.0.0.0' , port = 5000 )
