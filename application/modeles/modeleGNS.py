#!/usr/bin/python
# -*- coding: utf-8 -*-


import mysql.connector


connexionBD = None

def getConnexionBD() :
	global connexionBD
	try :
		if connexionBD == None :
			connexionBD = mysql.connector.connect(
					host = 'localhost' ,
					user = 'root' ,
					password = 'azerty' ,
					database = 'GNS'
				)
		return connexionBD
	except :
		return None
		
		
def getLesParties() :
	try :
		
		print "Ok1"
		curseur = getConnexionBD().cursor()
		print "Ok2"
		requete = '''
					select *
					from Partie
					inner join Joueur
					on Partie.numeroJoueur = Joueur.numeroJoueur
					inner join Couleur
					on Partie.numeroCouleur = Couleur.numeroCouleur
				'''

		print "Ok3"
		curseur.execute( requete , () )
		print "Ok4"
		tuples = curseur.fetchall()
		print "Ok5"
		lesParties = []
		for unTuple in tuples :
			unePartie = {}
			unePartie[ 'numeroPartie' ] = unTuple[ 0 ]
			unePartie[ 'dateCreation' ] = str(unTuple[ 1 ])
			unePartie[ 'numInitiateur' ] = unTuple[ 2 ]
			unePartie[ 'nomInitiateur' ] = unTuple[ 3 ]
			unePartie[ 'couleurInitiateur' ] = unTuple[ 4 ]
			unePartie[ 'numAdversaire' ] = unTuple[ 5 ]
			unePartie[ 'nomAdversaire' ] = unTuple[ 6 ]
			unePartie[ 'couleurAdversaire' ] = unTuple[ 7 ]
			unePartie[ 'suivant' ] = unTuple[ 8 ]
			unePartie[ 'vainqueur' ] = unTuple[ 9 ]
			lesParties.append( unePartie )
			
		curseur.close()
		return lesParties
		
	except :
		return None
		

def getPartie(numeroPartie) :
	try :
		
		curseur = getConnexionBD().cursor()
		
		requete = '''
					select *
					from Partie
					inner join Joueur
					on Partie.numeroJoueur = Joueur.numeroJoueur
					inner join Couleur
					on Partie.numeroCouleur = Couleur.numeroCouleur
					where Partie.numeroPartie = %s
				'''
		
		curseur.execute( requete , (numeroPartie , ) )
		
		unTuple = curseur.fetchone()
		
		if unTuple != None :
			unePartie = {}
			unePartie[ 'numeroPartie' ] = unTuple[ 0 ]
			unePartie[ 'dateCreation' ] = str(unTuple[ 1 ])
			unePartie[ 'numInitiateur' ] = unTuple[ 2 ]
			unePartie[ 'nomInitiateur' ] = unTuple[ 3 ]
			unePartie[ 'couleurInitiateur' ] = unTuple[ 4 ]
			unePartie[ 'numAdversaire' ] = unTuple[ 5 ]
			unePartie[ 'nomAdversaire' ] = unTuple[ 6 ]
			unePartie[ 'couleurAdversaire' ] = unTuple[ 7 ]
			unePartie[ 'suivant' ] = unTuple[ 8 ]
			unePartie[ 'vainqueur' ] = unTuple[ 9 ]
			curseur.close()
			return unePartie
		
		else :
			return None
		
		
	except :
		return None
		
def supprimerPartie(numeroPartie) :
	
	try :
		curseur = getConnexionBD().cursor()
		
		requete = '''
			delete from Partie
			where numeroPartie = %s 
			'''
			
		curseur.execute( requete , (  numeroPartie , ) )
		connexionBD.commit()
		nbTuplesTraites = curseur.rowcount
		curseur.close()
		
		return nbTuplesTraites
		
	except :
		return None
		
def creerPartie(numeroInitiateur, numeroCouleurInitiateur) :
	
	try :
		curseur = getConnexionBD().cursor()
		
		requete = '''
			update Partie as p
			create Partie = (
				select numeroPartie
				from Partie
				where p.numeroPartie = Joueur.numeroPartie
				and p.numeroPartie = %s
			)
			where numeroPartie = %s
			'''
			
		curseur.execute( requete , ( numeroPartie , numeroPartie ) )
		connexionBD.commit()
		nbTuplesTraites = curseur.rowcount
		curseur.close()
		
		return nbTuplesTraites
		
	except :
		return None		
		

if __name__ == "__main__" :
	print getConnexionBD()
	print getLesParties()
	print getPartie(2)
	print supprimerPartie(5)
