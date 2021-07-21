# Image Super Resolution Using CNN
(This is also the README for our team project)

We used the following dataset for the project:-
- https://www.tensorflow.org/datasets/catalog/div2k#div2kbicubic_x2_default_config : 
   This is the link for the div2K dataset in TensorFlow which we used in the project. It contains 900 pairs of images, 800 test and 100 validation, with each pair of images containing a low resolution image and it's high resolution
   counterpart. We trained our CNN by increasing the resolution of the low resolution images using our NN and measuring it's performance vis-a-vis the high resolution image.
- https://arxiv.org/pdf/1501.00092.pdf : We obtained the neural network architecture and implementation details from this paper.

- Results and comparisons of PSNR values (all neural network models were trained on 100,000 50 x 50 images) :

   | **Ground Truth**    | **Grayscale (dB)** | **RGB image (dB)** |
   | -------- | ------ | ------ |
   | Bicubic   | 49.63   |  45.42  |
   | With DCT bases (and without dense patches)   | 17.95   | --- (Grayscale is already low) |
   | Without DCT and without dense patches  | 28.79   | 28.14 |
   | Without DCT + Dense patches | 29.85 | 28.98 |
