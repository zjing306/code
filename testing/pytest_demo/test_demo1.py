# !/usr/bin/env python
# -*-encoding:utf-8-*-
# @Time:16:16
# @File:test_demo1.py
# @Author:秦时明月
import pytest

from testing.pytest_demo.calculator import Calculator


class TestCalc:

    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect',[[1,2,3],[2,3,5]],
                             ids=['int_cas11','int_case2'])
    def test_add(self,a,b,expect):
        result = self.calc.add(a,b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect',[[3,2,1],[7,5,2]],
                             ids=['int_cas11','int_case2'])
    def test_sub(self,a,b,expect):
        result = self.calc.sub(a,b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect',[[9,3,27],[5,6,30]],
                             ids=['int_cas11','int_case2'])
    def test_mul(self,a,b,expect):
        result = self.calc.mul(a,b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect',[[90,10,9],[72,8,9]],
                             ids=['int_cas11','int_case2'])
    def test_div(self,a,b,expect):
        result = self.calc.div(a,b)
        assert result == expect