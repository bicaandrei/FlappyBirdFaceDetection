from domain.pipe_class import Pipe

class PipeRepo:

    def __init__(self):

        pass

    def add_pipe(self, path_to_pipe):

        pipe = Pipe(path_to_pipe)
        return pipe

