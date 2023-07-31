import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from utils.clip_mapping_utils import load_map, get_new_pallete, get_new_mask_pallete
from utils.clip_utils import get_text_feats
import clip
import torch


from utils.classes_hex_dict import classes_hexCode_dict,dict2list


device = "cuda" if torch.cuda.is_available() else "cpu"
# clip_version = "ViT-B/32"
clip_version = "RN50"
clip_feat_dim = {'RN50': 1024, 'RN101': 512, 'RN50x4': 640, 'RN50x16': 768,
                'RN50x64': 1024, 'ViT-B/32': 512, 'ViT-B/16': 512, 'ViT-L/14': 768}[clip_version]
clip_model_path = {'RN50': "./RN50.pt", 'RN101':"" , 'RN50x4': "", 'RN50x16': "",
                'RN50x64': "", 'ViT-B/32': "ViT-B-32.pt", 'ViT-B/16':"" , 'ViT-L/14':"" }[clip_version]
clip_model, preprocess = clip.load(clip_model_path)  # clip.available_models()
# clip_model, preprocess = clip.load(clip_version)  # clip.available_models()
clip_model.to(device).eval()

userInst_list=["I want to sit","I want to go out through the second door.","四号门"]
userInst_text_feats =get_text_feats(userInst_list, clip_model, clip_feat_dim)
print(f"text_feats.shape:{userInst_text_feats.shape}")   

# mapPoint_list=list(classes_hexCode_dict.keys())
mapPoint_list=dict2list
mapPoint_text_feats = get_text_feats(mapPoint_list, clip_model, clip_feat_dim)
print(f"text_feats.shape:{mapPoint_text_feats.shape}")  


similarity_score=userInst_text_feats @ mapPoint_text_feats.T
print(similarity_score)

ok_index=np.argmax(similarity_score, axis=1)

for j,i in zip(range(len(mapPoint_list)),ok_index):
        print(userInst_list[j],':',mapPoint_list[i],similarity_score[j][i])

