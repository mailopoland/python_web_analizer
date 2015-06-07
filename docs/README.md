# python_web_analizer

1) Demon notyfikacji www. Demon (aplikacja nadzorująca, działająca w tle w systemie) który będzie nadzorować zadane strony www i pozwoli wykonywać określone akcje gdy strona się zmieni w określony sposób. 


2) Aplikacje uruchamiamy poprzez plik webmonitoring.py (komenda: "python webmonitoring.py"). Aplikacja musi mieć prawa zapisu do swoich katalogów: 'temp' oraz 'result'

Aby uzyskać dostępne komendy i opis ich działania należy uruchomić aplikacje poprzez: 'python webmonitoring.py help'


3) Zasady określające zmianę strony i reakcje na nią dodajemy do 'settings/instructions.settings', w komentarzu na początku pliku znajdują się dokładne wytyczne odnośnie dodawania instrukcji.

Dodanie/usunięcie pliku zapamiętującego stan pierwotny danej strony (dla danej instrukcji) następuje przy pierwszym uruchomieniu po wprowadzeniu ww modyfikacji monitorowania zmian na stronach (ręcznego lub automatycznego przez daemona).

Jeżeli warunek sprawdzający daną stronę zostanie spełniony, aplikacja zapamiętuje nową wersję strony jako aktualną i w następnej iteracji sprawdza znów ustawiony warunek z tym, że już względem uaktualnionej wersji strony.


4) Wymagania:
- System operacyjny Linux
- Python 2.7.3 (nie testowany na niższych wersjach)
- Dodatkowe biblioteki z pkt. 5
- Prawa odczytu do wszystkich plików zawartych w tym folderze jak i prawa zapisu dla folderów: 'result', 'settings', 'temp'

5) Użyte dodatkowe biblioteki
- python-daemon 2.0.5 (https://pypi.python.org/pypi/python-daemon)
- urllib3 1.10.4 (https://pypi.python.org/pypi/urllib3)


6) Projekt pisany w Eclipse Luna 4.4.1 z PyDev 4.1.0. Folder .metadata umożliwia otworzenie w ww. IDE projektu.