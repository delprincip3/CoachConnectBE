#!/usr/bin/env python3
"""
Script per avviare l'applicazione CoachConnect in modalità development
"""

from app import create_app
import os

# Crea l'istanza Flask usando il factory pattern
app = create_app(config_name='development')

if __name__ == '__main__':
    # Avvia l'applicazione in modalità debug per development
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5222)),
        debug=True
    ) 