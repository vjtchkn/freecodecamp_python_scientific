class Rectangle:
    def __init__(self, w, h):
        self.set_width(w)
        self.set_height(h)

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        if self.width <= 50 and self.height <= 50:
            return ("*" * self.width + "\n") * self.height
        else:
            return "Too big for picture."

    def get_amount_inside(self, sh):
        ratio_width = self.width // sh.width
        ratio_height = self.height // sh.height
        return ratio_width * ratio_height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, s):
        self.set_side(s)

    def set_side(self, s):
        self.width = s
        self.height = s

    def set_width(self, w):
        self.set_side(w)

    def set_height(self, h):
        self.set_side(h)

    def __str__(self):
        return f"Square(side={self.width})"
