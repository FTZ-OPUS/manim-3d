# -*- coding: utf-8 -*-
"""椭球面封装验收 —— 闭曲面模式首发
渲染: cd 本目录 && ~/venvs/manim/bin/manim -qh demo_ellipsoid.py EllipsoidSurface
"""
from manim_3d import ellipsoid_surface_scene


class EllipsoidSurface(ellipsoid_surface_scene(
    captions=("椭球面", "建立三维坐标系", "充气成椭球面",
              "等高线：水平椭圆", "360° 环绕展示",
              "绕轴翻转 · 展示背面", "manim 立体几何 · 第四画"),
)):
    """默认 semi_axes=(2.4, 1.6, 1.2),充气成型+贴面椭圆环+顶点标注。"""


class EllipsoidTeaser(ellipsoid_surface_scene(duration=16, name="EllipsoidTeaser",
                                              rings=False, annotate=False)):
    """16 秒版:砍等高线/标注,保住环绕+翻面。"""
