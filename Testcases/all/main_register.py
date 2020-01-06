import pytest
import os
import sys
sys.path.append('./')



if __name__ == '__main__':
    pytest.main(["-v","-m","register","--alluredir=../../OutPuts/allure-results",'--workers=2','--tests-per-worker=4'])
    os.system(r"allure generate --clean ../../OutPuts/allure-results -o ../../allure-report ")