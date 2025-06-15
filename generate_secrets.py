import secrets
import os

def generate_secrets():
    """Genera chiavi sicure per l'applicazione"""
    secret_key = secrets.token_hex(32)
    jwt_secret_key = secrets.token_hex(32)
    
    return secret_key, jwt_secret_key

def create_env_file(secret_key, jwt_secret_key):
    """Crea il file .env con tutte le variabili necessarie"""
    env_content = f"""DATABASE_URL=postgresql://postgres:Luigi2005@localhost:5433/coachconnect
SECRET_KEY={secret_key}
JWT_SECRET_KEY={jwt_secret_key}
JWT_ACCESS_TOKEN_EXPIRES=900
JWT_REFRESH_TOKEN_EXPIRES=2592000
FLASK_ENV=development
FLASK_DEBUG=True
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)

def main():
    # Genera le chiavi
    secret_key, jwt_secret_key = generate_secrets()
    
    # Stampa le chiavi
    print("\nChiavi generate:")
    print(f"SECRET_KEY={secret_key}")
    print(f"JWT_SECRET_KEY={jwt_secret_key}")
    
    # Chiedi se vuoi creare il file .env
    create_env = input("\nVuoi creare automaticamente il file .env? (s/n): ").lower()
    if create_env == 's':
        create_env_file(secret_key, jwt_secret_key)
        print("\nFile .env creato con successo!")
    else:
        print("\nCopia e incolla le chiavi nel tuo file .env")

if __name__ == "__main__":
    print("=== Generatore di chiavi sicure per CoachConnect ===")
    print("Questo script genera chiavi sicure per l'applicazione.")
    print("Le chiavi verranno generate usando secrets.token_hex(32)")
    print("che produce una stringa esadecimale casuale di 64 caratteri.\n")
    
    main() 