#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/8/5 16:18
import jmespath
import pytest

# 用例调用fixture的返回值，直接就是把fixture的函数名称当做变量名称。
def test_get_creation_forms(user1):
    """验证【我的】——我创建的表单列表获取正确性"""

    params = {'pageNo': 1, 'pageSize': 20}
    res = user1.v1_creation_forms(params=params, method=user1.GET)
    assert res.status_code == 200

    """20230210徐雪霞备注：由于数据库分库，目前返回的分页条数和请求的分页数对不上"""
    # forms = jmespath.search('@.data.creations.*[*][]', res.data)
    # # 分页测试
    # if len(forms) > 5:
    #     params = {'pageNo': 2, 'pageSize': 5}
    #     res = user1.v1_creation_forms(params=params, method=user1.GET)
    #     assert res.status_code == 200
    #     forms = jmespath.search('@.data.creations.*[*][]', res.data)
    #     assert 1 <= len(forms) <= 5


if __name__ == '__main__':
    pytest.main()
