from jsonobject import *


class PostModel(JsonObject):
    userId = IntegerProperty
    title = StringProperty
    body = StringProperty


class CreatedPost(JsonObject):
    userId = IntegerProperty
    title = StringProperty
    body = StringProperty
    id = IntegerProperty

    def __eq__(self, other):
        return self.userId == other.userId and self.title == other.title and self.body == other.body
