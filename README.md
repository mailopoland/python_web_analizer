# python_web_analizer


1) Demon notyfikacji www. Demon (aplikacja nadzorująca, działająca w tle w systemie) który będzie nadzorować zadane strony www i pozwoli wykonywać określone akcje gdy strona się zmieni w określony sposób. Możemy więc dodawać zasady według składni określonej w pkt 3.


2) Aplikacje uruchamiamy poprzez plik webmonitoring.py (komenda: "python webmonitoring.py"). 

a) Aby uzyskać dostępne komendy należy uruchomić aplikacje poprzez: "python webmonitoring.py help"


3) *todo* “REGUŁA -> AKCJA” (wg. jakiejś, ustalonej składni) np. 

(SITE CHANGED) AND (TEXT CONTAINS “oceny”) -> MESSAGE(“Sa oceny!”)


4) Użyte dodatkowe biblioteki
- python-daemon 2.0.5 (https://pypi.python.org/pypi/python-daemon)