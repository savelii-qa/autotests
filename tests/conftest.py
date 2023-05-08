import logging
import pytest
from test_data.data_posts import Post
from core.http_request import HTTPRequest


@pytest.fixture(scope="session")
def log(log_level=logging.INFO):
    logger = logging.getLogger()
    logger.setLevel(log_level)

    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


@pytest.fixture(scope="function")
def create_post():
    post = Post()
    r = HTTPRequest(method='POST', uri='/posts', body=post.generate_post())
    id = r.json["id"]
    return id
