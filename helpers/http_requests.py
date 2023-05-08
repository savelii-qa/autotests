from core.http_request import HTTPRequest


def post_creation(post):
    r = HTTPRequest(method='POST', uri='/posts', body=post.to_json())
    return r

def post_update(post, id):
    r = HTTPRequest(method='PUT', uri='/posts/1', headers={"id": f'{id}'}, body=post.to_json())
    return r

def post_delete(id):
    r = HTTPRequest(method='DELETE', headers={"id": f'{id}'}, uri='/posts/1')
    return r

def posts_list():
    r = HTTPRequest(method='GET', uri='/posts')
    return r

def post_details():
    r = HTTPRequest(method='GET', uri='/posts/1', headers={"id": f'{id}'})
    return r