class ServicePipe:

    def __init__(self, pipe_repository):

        self.__pipe_repository = pipe_repository

    def add_pipe(self, path_to_pipe):

        return self.__pipe_repository.add_pipe(path_to_pipe)