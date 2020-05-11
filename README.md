# Icky Project
Have you ever encountered a problem that seemed too hard to solve? Icky will help you come up with solutions for problems that seem impossible. It's best explained over [here](https://matttaylor.com/public/zwicky_box_uses.htm). If you don't feel like reading the whole text, just give it a go (when it's MVP ready).

## ToDo
- [ ] Rate limiter
- [ ] Expire token

## Prepare and run Backend
```
python3 -m venv [path_to_folder]
source [path_to_folder]/bin/activate
cd icky-project
pip install -r requirements.txt
python manage.py startapp icky-project
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Prepare and run frontend
```
cd [path_to_folder]/icky-frontend
npm install
npm run serve
```
