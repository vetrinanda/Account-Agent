from .database import Base,sessionmaker,engine
from .tables import User
from langchain_core.tools import tool


@tool
def get_user_balance(user_id: int) -> int:
    db = sessionmaker(bind=engine)()
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        return user.balance
    else:
        return 0