# Clone and run project
```bash
git clone https://github.com/it21998/devopsAdmin.git
python -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
cd student_management
cp student_management/.env.example student_management/.env
```
edit student_management/.env file to define
```vim
SECRET_KEY='test123'
DATABASE_URL=postgres://myprojectuser:password@localhost:/myproject
```
# run development server
```bash
python manage.py runserver
```
