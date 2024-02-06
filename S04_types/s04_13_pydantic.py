from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name= 'Jhon Doe'
    signup_ts: datetime | None = None
    friends: list[int] = []

    external_data= {
        "id": 123,
        "signup_ts": '2018-06-01 12:22',
        "friends": [1,2,3,4],
    }
    
    user = User(**external_data)
    print(user)
    print(user.id)
