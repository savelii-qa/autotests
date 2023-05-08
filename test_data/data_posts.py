from models.models import PostModel, CreatedPost
from models.test import TestCaseData
import uuid
import shortuuid
from core.http_request import HTTPRequest

def uuid_creation():
    uuid_id = f'{(uuid.uuid4())}'
    return uuid_id


USER_ID = 69


import json
import uuid

class Post:
    def __init__(self):
        self.userId = USER_ID
        self.title = str(uuid.uuid4())
        self.body = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit."

    def create_post(self):
        post = {
            "userId": self.userId,
            "title": self.title,
            "body": self.body
        }
        r = HTTPRequest(method='POST', uri='/posts', body=post)
        response = r.json
        return response


# suppose that validation for Title (20-50, uniq), Body (20-500)
post_creation_positive = [
    TestCaseData(
        description="Max boundary",
        status_code=201,
        data=PostModel(
            userId=USER_ID,
            title="Title=========" + f"{uuid_creation()}",
            body="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean "
                 "massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec "
                 "quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. "
                 "Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, "
                 "imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. "
                 "Cras dapibu",
        )
    ),
    TestCaseData(
        description="Min boundary",
        status_code=201,
        data=PostModel(
            userId=USER_ID,
            title=f"{shortuuid.uuid()[:20]}",
            body="Lorem ipsum dolor si",
        )
    )

]

post_creation_negative = [
    TestCaseData(
        description="Max boundary +1",
        status_code=400,
        data=PostModel(
            userId=USER_ID,
            title="Title=========1" + f"{uuid_creation()}",
            body="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean "
                 "massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec "
                 "quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. "
                 "Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, "
                 "imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. "
                 "Cras dapibu1",
        )
    ),
    TestCaseData(
        description="Min boundary -1",
        status_code=400,
        data=PostModel(
            userId=USER_ID,
            title=f"{shortuuid.uuid()[:19]}",
            body="Lorem ipsum dolor s",
        )
    )
]
