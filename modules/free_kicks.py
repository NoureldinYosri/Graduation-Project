import nn_controller, utils

if __name__ == "__main__":
    path = utils.join_parent("free_kicks", 2)
    nn_controller.conduct_experiment(path,[20,20],[5,5],4000,"free_kicks")