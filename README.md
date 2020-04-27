# Diabetyk_projekt

 
## Funkcjonalności aplikacji:
* Dodanie nowej pozycji poziomu cukru.
* Wyszukanie pomiaru po dacie lub wartości .
* Zapis i wczytywanie pomiarów przy zamknięciu/otwarciu programu.
* Zapis pomiarów do pliku pod zadaną ścieżkę.
* Statystyka pomiarów.
* Jedna zaproponowane przez grupę.
 
## Założenia Projektu : 
Wykonanie aplikacji która pomoże ludziom chorym monitorować poziom cukru we krwi na przestrzeni czasu oraz przyswojenie technik organizacji pracy w zespole za pomocą aplikacji takich jak Trello, GitHub oraz Google Dysk.


## Czynności do wykonania :
- [x] Zapoznanie się z problematyką projektu
- [ ] Dostosowanie środowisk do pracy grupowej
- [ ] Przypomnienie sobie środowiska jakim jest  Python i nauka programowania strukturalnego
- [x] Podział pracy w grupie
- [ ] Wspólne analizowanie wykonanych zadań
- [ ] Połączenie zebranych materiałów 


## Propozycje dodatkowej funkcji :
* Przypomnienia o pomiarze
* Ostrzeganie przy wejściu do aplikacji o wyższych ostatnio poziomach cukru
* Podświetlanie niepokojących statystyk
* Możliwość przesyłania statystyk np. do lekarza
* Interpretowanie wyniku na bieżąco ( np. stan wyższego ryzyka itd. )

## Wstępny szkielet programu:
```
main()
{
    wczytywanie danych zapisanych z ostatnich pomiarów()
    ostrzeżenie()
    Menu(){ 
  
        Dodaj pomiar()
        Wyszukaj pomiar()
        Zobacz statystyki()
        Eksportuj dane()
        Wyjście
  }
}
```
#### Spotkanie 18.04.2020r.

Na spotkaniu ustaliliśmy plan działania na najbliższe tygodnie pracy. Doszliśmy do porozumienia odnośnie terminu regularnych spotkań. **Głównym tematem był wybór komunikatora** do pracy przy naszym projekcie oraz portalu do współdzielenia plików.  Najlepszymi spośród dostępnych okazały się **Trello oraz GitHub**. Wybraliśmy Trello, ponieważ posiada przejrzysty interfejs co wspomaga orientowanie się w poszczególnych zadaniach i listach. GitHub natomiast jest narzędziem, które posiada szeroką gamę zastosowań. Nie tylko jest idealnym rozwiązaniem do szybkiego i bezproblemowego dzielenia się owocami pracy programistycznej ale również innych plików takich jak na przykład właśnie ta dokumentacja. Jedną z wielu jego zalet jest możliwość dodawania komentarzy przy każdym aktualizowaniu plików. Wprowadza to ład w projekcie informując innych użytkowników o potencjalnych zmianach. Co więcej dodając takowe zmiany nie musimy przenosić nigdzie plików jedynie przesłać je za pomocą prostych komend.

#### Spotkanie 27.04.2020r.
Po konsultacji z prowadzącym zespołu projektowego za pomocą MSTeams ustaliliśmy następujące rzeczy  :
* Zamierzamy użyć Python Pandas do tworzenia bazy danych
* Organizacja dokumentów na githubie w celu zwiększenia przejrzystości
* Wsparcie w tworzeniu statystyk w Matplotllib.org 
* Ostateczny wybór TUI przy wsparciu             pygames 
* Będziemy spotykać się w każdy poniedziałek i tworzyć notatki ze spotkań


Dostaliśmy także materiały pomocne do wykonania projektu:

[GitHub](https://education.github.com/)

[Pandas](https://pandas.pydata.org/) W celu pobrania "pip install pandas"

[Matplotlib](https://matplotlib.org/)

[Pygame](https://www.pygame.org/docs/tut/PygameIntro.html)

[Panda- Youtube tutorial](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&fbclid=IwAR1Mxve1U8rP_K5AgiFMHl2ibu0ewacf0OmPhqwkSTD1wvaFwvuhyfP4sHo)

