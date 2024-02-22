class BirdService:

    def __init__(self, pipe_repository):

        self.__pipe_repository = pipe_repository

    def add_bird(self, path_to_bird):

        return self.__pipe_repository.add_bird(path_to_bird)