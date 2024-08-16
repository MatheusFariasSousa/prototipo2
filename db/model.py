from sqlalchemy.orm import registry,mapped_column,Mapped
from db.connection import engine



table_registry = registry()

@table_registry.mapped_as_dataclass
class User():
    __tablename__="User_db"
    id:Mapped[int] = mapped_column("id",primary_key=True,autoincrement=True,init=False)
    name:Mapped[str] = mapped_column("name",nullable=False)
    cpf:Mapped[str] = mapped_column("cpf",nullable=False,unique=True)
    password:Mapped[str] = mapped_column("password",nullable=False)


table_registry.metadata.create_all(engine)