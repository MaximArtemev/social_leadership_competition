import numpy as np
import pandas as pd
import sys


class Model:
    def run(self, train_data, test_data):

        """
        train_data - train data
        test_data - test data

        Method returns dataframe with predictions.
 
        """

        x = test_data["uid"]
        pred = pd.DataFrame({
            "uid": x,
            "is_leader": np.zeros(len(x)),
        })

        return pred
