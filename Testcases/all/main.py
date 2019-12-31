import pytest
import os
# pytest.main(["-v","-m","login"])
#
# pytest.main(["-v","-m","demo","--reruns","1","--alluredir=../OutPuts/allure-results"])
# os.system(r"allure generate --clean ../OutPuts/allure-results -o ../allure-report ")

# pytest.main(["-v","-m","demo","--alluredir=../../OutPuts/allure-results"])
# os.system(r"allure generate --clean ../../OutPuts/allure-results -o ../../allure-report ")
if __name__ == '__main__':
    pytest.main(["-v","-m","register","--alluredir=../../OutPuts/allure-results",'--workers=2','--tests-per-worker=4'])
    os.system(r"allure generate --clean ../../OutPuts/allure-results -o ../../allure-report ")