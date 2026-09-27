# -*- coding: utf-8 -*-
"""马鞍面封装验收 —— 几行代码复刻手工样片
渲染: cd 本目录 && ~/venvs/manim/bin/manim -qh demo_saddle.py SaddleSurface
"""
from manim_3d import saddle_surface_scene


class SaddleSurface(saddle_surface_scene(
    captions=("马鞍面", "建立三维坐标系", "平面扭曲成马鞍面",
              "等高线：双曲线族与渐近线", "360° 环绕展示",
              "绕轴翻转 · 展示底面", "manim 立体几何 · 第二画"),
)):
    """默认 pace="full"(45s 内容预算)+7 条字幕 = 手工样片效果。"""


class SaddleTeaser(saddle_surface_scene(duration=16, name="SaddleTeaser",
                                        rings=False, annotate=False)):
    """16 秒版:砍等高线/标注,保住环绕+翻面。"""
