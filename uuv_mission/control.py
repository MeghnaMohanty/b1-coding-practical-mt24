class PDController:
    def __init__(self, KP=0.15, KD=0.6): 
        self.KP = KP
        self.KD = KD
        self.previous_error = 0
        
    #Takes the reference and output as arguments and returns the control action
    def compute_control(self, reference, output):
        error = reference - output
        derivative = error - self.previous_error
        control_action = self.KP * error + self.KD * derivative
        self.previous_error = error
        return control_action