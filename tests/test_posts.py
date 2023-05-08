import pytest
from models import models
from test_data import data_posts
from helpers.http_requests import *


@pytest.fixture(params=data_posts.post_creation_positive)
def param_post_positive_case(request):
    return request.param


@pytest.fixture(params=data_posts.post_creation_negative)
def param_post_negative_case(request):
    return request.param


def test_01_post_creation_positive(param_post_positive_case, log):
    post = param_post_positive_case.data
    log.info(f'Post creation, positive: {format(param_post_positive_case.description)}')
    log.info(f'Post request: {format(post)}')
    r = post_creation(post)
    assert r.status_code == 201
    created_post = models.CreatedPost(r.json)
    assert created_post == post


# Negative example
def test_02_post_creation_negative(param_post_negative_case, log):
    post = param_post_negative_case.data
    log.info(f'Post creation, negative: {format(param_post_negative_case.description)}')
    log.info(f'Post request: {format(post)}')
    r = post_creation(post)
    assert r.status_code == 400


def test_03_post_update_positive(param_post_positive_case, log, create_post):
    post = param_post_positive_case.data
    log.info(f'Post update, positive: {format(param_post_positive_case.description)}')
    log.info(f'Post request: {format(post)}')
    r = post_update(post, create_post)
    assert r.status_code == 200
    created_post = models.CreatedPost(r.json)
    assert created_post == post


# Negative example
def test_04_post_update_negative(param_post_negative_case, log, create_post):
    post = param_post_negative_case.data
    log.info(f'Post update, negative: {format(param_post_negative_case.description)}')
    log.info(f'Post request: {format(post)}')
    r = post_update(post, create_post)
    assert r.status_code == 400

def test_05_post_deleting(log, create_post):
    log.info(f'Post deleting, id = {format(create_post)}')
    r = post_delete(create_post)
    assert r.status_code == 200

def test_06_posts_list(log):
    log.info(f'Posts list')
    r = posts_list()
    assert r.status_code == 200
    result = r.json
    assert len(result) == 100
    assert all(key in result[0] for key in ['userId', 'title', 'body', 'id'])

def test_07_post_details(log, create_post):
    log.info(f'Post details, id = {format(create_post)}')
    r = post_details()
    assert r.status_code == 200
    assert all(key in r.json for key in ['userId', 'title', 'body', 'id'])


