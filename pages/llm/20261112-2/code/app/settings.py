from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL


class Settings(BaseSettings):
    db_user: str = "postgres"
    db_password: str
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "day19_crud_b"
    model_config = SettingsConfigDict(env_file=".env")

    @property
    def database_url(self) -> URL:
        # 비밀번호를 문자열로 이어 붙이지 않고 조각으로 넘긴다
        return URL.create(
            "postgresql+psycopg",
            username=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            database=self.db_name,
        )


settings = Settings()
