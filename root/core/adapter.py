import rpy2.robjects as robjects

class Adapter:
    def __init__(self):
        self.r_adapter = robjects.r

    def __del__(self):
        print("Adapter killed")
