### 地图语义点向量化


```py
    ## .pt文件联网时可下载保存本地
    # clip_version = "ViT-B/32"
    clip_version = "RN50"
    clip_feat_dim = {'RN50': 1024, 'RN101': 512, 'RN50x4': 640, 'RN50x16': 768,
                    'RN50x64': 1024, 'ViT-B/32': 512, 'ViT-B/16': 512, 'ViT-L/14': 768}[clip_version]
    clip_model_path = {'RN50': "./RN50.pt", 'RN101':"" , 'RN50x4': "", 'RN50x16': "",
                    'RN50x64': "", 'ViT-B/32': "ViT-B-32.pt", 'ViT-B/16':"" , 'ViT-L/14':"" }[clip_version]
    clip_model, preprocess = clip.load(clip_model_path)  # clip.available_models()
    # clip_model, preprocess = clip.load(clip_version)  # clip.available_models()
```
