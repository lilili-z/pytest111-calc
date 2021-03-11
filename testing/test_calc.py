"""
测试用例
用来测试业务代码calc-practice
"""
import pytest
import yaml

from python_code.calc import Calculator

with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    myid = datas['myid']


@pytest.mark.parametrize(
    "a,b,expect",
    add_datas, ids=myid
)
class TestCalc:
    def setup(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown(self):
        print("计算结束")

    def test_add(self, a, b, expect):
        # 实例化计算器类
        # calc = Calculator()
        # 调用add方法传入值
        result = self.calc.add(a, b)

        if isinstance(result, float):
            result = round(result, 2)
        # 断言
        assert result == expect
