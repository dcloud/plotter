import math

import vsketch
from numpy._core.numerictypes import ScalarType
from shapely.affinity import scale
from shapely.geometry import LineString, Point, Polygon


class FirstVskSketch(vsketch.SketchClass):
    # _hypotrochoid: https://mathworld.wolfram.com/Hypotrochoid.html
    # Unit circle?
    def _hypotrochoid(self, degrees=range(361), a=4, b=1, h=lambda a=2, b=1: a - b):
        thetas = (math.radians(x) for x in degrees)
        pts = []
        h_val = h(a, b)
        for t in thetas:
            x = (a - b) * math.cos(t) + h_val * math.cos((a - b) / b * t)
            y = (a - b) * math.sin(t) - h_val * math.sin((a - b) / b * t)
            pts.append([x, y])
        return pts

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("letter", landscape=True, center=False)
        vsk.scale("1mm")
        vsk.translate(24, 24)

        pts = self._hypotrochoid(a=9)
        s = LineString(pts)
        # s = scale(s, xfact=2, yfact=2)

        cols = 7
        rows = 4
        x_offset = 38
        y_offset = 54
        for r in range(rows):
            for c in range(cols):
                vsk.geometry(s)
                vsk.translate(x_offset, 0)
            vsk.translate(-x_offset * cols, y_offset)
        print("done")

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    FirstVskSketch.display()
