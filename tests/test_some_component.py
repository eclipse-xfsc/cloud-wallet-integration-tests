
import pytest
from pytest_bdd import *

from steps.login_steps import *
from steps.logout_steps import *
from steps.parallel_user_testing_steps import *

scenarios('../features/parallel_user_testing.feature')


# def test_some_component():
#     """
#     Some dummy test placeholder
#     """
#     x = 1
#     y = 1
#     assert x == y
