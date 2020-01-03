
import pytest
import os



if __name__ == '__main__':
    pytest.main(["-v","-m","register","--alluredir=../../OutPuts/allure-results",'--workers=1','--tests-per-worker=4'])
    os.system(r"allure generate --clean ../../OutPuts/allure-results -o ../../allure-report ")