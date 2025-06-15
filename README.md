# CoachConnect Backend

Backend per l'applicazione CoachConnect, sviluppato con Flask e PostgreSQL.

## Struttura del Progetto

```
CoachConnectBE/
├── database/           # Configurazioni e modelli del database
│   ├── __init__.py
│   └── config.py      # Configurazioni dell'applicazione
├── models/            # Modelli del database
│   └── __init__.py
├── routes/            # Route dell'API
│   └── __init__.py
├── utils/             # Funzioni di utilità
│   └── __init__.py
├── venv/              # Virtual environment Python
├── app.py            # File principale dell'applicazione
├── generate_secrets.py # Script per generare chiavi sicure
├── requirements.txt   # Dipendenze del progetto
└── .gitignore        # File e cartelle da ignorare in git
```

## Requisiti

- Python 3.13
- PostgreSQL 14
- pip (gestore pacchetti Python)

## Installazione

1. Clona il repository:
```bash
git clone <url-repository>
cd CoachConnectBE
```

2. Crea e attiva il virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Su Unix/macOS
# oppure
.\venv\Scripts\activate  # Su Windows
```

3. Installa le dipendenze:
```bash
pip install -r requirements.txt
```

4. Genera le chiavi sicure e crea il file .env:
```bash
python generate_secrets.py
```
Lo script genererà due chiavi sicure e ti chiederà se vuoi creare automaticamente il file `.env`. Se scegli 's', il file verrà creato con tutte le variabili necessarie.

5. Configura il database PostgreSQL:
- Assicurati che PostgreSQL sia in esecuzione
- Crea un database chiamato `coachconnect`
- Verifica che le credenziali nel file `.env` siano corrette

## Configurazione

Il file `.env` contiene le seguenti variabili d'ambiente:

- `DATABASE_URL`: URL di connessione al database PostgreSQL
- `SECRET_KEY`: Chiave segreta per l'applicazione Flask
- `JWT_SECRET_KEY`: Chiave segreta per i token JWT
- `JWT_ACCESS_TOKEN_EXPIRES`: Durata del token di accesso (in secondi)
- `JWT_REFRESH_TOKEN_EXPIRES`: Durata del token di refresh (in secondi)
- `FLASK_ENV`: Ambiente di esecuzione (development/production)
- `FLASK_DEBUG`: Modalità debug (True/False)

## Avvio dell'Applicazione

```bash
flask run
```

L'applicazione sarà disponibile all'indirizzo `http://localhost:5000`.

## Sviluppo

### Struttura delle Cartelle

- `database/`: Contiene le configurazioni del database e i modelli
- `models/`: Definizione dei modelli del database
- `routes/`: Endpoint dell'API
- `utils/`: Funzioni di utilità

### Convenzioni di Codice

- Utilizzare docstring per documentare funzioni e classi
- Seguire le linee guida PEP 8 per lo stile del codice
- Utilizzare type hints per le annotazioni dei tipi

## Licenza

Questo progetto è sotto licenza MIT. Vedi il file `LICENSE` per maggiori dettagli. 