import nn_controller, utils

def train(path):
    nn_controller.conduct_experiment(path,[20,20],[5,5],4000,"free_kicks")

if __name__ == "__main__":
    path = utils.join_parent("free_kicks", 2)
    train(path);