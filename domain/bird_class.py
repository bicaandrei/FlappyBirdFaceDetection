import cv2

class Bird:

    def __init__(self, bird_path):

       self.__bird_path = bird_path
       self.bird = cv2.imread(self.__bird_path)
       self.bird_x = 0
       self.bird_y = 0
       self.__bird_dimensions = self.bird.shape

    def get_bird(self):

        return self.bird

    def get_bird_height(self):

        height = self.__bird_dimensions[0]
        return height

    def get_bird_width(self):

        width = self.__bird_dimensions[1]
        return width

    def get_bird_x(self):

        x_pos = self.__bird_x
        return x_pos

    def get_bird_y(self):

        y_pos = self.__bird_y
        return y_pos