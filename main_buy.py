import pytest
import os
import sys
sys.path.append('./')


# pytest.main(["-v","-m","demo","--reruns","1","--alluredir=../OutPuts/allure-results"])
# os.system(r"allure generate --clean ../OutPuts/allure-results -o ../allure-report ")




pytest.main(["-v","-m","buy","--alluredir=OutPuts/allure-results"])
os.system("allure generate  OutPuts/allure-results -o allure-report --clean")

