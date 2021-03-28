"""
测试用例
用来测试业务代码calc-practice
"""
import allure
import pytest

from python_code.calc import Calculator


# with open("./datas/calc.yaml") as f:
#     datas = yaml.safe_load(f)
#     add_datas = datas['add']['datas']
#     myid = datas['add']['myid']
#
#     datas_div = datas['div']
#     div_datas=datas_div['datas']
#     div_myid =datas_div['myid']

@allure.feature("测试计算器")
class TestCalc:

    # def setup(self):
    #     print("开始计算")
    #     self.calc = Calculator()
    #
    # def teardown(self):
    #     print("计算结束")

    # @pytest.mark.parametrize(
    #     "a,b,expect",
    #     add_datas,  ids=myid
    # )
    @allure.story("测试加法")
    @allure.title("测试加法")
    def test_add(self, get_calc, get_add_datas):
        # 实例化计算器类
        # calc = Calculator()
        # 调用add方法传入值
        result = None
        try:
            with allure.step("输入两个值"):
              result = get_calc.add(get_add_datas[0], get_add_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        # 断言
        assert result == get_add_datas[2]

    # #用pytest进行参数化
    #  @pytest.mark.parametrize(
    #      "a1,b1,expect1",
    #      div_datas,  ids=div_myid
    #  )
    @allure.story("测试减法")
    def test_div(self, get_calc, get_div_datas):
        result = None
        try:
            with allure.step("输入两个值"):
                result = get_calc.div(get_div_datas[0], get_div_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_div_datas[2]
