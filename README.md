Suchmaschine, um Tiere zu finden, die eine Patenschaft suchen. Mit Filteroptionen für Entfernung, Tierheim, Tierart, Kosten und Art der Patenschaft.
Ich arbeite derzeit an Punkt 2 (Backend).

Ablauf

1. Datenbank	
•	Datenbank in „PostgreSQL“. Alle Daten über die Tiere und Tierheime befinden sich in einer Excel-Tabelle.

•	Erweiterung „PostGIS“: Speicherung, Abfrage und Bearbeitung von räumlichen Daten. Damit kann gemessen werden, welche Tiere in der gewünschten Entfernung sind.


2. Backend	
•	Python (Flask/Django) für API und Datenverarbeitung. Extrahiert Daten aus der Datenbank.


3. Frontend	
•	TKInter. 
•	Leaflet : JavaScript Bibliothek für die Darstellung interaktiver Karten. Wird die Suchergebnisse auf der Karte anzeigen.


4. Zugriff	
•	Das Projekt wird mit den Fotos als .zip geschickt. Es müssen nur Python und TKInter installiert sein. Die Datenbank wird auf dem Heroku Cloud-Plattform gehostet.

