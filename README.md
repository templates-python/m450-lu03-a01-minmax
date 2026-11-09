# M450 LU03.A01 - Kleinste und grösste Zahl finden

Schreibe die Unittests für das Programm `main.py`.

Wiki: <https://wiki.bzz.ch/modul/m450/learningunits/lu03/aufgaben/kleingross>

## Ausgangslage

In `main.py` ist das Programm fertig vorgegeben – es muss **nicht** verändert
werden:

| Funktion | Verhalten |
| --- | --- |
| `user_input()` | liest Zahlen ein, bis `0` eingegeben wird, ruft `min_max` auf und gibt die Liste zurück |
| `random_numbers()` | erzeugt 15 Zufallszahlen zwischen -999 und 999, ruft `min_max` auf und gibt die Liste zurück |
| `min_max(numbers)` | gibt die kleinste und die grösste Zahl der Liste je auf einer eigenen Zeile aus |

## Auftrag

In `main_test.py` sind drei Testfunktionen vorbereitet. Die Kommentare
`# TODO ...` beschreiben jeweils, welche Situation zu testen ist.

Schreibe den Code für den Aufruf der Funktionen und die Auswertung des
Resultats. Für die Konsolen-Ausgabe brauchst du `capsys`, für die
Benutzereingaben `monkeypatch`.

## Lokal testen

```bash
pip install -r requirements.txt
pytest
python _run_pylint.py
```

## Bewertung

| Teil | Punkte |
| --- | --- |
| Unittests (`test_random`, `test_userinput_normal`, `test_userinput_special`) | 3 |
| Linting von `main_test.py` | 2 |
| **Total** | **5** |

## Abgabe

Die Abgabe erfolgt durch den Push ins GitHub-Repository. Jeder Push wird
automatisch bewertet.
