pipenv run python run.py --description $1 --model v2 --form t1 --label outcome --hyperparameters hyperparameters.json --split 6f91b43f-d6cd-42dc-9eb6-8178f4ea8cc1
pipenv run python run.py --description $1 --model v2 --form t2 --label outcome --hyperparameters hyperparameters.json --split 6f91b43f-d6cd-42dc-9eb6-8178f4ea8cc1
pipenv run python run.py --description $1 --model v2 --form features --label outcome --hyperparameters hyperparameters.json --split 6f91b43f-d6cd-42dc-9eb6-8178f4ea8cc1