# AulaCRUD

Fazendo um CRUD no django

Projeto simples e funcional, para quem deseja aprender como fazer o primeiro CRUD com Django.

#aulas também gravei algumas aulas no youtube para tentar ajudar

Instalando:

https://python.org/downloads/.

LEMBRE-SE DA MARCAR , NA PRIMEIRA PÁGINA DA INSTALAÇÃO O "PATH"

python --version

Agora, digite pip --version.

A saída desse comando deve ser a versão instalada do pip.

python -m pip install --upgrade pip

################################################

Criar ambiente virtual dentro da pasta:

pip install virtualenv

pip install virtualenvwrapper-win

mkvirtualenv "nome_env"

agora workon "nome_env" <-------- abrir ambiente virtual

################################################

outra forma de virtualizar é

py -m pip install --user virtualenv

py -m venv nome_env

.\nome_env\Scripts\activate

Vamos precisar instalar

################################################

melhorar o layout dos formulários

pip install django-crispy-forms

pARA EXCLUIR ARQUIVOS AR EDITAR

pip install django-cleanup

################################################

Criar as tabelas no banco de dados

Se você só alterou as tabelas e quer atualizar

py manage.py makemigrations

py manage.py migrate

################################################

Aula template

https://www.youtube.com/watch?v=jSpx2t__Iv0

No settings ##################### DECLARAR

STATIC_URL = '/staticfiles/'

STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = [

os.path.join(BASE_DIR, 'static')
]

CRISPY_TEMPLATE_PACK = "bootstrap4"

############## CRIOU UM APP ##################

Lembre-se de declara no settings

#abraços
