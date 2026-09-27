# manim-3d 🧊 Manim 三维几何与动画

**manim-3d** 是 [Manim](https://www.manim.community/) Community Edition 的立体几何补充库。
高斯曲面、马鞍面、抛物面、椭球面、圆环面、单叶双曲面——这些经典三维曲面的整套演示动画
（成型 → 等高线 → 360° 环绕 → 翻面 → 特征点标注），被封装成**一个工厂函数 + 几个参数**。

*One-liner 3D surface animation presets for Manim CE: rainbow-shaded surfaces, orbit & flip camera work, paced timelines from 10s to 45s — in a class definition.*

---

## 为什么需要它

不用库，手写一支"平面隆起成彩虹高斯曲面 → 底面等高线 → 360° 环绕 → 翻面 → 峰顶标注"的 3D 视频，
你要面对的是：ThreeDScene 相机调度、`set_fill_by_value` 高度色带、HUD 固定帧字幕（还得躲开
"字幕被 3D 透视拉斜"的暗坑）、等高线解析与 z-fighting、深度遮挡、逐拍时长编排……
**130+ 行起步，坑还都不在文档里。**

用 manim-3d：

```python
from manim_3d import gaussian_surface_scene

class GaussianSurface(gaussian_surface_scene()): pass
```

6 行，渲染命令照旧：`manim -qh demo.py GaussianSurface`。
配色、运镜、字幕、节拍、时长——全部预设到审美在线的状态；想不一样，每个环节都有参数。

| 高斯曲面 | 马鞍面 | 抛物面 |
|---|---|---|
| ![](assets/demo_gaussian.gif) | ![](assets/demo_saddle.gif) | ![](assets/demo_paraboloid.gif) |
| **椭球面** | **圆环面** | **单叶双曲面** |
| ![](assets/demo_ellipsoid.gif) | ![](assets/demo_torus.gif) | 📷 见 examples |

以上全部由本库直接渲染输出，无后期。

## 特性

- 🎬 **几行代码出片** —— 类定义即视频；六个曲面开箱即用，覆盖图曲面与闭曲面两种形态
- ⏱️ **权重配速** —— 同一套动画，45s 完整版与 10s 混剪版只是一个参数：每拍按权重伸缩、
  夹住"难看下限"，压不下自动按优先级砍可选拍并在日志告诉你砍了啥，主线一个不少
- 🌈 **预设即美观** —— 七段彩虹高度色带（海洋/熔岩可换）、金色大字幕、环绕恒转满一整圈、
  标注自动防遮挡（3D 天线 / 屏幕 HUD 两种方案按几何自动选择）
- 🔧 **全参数可调** —— 换函数、换半轴、换配色主题、五个节拍开关、字幕槽位对位，
  每一处预设都留了改口
- 🤫 **字幕默认关** —— 片子干干净净；要讲课时把字幕列表传进去，自动按节拍挂载
- 🧭 **替你踩平的坑** —— fixed-in-frame 注册、Transform 字形错配、partial 缓存失效、
  深度遮挡……全部在库内处理，使用者无需知晓

## 安装

```bash
pip install manim-3d          # PyPI（发布后）
# 或从源码
git clone https://github.com/FTZ-OPUS/manim-3d && pip install -e ./manim-3d
```

依赖：Python ≥ 3.10、[Manim CE](https://docs.manim.community/) ≥ 0.21（含其自身依赖与 LaTeX）。

## 快速开始

六个曲面，同一套 API——

```python
from manim_3d import (gaussian_surface_scene, saddle_surface_scene,
                       paraboloid_surface_scene, ellipsoid_surface_scene,
                       torus_surface_scene, hyperboloid_one_sheet_scene)

class GaussianSurface(gaussian_surface_scene()): pass
class SaddleSurface(saddle_surface_scene()): pass
class ParaboloidSurface(paraboloid_surface_scene()): pass
class EllipsoidSurface(ellipsoid_surface_scene()): pass
class TorusSurface(torus_surface_scene()): pass
class Hyperboloid(hyperboloid_one_sheet_scene()): pass
```

> 完整可运行示例见 [`examples/`](examples/)（每个曲面一个文件，含字幕版与 16 秒速览版）。

### 加字幕

字幕默认关闭。要讲课时传入字幕列表，自动按节拍挂载（整行淡出淡入，绝不形变糊字）：

```python
class SaddleSurface(saddle_surface_scene(
    captions=("马鞍面", "建立三维坐标系", "平面扭曲成马鞍面",
              "等高线：双曲线族与渐近线", "360° 环绕展示",
              "绕轴翻转 · 展示底面", "manim 立体几何 · 第二画"),
)): pass
```

### 控时长（混剪友好）

```python
class SaddleFast(saddle_surface_scene(pace="fast", name="SaddleFast")):   # 10 秒
class SaddleTeaser(saddle_surface_scene(duration=16, name="SaddleTeaser")):  # 16 秒
```

`duration=16` 时放不下全部节拍？库会按 **等高线 → 平面 → 标注 → 环绕 → 翻面** 的优先级
自动砍拍并打印，保住"成型 → 环绕 → 翻面"主线——混剪快切时每一拍依然完整。

### 换函数 / 换配色 / 换形状

```python
import numpy as np
from manim_3d import gaussian_surface_scene

# 高斯曲面接受任意 z=f(x,y)，峰值自动归一化，不用调坐标轴
class MySurface(gaussian_surface_scene(
    func=lambda x, y: np.exp(-((x - 1) ** 2 + y * y)),
    colors="ocean",                       # rainbow / ocean / magma 或自定义色带
)): pass

# 椭球三轴随意改，公式自动跟着变
class MyEgg(ellipsoid_surface_scene(semi_axes=(2.6, 1.4, 1.8))): pass
```

## 参数一览

| 参数 | 默认 | 说明 |
|---|---|---|
| `func` / `func_tex`（高斯） | 内置高斯 | 任意 `z=f(x,y)`；公式 LaTeX 自动/手填 |
| `semi_axes`（椭球） | (2.4, 1.6, 1.2) | 半轴 (a, b, c)，坐标轴等比缩放防畸变 |
| `major_radius` / `minor_radius`（圆环面） | 2.0 / 0.5 | 环半径 / 管半径 |
| `waist_radius` / `z_extent`（单叶双曲面） | 1.0 / 1.5 | 腰圆半径 / 上下截断高度 |
| `domain` | ±2.2~2.6 | 图曲面 x/y 定义域 |
| `colors` | "rainbow" | `rainbow / ocean / magma` 或 `[(hex, 0~1)...]` |
| `height` | 1.0~1.2 | 峰值自动归一化目标高度 |
| `axes / rings / orbit / flip / annotate` | True | 五个节拍开关 |
| `captions` | None | 字幕按节拍槽位对位，不传 = 无字幕 |
| `duration` / `pace` | "full" | 内容预算秒数；`fast`=10s / `normal`=24s / `full`=45s |

### 字幕槽位

按曲面节拍序列位置对位：高斯 6 槽（片头/坐标轴/隆起/环绕/翻面/片尾），
其余 7 槽（多一个"等高线"槽）。传少于槽数的条目时自动截取。

### 配速规则

每拍带三个数：**参考时长**（完整版节奏）、**下限**（低于就难看的压缩底线）、
**上限倍率**（拉伸顶格）。`duration` 先等比分摊，夹进上下限迭代收敛；
全体顶到下限仍放不下才砍拍。环绕拍永远**恰好转满一整圈**（角速度随时长自适应）。

## 六曲面差异一览

| 曲面 | 方程 | 成型 | 等高线 | 标注 |
|---|---|---|---|---|
| 高斯曲面 | z = e^(−x²−y²) | 平面隆起 | 地板投影圆 | 峰顶 3D 标签 |
| 马鞍面 | z = x² − y² | 平面扭曲 | 双曲线族 + 渐近线 | 鞍点 HUD 标签 |
| 抛物面 | z = x² + y² | 平面卷起 | 贴面同心圆 | 顶点 HUD 标签 |
| 椭球面 | x²/a²+y²/b²+z²/c²=1 | 充气成型 | 贴面水平椭圆环 | 上顶点 3D 标签 |
| 圆环面 | (√(x²+y²)−R)²+z²=r² | 充气成型 | 贴面水平成对圆环 | 最高点 3D 标签 |
| 单叶双曲面 | x²+y²−z²=a² | 充气成型 | 水平圆族（含腰圆） | 腰点 HUD 标签 |

标注方案按几何自动选择：特征点外露用 3D 标签（天线虚线），被曲面环抱则用
**相机定格投影 + 固定帧** 的屏幕 HUD 标签，永不被深度遮挡。

## 设计边界（诚实声明）

- 高斯等高线为径向近似，仅旋转对称函数精确；一般函数建议 `rings=False`
- 马鞍/抛物面/圆环面/单叶双曲面为固定几何预设（解析等高线依赖具体方程），
  任意函数请走高斯入口
- 双叶双曲面等参数曲面在路线图上

## 用它做过的片子

《立体几何 N 画》系列（B站）：高斯曲面 · 第一画 / 马鞍面 · 第二画 / 抛物面 · 第三画 /
椭球面 · 第四画 / 圆环面 · 第五画 / 单叶双曲面 · 第六画 —— 全部由本库（或其前身脚本）直接渲染。

## License

[MIT](LICENSE) © FTZ-OPUS
