# -*- coding: utf-8 -*-
"""圆环面封装验收 —— 闭曲面 (√(x²+y²)−R)²+z²=r²
渲染: cd 本目录 && ~/venvs/manim/bin/manim -qm demo_torus.py TorusTeaser   (720p 16秒档)
"""
from manim_3d import torus_surface_scene


class TorusSurface(torus_surface_scene(
    captions=("圆环面", "建立三维坐标系", "充气成圆环面",
              "等高线：水平成对圆环", "360° 环绕展示",
              "绕轴翻转 · 展示背面", "manim 立体几何 · 第五画"),
)):
    """默认 major_radius=2.0, minor_radius=0.5(参考图 4:1 比例)。"""


class TorusTeaser(torus_surface_scene(duration=16, name="TorusTeaser",
                                      rings=False, annotate=False)):
    """16 秒版:砍等高线/标注,保住环绕+翻面。"""
