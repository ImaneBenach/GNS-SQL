!-- numeroJoueur_1 = ADVERSAIRE | numeroJoueur_2 = VAINQUEUR --!

1)
 
Select *
From Partie ;
where numeroJoueur_2 is not null ;

2)

Select *
from Partie 
Where  numeroJoueur_2 is null ;


3)

Select *
From Partie
Where  numeroJoueur_1 is null ;


4)

Select *
From Partie
Where numeroJoueur = 5 
and numeroJoueur_2 is not null ;


5)
Select *
From Partie
Where numeroJoueur_2 = 5 ;

6) 
Select *
From Partie
Where numeroJoueur = 5 ;
and numeroJoueur_1 is null ;

7) Select *
from Partie 
Where  numeroJoueur = 5 
and numeroJoueur_2 is null ;

8) 
Select *
From Partie 
Where numeroJoueur_3 = 5 ;

9) 
Select *
From Partie 
Where numeroJoueur_1 is null 
And numeroJoueur != 5 ;

10) 
Select *
From Partie ;

////////// PARTIE /////////

Create table Partie (
numero int PRIMARY KEY,
creation date ,
initiateur varchar (20) ,
adversaire varchar (20) ,
vainqueur varchar (15) ,
suivant varchar (15) ,
couleurInitiateur varchar (10) ,
couleurAdversaire varchar (10) 
) ;

INSERT into Partie VALUES (1 , "1/05/18", 5, 2, 2, null, 1, 2) ;
INSERT into Partie VALUES (2 , "1/05/18", 5, 2, 5, null, 2, 1) ;
INSERT into Partie VALUES (3 , "1/05/18", 5, null, null, 5, 1, null) ;
INSERT into Partie VALUES (4 , "1/05/18", 2, null, null, null, 2, null ) ;
INSERT into Partie VALUES (5 , "2/05/18", 5, 1, null, 1, 1, 2 ) ;
INSERT into Partie VALUES (6 , "2/05/18", 5, 1, null, 5, 1, 2 ) ;
INSERT into Partie VALUES (7 , "2/05/18", 1, null, null, null, null, 2 ) ;
INSERT into Partie VALUES (8 , "2/05/18", 1, null, null, null, null, 2 ) ;
INSERT into Partie VALUES (9 , "3/05/18", 5, 2, null, 2, 1, 2 ) ;
INSERT into Partie VALUES (10 , "3/05/18", 2, 1, 2, null, 2, 1 ) ;



