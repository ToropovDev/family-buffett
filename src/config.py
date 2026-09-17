import dotenv
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

dotenv.load_dotenv()


class _PGSettings(BaseSettings):
    scheme: str = "postgresql+asyncpg"
    host: str = "localhost"
    port: int = 5432
    user: str = "buffett"
    password: str = "buffett"
    database: str = "buffett"

    def build_dsn(self, *, scheme: str | None = None) -> str:
        return str(
            PostgresDsn.build(
                scheme=scheme or self.scheme,
                host=self.host,
                port=self.port,
                username=self.user,
                password=self.password,
                path=self.database,
            ),
        )

    model_config = SettingsConfigDict(env_prefix="POSTGRES_")


PGSettings = _PGSettings()
