import nn_controller, utils

if __name__ == "__main__":
    path = utils.join_parent("pitch-invasion", 2)
    nn_controller.conduct_experiment(path,[50,50],[30,30,30],4000,"pitch-invasion")