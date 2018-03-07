#!/bin/bash
export FLASK_APP=artikulo/artikulo.py
export FLASK_DEBUG=true

export SECRET_KEY=secret_key

export MAIL_SERVER=smtp.googlemail.com
export MAIL_PORT=587
export MAIL_USE_TLS=1
export MAIL_USERNAME=username
export MAIL_PASSWORD=password