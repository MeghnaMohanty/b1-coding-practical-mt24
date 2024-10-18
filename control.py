# control.py
def pd_controller(KP: float, KD: float):
    def controller(error_t: float, error_delta: float) -> float:
        return KP * error_t + KD * error_delta
    return controller
