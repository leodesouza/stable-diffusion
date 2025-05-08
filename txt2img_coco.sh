#!/bin/bash
python txt2img_coco.py \
        --ddim_eta 0.0 \
        --n_samples 10 \
        --n_iter 1 \
        --scale 7.5 \
        --ddim_steps 50 \
        --plms \
        --skip_grid \
        --ckpt ./_model_pool/sd-v1-4-full-ema.ckpt \
        --from-file './name_of_your_coco_captions_file.txt' \
        --outdir './path_of_your_targeted_images' \