CREATE DATABASE Sterrenstelsel

CREATE TABLE Planeten (
    Naam varchar(255)
);

INSERT INTO planeten
	(Naam)
VALUES
	('Zon'), 
    ('Mercurius'), 
    ('Venus'), 
    ('Aarde'), 
    ('Mars');

SELECT * FROM planeten;

TRUNCATE TABLE planeten;

ALTER TABLE planeten
ADD diameter INT(11),
ADD afstand INT(11),
ADD massa INT(11);

INSERT INTO planeten
    (naam, diameter, afstand, massa)
VALUES
    ('Zon', 1392000, 0, 332946), 
    ('Mercurius', 4880, 57910000, 0), 
    ('Venus', 12104, 108208930, 1), 
    ('Aarde', 12756, 149597870, 1), 
    ('Mars', 6794, 227936640, 0);

ALTER TABLE planeten MODIFY Naam varchar(255) NOT NULL;
ALTER TABLE planeten MODIFY afstand INT(11) NOT NULL;
ALTER TABLE planeten MODIFY diameter INT(11) NOT NULL;
ALTER TABLE planeten MODIFY massa INT(11) NOT NULL;

ALTER TABLE 
    planeten
ADD bezoekdatum DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

