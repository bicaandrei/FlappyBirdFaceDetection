from domain.bird_class import Bird

class BirdRepo:

    def __init__(self):

        pass

    def add_bird(self, path_to_bird):

        bird = Bird(path_to_bird)
        return bird



