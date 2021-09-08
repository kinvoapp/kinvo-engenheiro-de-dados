# Python Developer Job Candidate Test (AI focused)

Powered by [Logo Kinvo](https://github.com/kinvoapp/kinvo-mobile-test/blob/master/logo.svg).

## Test Instructions

1. Mining five news about B3 shares (_Note: Important to save to be used in natural language processing (NLP) later._)
   - [finace news](https://financenews.com.br/feed/)
   - [ultimo instance](https://www.ultimoinstante.com.br/feed/)
2. Extract the entities from the 5 previously mined news items (entity recognition).
3. Create an API with two endpoints for:
   - Mining and save the news;
   - Extrat the entities from the crawled news (entity recognition);
4. Finally, make a pull request on github of your solution and wait for your feedback (please follow instrunctions on the (Submission Process)[#submission-process]).
5. Test requirements:
   - Flask;
   - Python;
   - Spacy;
   - Scrapy;

## Basic commands

- To run on *Dev mode* and execute the project locally, uses the command `make dev`.
- For running this project through a docker container please uses the `make run` command.
- Run on your terminal `make help` to check all commands available.

_Note: The project was developed using `Poetry` for Python dependency management. Thus, to run on dev mode it required the installation of Poetry first. To doing so, please follow the instructions on the [Poetry's page](https://python-poetry.org/). Finally, the dependency list is available on the `pyproject.toml` file._

After startup the app (using `make dev` or `make run` commands), open the following URL on your preferred browser: [http://0.0.0.0:6500/](http://0.0.0.0:6500/).

## API Information

Available endpoints:

- POST [http://0.0.0.0:6500/api/v1/news](http://0.0.0.0:6500/api/v1/news): Crawl news to save on database;
- GET [http://0.0.0.0:6500/api/v1/entities](http://0.0.0.0:6500/api/v1/entities): Recognize the text entities;

## App Folder Structure

The app was developed using the stack described on item 5 of the test instructions section and the code is strucutred as follow:

```sh
- kinvo                  >> app root
  - alembic              >> alembic database migration scripts
  - api                  >> REST api routes
  - core                 >> app core structure (config)
  - database             >> database structure (access, crud, models, and schemas)
  - frontend             >> frontend content (static assets and html templates)
  - services             >> app services (news spiders)
  - tasks                >> app tasks (data mining)
  - logger.py            >> app logger
  - main.py              >> app main

- .dockerignore          >> list of files and folders ignored by docker
- .gitignore             >> list of files and folders ignored by git
- alembic.ini            >> alembic config file
- docker-compose.yml     >> docker ignore file
- Dockerfile             >> docker file with instructions to assemble an docker image.
- entrypoint.sh          >> docker entrypoint file to startup the app correctly
- Makefile               >> project makefile to easy run the basic commands
- postgresql.conf        >> postgresql config file
- pyproject.toml         >> project dependcies file
- README.md              >> this file
- scrapy.cfg             >> scrapy config file
- wsgi.py                >> wsgi file to run the app through gunicorn
```
