# alembic for SyamsulApp migration
- database revision control

# requirements
[pip]
- alembic
- mysqlclient

[documentation]
- https://alembic.sqlalchemy.org/en/latest/autogenerate.html

[usefull-command]
- alembic init "name" -> initialize alembic folder
- alembic revision --autogenerate -m "comment" -> create revision script
- alembic upgrade head -> upgrade database
- alembic downgrade -1 -> downgrade 1 step