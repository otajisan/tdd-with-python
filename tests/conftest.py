'''
Common Test Fixture
'''
from otajisan.samples.tdd.play.hello import Hello

import pytest


@pytest.fixture()
def sample_fixture():
    print('>>> setup')
    yield
    print('<<< teardown')
