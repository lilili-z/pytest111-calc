import pytest
import yaml
import os

from python_code.calc import Calculator

yaml_file_path = os.path.dirname(__file__) + "/datas/calc.yaml"
with open("./datas/calc.yaml", encoding='utf-8')as f:
    datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    myid = datas['add']['myid']

    div_datas = datas['div']['datas']
    div_myid = datas['div']['myid']


@pytest.fixture(scope="class")
def get_calc():
    print("开始计算")
    calc = Calculator()
    return calc


@pytest.fixture(params=add_datas, ids=myid)
def get_add_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据{data}")
    yield data
    print("结束计算")


@pytest.fixture(params=div_datas, ids=div_myid)
def get_div_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据{data}")
    yield data
    print("结束计算")
