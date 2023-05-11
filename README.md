# Simple migration example with [alembic](https://alembic.sqlalchemy.org/en/latest/index.html)

Used links:
 * [Alembic Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
 * [Schema migrations with Alembic, Python and PostgreSQL](https://www.compose.com/articles/schema-migrations-with-alembic-python-and-postgresql/)

1. `alembic init migration`

2. Edit `env.py` and `alembic.ini`.

3. `alembic revision -m "baseline"`

4. Edit `..._baseline.py`

    ```python
    op.add_column(
        'customer',
        column=sa.Column('personal_discount', sa.types.Integer)
    )
    op.alter_column(
        'product',
        column_name='price',
        type_=sa.types.Float
    )
    ```

5. `alembic upgrade head`