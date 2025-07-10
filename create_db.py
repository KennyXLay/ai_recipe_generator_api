from app.db.session import engine, Base
from app.models import user, recipe # import all models

Base.metadata.create_all(bind=engine)