from lib import Database

from core.config import settings

db = Database(settings.POSTGRESQL_URI, debug=settings.DEBUG)
engine = db.engine
async_session = db.session_factory
init_db = db.init_db
get_session = db.get_session_context
