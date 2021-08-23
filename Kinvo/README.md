```sh

virtualenv env --python="$(which python3)"

source env/bin/activate
pip install -r requirements.txt

cd Kinvo && cd Kinvo && scrapy crawl feedspider -L WARNING -o feedspider.json

flask run
```

