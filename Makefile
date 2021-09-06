.PHONY : help clean dropdb install migrations run

help:
	@echo ""
	@echo "Python Developer Job Candidate Test (focused on AI - Artificial Intelligence)"
	@echo ""
	@echo ""
	@echo "Available commands:"
	@echo "    clear \t\t Clean deployment assets and remove created database"
	@echo "    run \t\t Run project through docker containers"
	@echo "    testapp \t\t Run unit tests"

clear:
	@echo ""
	@echo "Cleaning generated files during deployment"
	@docker-compose down --rmi all -v
	@docker system prune -af

run:
	@echo ""
	@echo "Building and runing docker container"
	@echo ""
	@docker-compose up

testapp:
	@echo ""
	@echo "Runing Application Unit Test"
	@echo ""
	@poetry run pytest tests -vv --disable-warnings
