# -*- coding: utf-8 -*-
"""几行代码复刻《高斯曲面 · 第一画》完整版 —— manim_3d 封装验收
渲染: cd 本目录 && ~/venvs/manim/bin/manim -qh demo_full.py GaussianSurface
"""
from manim_3d import gaussian_surface_scene


class GaussianSurface(gaussian_surface_scene(
    captions=("高斯曲面", "建立三维坐标系", "平面隆起为彩色曲面",
              "360° 环绕展示", "绕轴翻转 · 展示底面", "manim 立体几何 · 第一画"),
)):
    """默认 pace="full"(45s 内容预算)+全套节拍 = 原版效果。"""
