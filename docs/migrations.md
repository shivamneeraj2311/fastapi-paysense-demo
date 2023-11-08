# Migrations

## Creating new migration

1. Make sure the current local schema is up to date

```
make upgrade_database
```

2. Make desired changes to `sparc_pay_api/database/orm.py`
3. Run the following commands to create a new revision

```
make create_migration message="add new column to some old table"
```

4. Run `make upgrade_database` to update the local schema to desired state




> Note
Since we internally use alembic to manage migrations, you can use regular alembic commands to interact with migrations management.
