import numpy as np
import pandas as pd
import sys


class Model:
    def run(self, data):

        """
        data: dict, {name: pd.DataFrame}
        """

        x = data['users_test']["uid"]
        pred = pd.DataFrame({
            "uid": x,
            "is_leader": np.ones(len(x)),
        })

        return pred
