# Docker operations

build:
	docker-compose up -d --build

run:
	docker-compose up -d

stop:
	docker-compose down

restart:
	docker-compose down
	docker-compose up -d

logs:
	docker-compose logs -f

# Import operations

import:
	docker-compose run --rm --no-deps web python manage.py import_highlights --tv_show_id=1 --max_items_to_parse=50

import_legacy:
	docker-compose run --rm --no-deps web python manage.py import_legacy_highlights --tv_show_id=1 --max_items_to_parse=50