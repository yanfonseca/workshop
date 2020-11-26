# Workshops
Interface para criar workshops.

[![Build Status](https://travis-ci.org/yanfonseca/workshop.svg?branch=main)](https://travis-ci.org/yanfonseca/workshop)

## Como desenvolver
1. Clone o repositório
1. Crie um virtualenv com Python 3.5 ou superior.
1. Ative o virtualenv
1. Instale as dependências
1. Configure a instância com o .env
1. Execute os testes

```console
git clone https://github.com/yanfonseca/workshop.git
cd workshop
python -m venv .myenv
source .myenv/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy

### Configurações do Heroku
1. Crie uma instância no heroku
1. Envie as configurações para o heroku
1. Defina uma SECRET_KEY segura para a instância
1. Defina DEBUG=False
1. Defina o smtp do gmail ou outro serviço
1. Defina configurações para envio de e-mail

```console
heroku apps:create <yourname>-workshop
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
heroku config:set EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
heroku config:set EMAIL_HOST=******
heroku config:set EMAIL_PORT=587
heroku config:set EMAIL_USE_TLS=True
heroku config:set EMAIL_HOST_USER=******
heroku config:set EMAIL_HOST_PASSWORD=******
```

### Enviar para o Heroku e criar migrações
1. Envie o código para o heroku
1. Faça as migrações no heroku
1. Crie um super-user para o /admim

```console
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```
