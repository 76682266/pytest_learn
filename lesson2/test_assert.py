#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class TestCase(object):
    def test_assert_true(self):
        a=1
        assert a
    def test_assert_false(self):
        a=False
        assert a
    def test_assert_in(self):
        a=1
        assert a in [1,2,3]
    def test_assert_equal(self):
        a=1
        assert a==1
    def test_assert_unique(self):
        a=1
        assert a not in [1,2,3]
    def test_assert_null(self):
        a=1
        assert a is None