pip install virtualenv
virtualenv test_kinvo
call test_kinvo/scripts/activate

pip install -r bibliotecas.txt
python -m spacy download pt_core_news_sm

python scripts/train_model.py

pause