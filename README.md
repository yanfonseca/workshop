# Workshops
Interface para criar workshops.

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
pip install -r requirements.txt
cp contrip/env-sample .env
python manage.py test
```

## Como fazer o deploy
1. Crie uma instância no heroku
1. Envie as configurações para o heroku
1. Defina uma SECRET_KEY segura para a instância
1. Defina DEBUG=False
1. Envie o código para o heroku

```console
heroku apps:create yourname-workshop
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
git push heroku main
```

