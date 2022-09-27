# Brent A. Thorne <brentathorne@gmail.com> 
#
# Render animation using the following command
#
# $ manim -pql midpoint_poly_animation.py PolygonExample

from manim import *

class PolygonExample(Scene):
    def construct(self):
        p0 = [[3.0, 0.0, 0.0],
  [0.9270510077476501, 2.8531696796417236, 0.0],
  [-2.427051067352295, 1.7633557319641113, 0.0],
  [-2.427051067352295, -1.7633557319641113, 0.0],
  [0.9270510077476501, -2.8531696796417236, 0.0]] 

        p1 = [[1.963525414466858, -1.4265848398208618, 0.0],
  [1.963525414466858, 1.4265848398208618, 0.0],
  [-0.75, 2.308262586593628, 0.0],
  [-2.427051067352295, 1.0164395367051604e-20, 0.0],
  [-0.75, -2.308262586593628, 0.0]] 

        p2 =[[2.427051067352295, -1.7633559703826904, 0.0],
  [2.427051067352295, 1.7633559703826904, 0.0],
  [-0.9270510077476501, 2.8531696796417236, 0.0],
  [-3.0, 1.2563883957560981e-20, 0.0],
  [-0.9270510077476501, -2.8531696796417236, 0.0]]  

        p3 = [[0.75, -2.308262586593628, 0.0],
  [2.427051067352295, 6.2819419787804906e-21, 0.0],
  [0.75, 2.308262586593628, 0.0],
  [-1.963525414466858, 1.4265848398208618, 0.0],
  [-1.963525414466858, -1.4265848398208618, 0.0]]

        p4 = [[0.9270509481430054, -2.8531692028045654, 0.0],
  [2.999999761581421, 7.764906776542227e-21, 0.0],
  [0.9270509481430054, 2.8531692028045654, 0.0],
  [-2.427050828933716, 1.7633554935455322, 0.0],
  [-2.427050828933716, -1.7633554935455322, 0.0]]

        myPoly0 = Polygon(*p0, color=PURPLE_B)
        myPoly1 = Polygon(*p1, color=RED)
        myPoly2 = Polygon(*p2, color=RED)
        myPoly3 = Polygon(*p3, color=PURPLE_B)
        myPoly4 = Polygon(*p4, color=PURPLE_B)
        self.play(Create(myPoly0))  # animate the creation of the poly 
        self.play(TransformFromCopy(myPoly0, myPoly1))  # interpolate the one ploy into another 
        self.play(FadeOut(myPoly0))

        self.play(Transform(myPoly1, myPoly2))  
        self.play(TransformFromCopy(myPoly1, myPoly3))
        self.play(FadeOut(myPoly1))
        self.play(Transform(myPoly3, myPoly4))  
