exp_id = 'custom_5vals_colors_all_30ep_data2_randaug_50ep'
load_model = '../pretrained/fairmot_dla34.pth'
num_epochs = 50
lr_step = '15'
data_cfg = '../src/lib/cfg/custom.json'
color_weight = 1.05
ball_weight = 0.0
num_teams = 152
randaug = True