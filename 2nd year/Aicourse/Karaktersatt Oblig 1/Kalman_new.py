import numpy as np
from copy import deepcopy

class Kalman():
    def __init__(self):
        """ Initialize filter """
        self.t_d = 1.0
        self.F = np.array([[1.0, self.t_d, 0.5*(self.t_d**2)], [0.0, 1.0, self.t_d], [0.0, 0.0, 1.0]]) # State transition matrix
        self.P = np.diag([3400.0, 0.0315, 8.26e-7]) # Estimate uncertainty matrix, changing these values does not really matter as the filter will change it to a decent value on it's first iteration.
        self.H = np.array([[1.0], [0.0], [0.0]]).T # Observation matrix, we only get 1 of 3 values. 
        self.R = np.array([[22_500.0]]) # Measurement uncertainty, which we can get from HitTheTarget.py by doing 150^2

        """ The following variables can be removed, but i will keep them to let the function be in it's 'fulfilled' state.
        If i was to remove them i could not use this Kalman Filter on other projects later, 
        I will still have to search up the implementation of starting matrixes but leaving the calculation as a 'format'. """
        self.G = 0 # Control matrix, we don't have this since we only have 1 input value.
        self.Un = 0 # Control variable, same as above.
        self.Q = 0 # Process noise, excepting zero cpu noise


        # Initial values
        self.x = np.array([108.0, 0.7, 0.0015]) # Values gathered from studying HitTheTarget.py
        self.Xn = np.dot(self.F, self.x) + np.dot(self.G, self.Un) + self.Q
        self.P = np.dot(np.dot(self.F, self.P), self.F.T) + self.Q
        
    def estimate_current_position_and_velocity(self, zn):
        # Estimate next move
        self.Kn = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(np.dot(self.H, np.dot(self.P, self.H.T) + self.R))) # Kalman Gain
        
        self.Xn = self.Xn + np.dot(self.Kn, (zn - np.dot(self.H, self.Xn))) # State update equation
        self.current_x = deepcopy(self.Xn) # Save value to return

        # Predict next move
        self.P = np.dot(np.dot(np.eye(3) - np.dot(self.Kn, self.H), self.P), \
            (np.eye(3) - np.dot(self.Kn, self.H)).T) + np.dot(np.dot(self.Kn, self.R), self.Kn.T) # Covarianve update equation
        
        self.Xn = np.dot(self.F, self.Xn) + np.dot(self.G, self.Un) + self.Q # State extrapolation equation

        self.P = np.dot(np.dot(self.F, self.P), self.F.T) + self.Q # Covariance extrapolation equation

        return self.current_x[0], self.current_x[1]
