# pythonrio-django

Essa é a nova versão do site da pythonrio, baseado no projeto 'python_getting_started' do heroku.

## Rodando localmente

Antes de tudo, você precisa ter o portgres (dependência do heroku) o python 3.6 ou superior instalado na sua máquina.
Depois de clonar o projeto (`git clone https://github.com/lucianoratamero/pythonrio-django.git`), você deve instalar uma virtualenv e ativá-la:

```sh
python -m virtualenv pythonrio-django
cd pythonrio-django
source bin/activate
```

Depois disso, instale as dependências e crie um banco local usando o django:

```sh
pip install -r requirements.txt
python manage.py migrate
```

Com tudo pronto, rode o servidor localmente:

```sh
python manage.py runserver
```
