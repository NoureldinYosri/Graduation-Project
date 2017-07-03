import nn_controller, utils

def train(path):
    nn_controller.conduct_experiment(path,[20,20],[5,5],4000,"BFC VS MAG")
    
if __name__ == "__main__":
    path = utils.join_parent("BFC VS MAG", 2)
