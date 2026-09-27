# -*- coding: utf-8 -*-
"""混剪节奏演示 —— 时长压缩与砍拍
渲染: cd 本目录 && ~/venvs/manim/bin/manim -qh demo_fast.py GaussianFast
"""
from manim_3d import gaussian_surface_scene


class GaussianFast(gaussian_surface_scene(pace="fast", name="GaussianFast")):
    """10 秒混剪版:预算放不下,自动砍掉等高线→平面→标注→环绕→翻面。"""


class GaussianTeaser(gaussian_surface_scene(duration=16, name="GaussianTeaser",
                                            rings=False, annotate=False)):
    """16 秒预告版:手动砍等高线/标注,保住环绕+翻面。"""
