# Dashboard administracyjny dla sklepu internetowego

# Instrukcja uruchomienia aplikacji

Poniżej przedstawione są kroki, które należy wykonać, aby uruchomić aplikację na swoim lokalnym środowisku.

## Wymagania

- Python w wersji 3.10 lub nowszej
- Pakiet `virtualenv` (można zainstalować globalnie za pomocą: `pip install virtualenv`)

## Kroki
Podczas wykonywania poniższych kroków należy znajdować się w głównym folderze aplikacji.

### 1. Skopiowanie pliku .env

Skopiuj plik `.env.example` i zmień jego nazwę na `.env`. Plik ten zawiera wszystkie potrzebne zmienne środowiskowe.

```bash
cp .env.example .env
```
Domyślnie ustawione są parametry bazy danych SQLite, ponieważ nie wymaga to żadnych dodatkowych instalacji.
W razie potrzeby można zmienić ustawienia pod inny silnik.

### 2. Stworzenie środowiska wirtualnego
Utwórz środowisko wirtualne za pomocą `virtualenv`:

```bash
virtualenv venv
```

Aktywuj środkowisko wirtualne:

- Na systemie Linux/macOS:
    ```bash
    source venv/bin/activate
    ```
- Na systemie Windows:
    ```bash
    venv\\Scripts\\activate
    ``` 

### 3. Instalacja zależności
Zainstaluj wszystkie wymagane biblioteki z pliku `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Migracje bazy danych
Przed uruchomieniem aplikacji, wykonaj migracje bazy danych:

```bash
python manage.py migrate
```

### 5. Uruchomienie aplikacji
Aby uruchomić serwer deweloperski Django, użyj poniższej komendy:

```bash
python manage.py runserver
```
Aplikacja będzie dostępna pod adresem: http://127.0.0.1:8000