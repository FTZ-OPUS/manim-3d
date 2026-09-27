# -*- coding: utf-8 -*-
"""单叶双曲面封装验收 —— x²+y²−z²=1,腰圆为签名特征
渲染: cd 本目录 && ~/venvs/manim/bin/manim -ql demo_hyperboloid.py HyperboloidTeaser  (480p 16秒档)
"""
from manim_3d import hyperboloid_one_sheet_scene


class HyperboloidOneSheet(hyperboloid_one_sheet_scene(
    captions=("单叶双曲面", "建立三维坐标系", "充气成单叶双曲面",
              "等高线：水平圆族与腰圆", "360° 环绕展示",
              "绕轴翻转 · 展示背面", "manim 立体几何 · 第六画"),
)):
    """默认 waist_radius=1.0, z_extent=1.5(端口半径 √(1+1.5²)≈1.80)。"""


class HyperboloidTeaser(hyperboloid_one_sheet_scene(duration=16, name="HyperboloidTeaser",
                                                    rings=False, annotate=False)):
    """16 秒版:砍等高线/标注,保住环绕+翻面。"""
