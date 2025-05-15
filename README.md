-- criar ambiente virtual
   python  -m venv venv

-- Ativar ambiente virtual
   venv\Scripts\activate

-- instalar as dependencias do projeto
   pip install -r requirements.txt

-- rodar a migration
   python ./manage.py  migrate 

-- criar super usuario
   python manage.py createsuperuser (seguir os passos solicitados pelo cmd)

   Usuário: admin@admin.com.br
   E-mail: admin@admin.com.br
   Password:123456789   

-- rodar o projeto
   python manage.py runserver
