from models.shared_resource import SharedResource
from models.simulation_state import SimulationState
from controller.simulation_controller import SimulationController
from ui.main_window import MainWindow
def main():
    runtime_state = SimulationState()
    shared_resource = SharedResource()
    controller = SimulationController(runtime_state,shared_resource)
    app = MainWindow(controller)
    app.mainloop()
if __name__ == "__main__":
    main()