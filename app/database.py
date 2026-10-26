import logging
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

logger = logging.getLogger(__name__)


def _normalize_url(url: str) -> str:
    # Supabase/Heroku style "postgres://" -> SQLAlchemy "postgresql://"
    if url.startswith("postgres://"):
        url = "postgresql://" + url[len("postgres://"):]
    # Use the psycopg 3 driver explicitly (installed via requirements: psycopg[binary])
    if url.startswith("postgresql://"):
        url = "postgresql+psycopg://" + url[len("postgresql://"):]
    return url


SQLALCHEMY_DATABASE_URL = _normalize_url(settings.DATABASE_URL or "sqlite:///./news.db")
IS_SQLITE = SQLALCHEMY_DATABASE_URL.startswith("sqlite")

def _sqlite_engine():
    # check_same_thread=False is required for SQLite in FastAPI
    return create_engine("sqlite:///./news.db", connect_args={"check_same_thread": False})


if IS_SQLITE:
    engine = _sqlite_engine()
else:
    try:
        # Supabase Postgres: drop dead connections, keep the pool small for the free tier
        engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, pool_size=5, max_overflow=5,
                               pool_recycle=1800, connect_args={"connect_timeout": 10})
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        logger.info("Connected to Postgres (Supabase).")
    except Exception as e:
        # Never take the site down because of a bad DATABASE_URL: fall back to the bundled SQLite file
        import re
        msg = (str(e).splitlines() or [""])[0][:200]
        msg = re.sub(r"://[^\s'\"]*@", "://***@", msg)  # never log the password
        msg = re.sub(r"(postgres(?:ql)?://)\S+", r"\1***", msg)
        logger.error(f"Could not connect to DATABASE_URL, falling back to SQLite news.db: "
                     f"{e.__class__.__name__}: {msg}")
        engine = _sqlite_engine()
        IS_SQLITE = True

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
