# Import all the models, so that Base has them before being
# imported by Alembic
from src.database.base import Base # noqa
from src.database.orm import User, Org # noqa
