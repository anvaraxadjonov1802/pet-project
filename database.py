from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, sessionmaker
from sqlalchemy.testing.schema import mapped_column

# Use create_async_engine for asynchronous operations
engine = create_async_engine(
    "postgresql+asyncpg://pre_project_user:password@localhost:5432/pre_project_db"
)

# Use AsyncSession for session creation
new_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class TaskOrm(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]

# Functions for creating and dropping tables
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
