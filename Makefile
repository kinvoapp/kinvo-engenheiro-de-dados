.PHONY : help clean dev install migrations run

help:
	@echo ""
	@echo "Python Developer Job Candidate Test (focused on AI - Artificial Intelligence)"
	@echo ""
	@echo ""
	@echo "Available commands:"
	@echo "    clean \t\t Clean deployment assets and remove created database"
	@echo "    dev \t\t Run app on development mode"
	@echo "    install \t\t Install project dependencies"
	@echo "    migrations \t\t Run database migrations"
	@echo "    run \t\t Run project through docker containers"

clean:
	@echo ""
	@echo "Cleaning generated files during deployment"
	@docker-compose down --rmi all -v
	@docker system prune -af

dev: install migrations
	@echo ""
	@echo "Runing app on DEV mode"
	@echo ""
	@poetry run spacy download pt_core_news_sm
	@poetry run gunicorn --bind 0.0.0.0:6500 wsgi:app --reload

install:
	@echo ""
	@echo "Install dependencies"
	@echo ""
	@poetry install --no-root --remove-untracked

migrations:
	@echo ""
	@echo "Runing Database Migrations"
	@echo ""
	@poetry run alembic upgrade head

run: clean
	@echo ""
	@echo "Building and runing docker container"
	@echo ""
	@docker-compose up -d postgres
	@docker-compose build --no-cache --compress --force-rm
	@docker-compose up -d kinvo
