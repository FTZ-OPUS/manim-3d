# -*- coding: utf-8 -*-
"""抛物面封装验收 —— 几行代码复刻手工样片
渲染: cd 本目录 && ~/venvs/manim/bin/manim -qh demo_paraboloid.py ParaboloidSurface
"""
from manim_3d import paraboloid_surface_scene


class ParaboloidSurface(paraboloid_surface_scene(
    captions=("抛物面", "建立三维坐标系", "平面卷成抛物面",
              "等高线：同心圆", "360° 环绕展示",
              "绕轴翻转 · 展示底面", "manim 立体几何 · 第三画"),
)):
    """默认 pace="full"(45s 内容预算)+7 条字幕 = 手工样片效果。"""


class ParaboloidTeaser(paraboloid_surface_scene(duration=16, name="ParaboloidTeaser",
                                                rings=False, annotate=False)):
    """16 秒版:砍等高线/标注,保住环绕+翻面。"""
