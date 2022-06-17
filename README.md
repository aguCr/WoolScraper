# WoolScraper

## Ausführen:
- Als PyCharm Projekt öffnen
- Im Terminal cd woolscraper eingeben
- in diesem Verzeichnis : scrapy crawl wool
- optional: scrapy crawl wool -o IrgendeinenDateinamen.Endung
- Die Endung kann bspw. .json/.jsonlines/.csv/.xml sein
- Dadurch werden die gescrapten Inhalte in eine Datei geschrieben. Das Funktioniert aber nur einmal da beim 2ten mal in die Datei geschrieben wird, anstatt diese zu Überschreiben.
  Die Inhalte werden zudem in einer SQLite Datenbank gespeichert (WoolScraper/Wools.db) die man zum Beispiel mit DB Browser for SQLite ansehen kann. Die darin enthaltene Tabelle wird bei 
  jedem Befehl neu erstellt.
 - ![screenshotDB](https://user-images.githubusercontent.com/105021682/174255620-6648d14b-228f-4bef-a096-33c2139554df.png)

  
  ## Mein Vorgehen
  - Pycharm Projekt + virtual environment erstellt
  - Im PyCharm Terminal: pip install scrapy (Webscralling Framework)
  - Im PyCharm Terminal: scrapy startproject WoolScraper (erstellt einige Ordner + Dateien)
  - In der Generierten Itemklasse wird das  Objekt definiert, welches ausgelesen werden soll (dadurch kann man es beliebig erweitern) oder weitere Klassen ergänzen 
  - Im Spiders Unterorder wurde der scrapper geschrieben der die Webseite ausliest
  - Dann habe ich einige Tests geschrieben und da diese glücklicherweise die ersten Paar male nicht durchgelaufen sind, sind mir einige Fehler und Schwachstellen aufgefallen
  - Als nächstes habe ich die Zeilen 65-67 aus der Settings-Datei auskommentiert um die Pipeline zu aktiveren, um die Datenbank anzubinden
  - In der Pipelines Datei ist dann auch der Code für die Datenbank, auf die Empfehlung von PyCharm habe ich das SQLDialect auf Generic SQL umgestellt
  
  
  ## Warum Scrapy ?
  - Vorteil von Scrapy ist die Performance, da man asynchron mehrere GET Request parallel senden kann.
  - Beautiful Soup kann aufgrund der externen Dependencies in größeren Projekten problematisch sein
  
  
   ## Wie kann man weitere Marken + Artikel suchen?
  - ![grafik](https://user-images.githubusercontent.com/105021682/174257381-62a8952b-6340-456a-b464-386a961d3a00.png)
  - Scrapy benötigt einen Namen zum scrapen: wool 
  - sowie eine Adresse: Hier sind am ende zwei Klammern {} um weitere Parameter zu übergeben
  - In einem Dictionary werden alle Marken als Key und die Artikel als Liste eingefügt, eigene Methoden erstellen daraus passende requests die parallen ausgeführt werden.
  - ![grafik](https://user-images.githubusercontent.com/105021682/174258776-bdb774a0-c704-407d-98ff-877817f43ddc.png)
  -
  
  ## Anmerkungen
  - Mit diesem Lösungsansatz bin ich nicht ganz zufrieden da es ziemlich Fehleranfällig sein kann, aber da fehlt einfach das nötige Know-How
  - Auf die Angabe der Lieferzeit habe ich verzichtet, da diese nicht Abhängig vom Produkt sondern vom Land ist, und mir unklar war, was ich genau auslesen sollte
  - Die Marke Hahn existiert nicht, wird aber dennoch, wie man im Screenshot sehen kann, gesucht

