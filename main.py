from repository.pipe_repository import PipeRepo
from repository.bird_repository import BirdRepo
from game_service.pipe_service import ServicePipe
from game_service.bird_service import BirdService
from game_ui.ui import UI

def main():

    pipe_repository = PipeRepo();
    bird_repository = BirdRepo();
    bird_service = BirdService(bird_repository)
    pipe_service = ServicePipe(pipe_repository)
    console = UI(bird_service, pipe_service)
    console.game()

main()