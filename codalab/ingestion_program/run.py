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

input_train_pos = os.path.join(train_data, "train/pmts_pos.csv")
input_train_s_hits = os.path.join(train_data, "train/spmt_hits.h5")
input_train_l_hits = os.path.join(train_data, "train/lpmt_hits.h5")
input_train_true_info = os.path.join(train_data, "train/true_info.csv")
#input_train_list = glob.glob(os.path.join(train_data, "/*.csv"))
input_test_l_hits = os.path.join(input_dir, "test/test_l_hits.h5")
input_test_s_hits = os.path.join(input_dir, "test/test_s_hits.h5")   

test_l_hits = pd.read_hdf(input_test_l_hits, mode='r')
test_s_hits = pd.read_hdf(input_test_s_hits, mode='r')

pmts_pos = pd.read_csv(input_train_pos)
spmt_hits = pd.read_hdf(input_train_s_hits, mode='r')
lpmt_hits = pd.read_hdf(input_train_l_hits, mode='r')
true_info = pd.read_csv(input_train_true_info)

sys.path.append(submission_program)

import submission_model

model = submission_model.Model()

pred = model.run(pmts_pos, spmt_hits, lpmt_hits, true_info, test_l_hits, test_s_hits)

answer_path = os.path.join(output_dir, "pred.csv")
pred.to_csv(answer_path, index=False)
