#!/bin/bash
python txt2img_coco.py \
        --ddim_eta 0.0 \
        --n_samples 1 \
        --n_iter 1 \
        --scale 7.5 \
        --ddim_steps 30 \
        --plms \
        --skip_grid \
        --ckpt /home/swf_developer/storage/checkpoints/stable_diffusion/sd-v1-4-full-ema.ckpt \
        --from-file '/home/swf_developer/stable-diffusion/scripts/coco_captions_10000.txt' \
        --outdir '/home/swf_developer/storage/attack/targeted_images' \



        

