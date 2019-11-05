import sys, os
import glob
import numpy as np
import pandas as pd

# path arguments
ingestion_program = sys.argv[1] 
train_data = sys.argv[2] 
output_dir = sys.argv[3] 
input_dir = sys.argv[4] 
submission_program = sys.argv[5] 

# read the data however you like
csv_files = glob.glob(train_data + '/*.csv')
data = {name.split('/')[-1]: pd.read_csv(os.path.join(name)) for name in csv_files}


# our file with the solution
sys.path.append(submission_program)
import submission_model

model = submission_model.Model()

# you can rewrite your model interface

pred = model.run(data)

# write your prediction to the output_dir
answer_path = os.path.join(output_dir, "prediction.csv")
pred.to_csv(answer_path, index=False)
