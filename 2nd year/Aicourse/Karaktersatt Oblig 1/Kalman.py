class Kalman():
    def __init__(self):
        """ Initialize filter """
        self.t_d = 1 # Time delta

        # Initial values
        self.pred_p = 0.0
        self.pred_v = 0.0
        self.pred_a = 1.0e-2

        # Do not change these.
        self.alpha = 2.0e-2
        self.beta = 8.0e-5
        self.gamma = 3.0e-7


    def estimate_current_position_and_velocity(self, zn):
        
        # Estimates
        self.e_p = self.pred_p + self.alpha * (zn - self.pred_p)
        self.e_v = self.pred_v + self.beta * ((zn - self.pred_p)/self.t_d)
        self.e_a = self.pred_a + self.gamma * ((zn - self.pred_p)/((self.t_d**2)*0.5))

        # Predictions
        self.pred_p = self.e_p + self.e_v * self.t_d + self.e_a * ((self.t_d**2)*0.5)
        self.pred_v = self.e_v + self.e_a * self.t_d
        self.pred_a = self.e_a

        return self.e_p, self.e_v
