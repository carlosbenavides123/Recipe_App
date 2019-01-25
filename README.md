# Recipe_App

install

Build the project.
- (sudo) docker build .

Run the unit tests (will download all dependencies from requirements if havn't done so yet)
- (sudo) docker-compose run --rm app sh -c "python manage.py test && flake8"

Add new migrations (assuming new model has been made, core is a directory for example)
- (sudo) docker-compose run --rm app sh -c "python manage.py makemigrations core"
