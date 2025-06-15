from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import logging
from logging.handlers import RotatingFileHandler
import os
from config import config

# Inizializzazione delle estensioni FUORI dalla funzione create_app
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
cors = CORS()

def create_app(config_name='development'):
    """Factory function per creare l'istanza Flask"""
    app = Flask(__name__)
    
    # Carica la configurazione
    app.config.from_object(config[config_name])
    
    # Inizializza le estensioni con l'app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # Configura CORS per accettare richieste dal frontend
    cors.init_app(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:3000", "http://127.0.0.1:3000"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })
    
    # Configura logging (PRIMA di tutto)
    setup_logging(app)
    
    # Registra gestori di errori HTTP
    register_error_handlers(app)
    
    # Registra gestori di errori JWT (devono essere nell'app context)
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({
            'error': 'Token Expired',
            'message': 'Il token è scaduto'
        }), 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({
            'error': 'Invalid Token',
            'message': 'Token non valido'
        }), 401
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({
            'error': 'Missing Token',
            'message': 'Token di autorizzazione richiesto'
        }), 401
    
    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return jsonify({
            'error': 'Fresh Token Required',
            'message': 'Token fresco richiesto'
        }), 401
    
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return jsonify({
            'error': 'Token Revoked',
            'message': 'Il token è stato revocato'
        }), 401
    
    # TODO: Registrare i blueprint qui
    # from routes import auth_bp, coach_bp, user_bp
    # app.register_blueprint(auth_bp, url_prefix='/api/auth')
    # app.register_blueprint(coach_bp, url_prefix='/api/coaches')
    # app.register_blueprint(user_bp, url_prefix='/api/users')
    
    # Health check route
    @app.route('/')
    def health_check():
        return jsonify({
            'status': 'ok',
            'message': 'CoachConnect API is running',
            'version': '1.0.0'
        })
    
    # Comandi CLI personalizzati
    register_cli_commands(app)
    
    return app

def setup_logging(app):
    """Configura il sistema di logging"""
    if not app.debug and not app.testing:
        # Crea la cartella logs se non esiste
        if not os.path.exists('logs'):
            os.mkdir('logs')
        
        # Configura il RotatingFileHandler
        file_handler = RotatingFileHandler(
            'logs/coachconnect.log',
            maxBytes=10240000,  # 10MB
            backupCount=10
        )
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        
        app.logger.setLevel(logging.INFO)
        app.logger.info('CoachConnect startup')

def register_error_handlers(app):
    """Registra i gestori di errori HTTP"""
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'error': 'Bad Request',
            'message': 'La richiesta non è valida'
        }), 400
    
    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'error': 'Unauthorized',
            'message': 'Accesso non autorizzato'
        }), 401
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'error': 'Not Found',
            'message': 'Risorsa non trovata'
        }), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return jsonify({
            'error': 'Internal Server Error',
            'message': 'Errore interno del server'
        }), 500

def register_cli_commands(app):
    """Registra i comandi CLI personalizzati"""
    
    @app.cli.command('init-db')
    def init_db():
        """Crea tutte le tabelle del database"""
        try:
            db.create_all()
            print('✅ Database inizializzato con successo!')
        except Exception as e:
            print(f'❌ Errore durante l\'inizializzazione del database: {e}')
    
    @app.cli.command('seed-db')
    def seed_db():
        """Popola il database con dati di test"""
        try:
            # TODO: Implementare il seeding dei dati
            print('🌱 Seeding del database completato!')
            print('ℹ️  Al momento questo è un placeholder - implementare i dati di test')
        except Exception as e:
            print(f'❌ Errore durante il seeding: {e}')
