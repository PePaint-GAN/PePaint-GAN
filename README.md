# Readme.md

models.py: all structure definition of models.

train.py: the main entry of the code, execute this file to train the model, the intermediate results and checkpoints will be automatically saved periodically into a folder "train_results".
operation.py: the helper functions and data loading methods during training. (used in train.py)
diffaug.py: used for training more efficiently by applying random transformations to the input data. (used in train.py)

eval.py: generates images from a trained generator into a folder
newimage.py: simpler image generation

newIS.py: calculate inception score

--------------------------

Training:
python train.py


Generate New Images:
python eval.py
or
python newimage.py


Measure FID:
python -m pytorch_fid [original images folder] [generated images folder]
python -m pytorch_fid ./datasets/150-shot-col/img ./train_results/Colonial_PaintGAN/eval_10000/img


Measure IS:
newIS.py (update image_directory variable in file with the folder of the generated images)