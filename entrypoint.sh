#!/bin/sh

alembic upgrade head
spacy download pt_core_news_sm

exec "$@"
