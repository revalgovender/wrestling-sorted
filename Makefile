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

import_raw:
	docker-compose run --rm --no-deps web python manage.py import_highlights --tv_show_id=1 --max_items_to_parse=50

import_raw_legacy:
	docker-compose run --rm --no-deps web python manage.py import_legacy_highlights --tv_show_id=1 --max_items_to_parse=50

import_smackdown:
	docker-compose run --rm --no-deps web python manage.py import_highlights --tv_show_id=2 --max_items_to_parse=50

import_smackdown_legacy:
	docker-compose run --rm --no-deps web python manage.py import_legacy_highlights --tv_show_id=2 --max_items_to_parse=50