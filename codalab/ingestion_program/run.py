import sys, os
import glob
import numpy as np
import pandas as pd


ingestion_program = sys.argv[1] 
train_data = sys.argv[2] 
output_dir = sys.argv[3] 
input_dir = sys.argv[4] 
#shared_directory = sys.argv[5]
submission_program = sys.argv[5] 


input_train_data = os.path.join(train_data, "train_data.csv")
#input_train_list = glob.glob(os.path.join(train_data, "/*.csv"))
input_test_data = os.path.join(input_dir, "test_data.csv")


test_data = pd.read_csv(input_test_data)

train_data = pd.read_csv(input_train_data)

sys.path.append(submission_program)

import submission_model

model = submission_model.Model()

pred = model.run(train_data, test_data)

answer_path = os.path.join(output_dir, "pred.csv")
pred.to_csv(answer_path, index=False)
