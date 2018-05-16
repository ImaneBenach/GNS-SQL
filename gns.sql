#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------

CREATE DATABASE GNS ;
#------------------------------------------------------------
# Table: Joueur
#------------------------------------------------------------

CREATE TABLE Joueur(
        numeroJoueur Int NOT NULL ,
        nomJoueur    Varchar (25) ,
        mdpJoeur     Varchar (25) ,
        PRIMARY KEY (numeroJoueur )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Couleur
#------------------------------------------------------------

CREATE TABLE Couleur(
        numeroCouleur Int NOT NULL ,
        nomCouleur    Varchar (25) ,
        PRIMARY KEY (numeroCouleur )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Partie
#------------------------------------------------------------

CREATE TABLE Partie(
        numeroPartie    Int NOT NULL ,
        dateCreation    Date ,
        numeroJoueur    Int ,
        numeroJoueur_1  Int ,
        numeroJoueur_2  Int ,
        numeroJoueur_3  Int ,
        numeroCouleur   Int ,
        numeroCouleur_4 Int ,
        PRIMARY KEY (numeroPartie )
)ENGINE=InnoDB;

ALTER TABLE Partie ADD CONSTRAINT FK_Partie_numeroJoueur FOREIGN KEY (numeroJoueur) REFERENCES Joueur(numeroJoueur);
ALTER TABLE Partie ADD CONSTRAINT FK_Partie_numeroJoueur_1 FOREIGN KEY (numeroJoueur_1) REFERENCES Joueur(numeroJoueur);
ALTER TABLE Partie ADD CONSTRAINT FK_Partie_numeroJoueur_2 FOREIGN KEY (numeroJoueur_2) REFERENCES Joueur(numeroJoueur);
ALTER TABLE Partie ADD CONSTRAINT FK_Partie_numeroJoueur_3 FOREIGN KEY (numeroJoueur_3) REFERENCES Joueur(numeroJoueur);
ALTER TABLE Partie ADD CONSTRAINT FK_Partie_numeroCouleur FOREIGN KEY (numeroCouleur) REFERENCES Couleur(numeroCouleur);
ALTER TABLE Partie ADD CONSTRAINT FK_Partie_numeroCouleur_4 FOREIGN KEY (numeroCouleur_4) REFERENCES Couleur(numeroCouleur);
