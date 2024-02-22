import cv2

class Pipe:

    def __init__(self, pipe_path):

        self.__pipe_path = pipe_path
        self.pipe = cv2.imread(self.__pipe_path)
        self.__pipe_dimensions = self.pipe.shape
        self.pipe_x = 0
        self.pipe_y = 0

    def get_pipe(self):

        return self.pipe

    def get_pipe_height(self):

        height = self.__pipe_dimensions[0]
        return height

    def get_pipe_width(self):

        width = self.__pipe_dimensions[1]
        return width

    def get_pipe_x(self):

        x_pos = self.pipe_x
        return x_pos

    def get_pipe_y(self):

        y_pos = self.pipe_y
        return y_pos