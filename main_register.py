import pytest
import os
import sys
sys.path.append('./')



if __name__ == '__main__':

    pytest.main(["-v","-m","register","--reruns","2","-delay","5","--alluredir=OutPuts/allure-results"])
    os.system("allure generate  OutPuts/allure-results -o allure-report --clean")



