# Wymagania projektu
Projekt ma być aplikacją do eksploracji danych w formie jupyter notebooka.
1. W branchu master ZAWSZE ma znajdować się działająca "produkcyjna"	aplikacja. (nawet jeżeli nic ambitnego nie robi - nie ma wywoływać błędów)
 2. Aplikacja ma mieć opis README w którym zawierają się informację o funkcjonalności aplikacji, opisu jak jej używać oraz lista niezbędnych pakietów.
 4. W aplikacji muszą znajdować się następujące funkcjonalności:
- pobieranie danych ze źródła 
- elementy data cleaning, usuwanie/analiza outleierów
- co najmniej 2 rodzaje wykresów
- co najmniej 1 test statystyczny
- co najmniej 1 zastosowanie metody Monte Carlo

Podpowiedzi:
- Warto skonfigurować plik .gitignore tak by nie commitować .ipynb_checkpoints oraz \_\_pycache__
- Jeżeli wasz dataset jest za duży by go trzymać w repozytorium należy dopisać go do .gitignore oraz w pliku README opisać skąd pobrać plik i pod jaką ścieżką go umieścić.
