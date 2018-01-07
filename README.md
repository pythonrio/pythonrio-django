# pythonrio-django-2

Essa é a nova versão do site da pythonrio, baseado no projeto 'python_getting_started' do heroku.

## Rodando localmente

Como usamos django 2, você precisa ter o python 3.6 ou superior instalado na sua máquina e o postgres (dependência do heroku).
Depois de clonar o projeto (`git clone https://github.com/lucianoratamero/pythonrio-django-2.git`), você deve instalar uma virtualenv e ativá-la:

```sh
python -m virtualenv pythonrio-django-2
cd pythonrio-django-2
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
