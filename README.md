# A Neural Algorithm of Artistic Style

- [A Neural Algorithm of Artistic Style](http://arxiv.org/abs/1508.06576) - [pdf](pdf/a-neural-algorithm-of-artistic-style.pdf)


- [Texture Synthesis Using Convolutional Neural Networks](http://arxiv.org/abs/1505.07376) - [pdf](pdf/texture-synthesis-using-cnn.pdf)
- [bethgelab](https://bethgelab.org/deepneuralart/) where you can download the [caffe model](https://bethgelab.org/media/uploads/deeptextures/vgg_normalised.caffemodel).

[TOC]

## let's do some searches

### Google Search: neural algorithm artistic style

1. the paper link
   
2. [GitXiv link](http://gitxiv.com/posts/jG46ukGod8R7Rdtud/a-neural-algorithm-of-artistic-style)
   
   1. [jcjohnson](https://github.com/jcjohnson/neural-style) it's lua, skip.
      
   2. [kaishengtai](https://github.com/kaishengtai/neuralart) it's lua, skip.
      
   3. it's a terminal snapshot. (terminal is a linux cloud service)
      
      You will have to pay $0.992/hour if you would like to use this snapshot.
      
   4. [andersell](https://github.com/andersbll/neural_artistic_style) it's python, finally.
      
   5. [bamos](https://github.com/bamos/dream-art) it's lua, skip
      
      Bamos combines "google deepdream" with "neural algorithm of artistic style".
      
      We will talk about "google deepdream" later, if we have time.
      
   6. [mbartoli](https://github.com/mbartoli/neural-animation) it's lua, skip
      
      mbartoli uses this technique on video.
      
      it's not very smooth between frames though.
      
   7. [Lasagne](https://github.com/Lasagne/Recipes/blob/master/examples/styletransfer/Art%20Style%20Transfer.ipynb) it's a ipython notebook script.
      
   8. [memisevic](https://github.com/memisevic/artify) it's python, again!
      
   9. [fzliu](https://github.com/fzliu/style-transfer) it's python, lol.

### github search: neural art

1. [rainmakerr](https://github.com/rainmakerr/neural_art) it mentions [docker container](http://ryankennedy.io/running-the-deep-dream/)
2. [jayelm](https://github.com/jayelm/neural-art) it has a [wikiart](http://www.wikiart.org) crawler

## Outline

1. get environment ready
2. play with some images
3. talk about the concept
4. google deepdream / deep learning

## Environment

### Let's pick a repository

- [andersbll](https://github.com/andersbll/neural_artistic_style) using DeepPy (andresbll owns DeepPy)
- [Lasagne](https://github.com/Lasagne/Recipes/blob/master/examples/styletransfer/Art%20Style%20Transfer.ipynb) using theano
- [memisevic](https://github.com/memisevic/artify) using theano
- [fzliu](https://github.com/fzliu/style-transfer) using Caffe
- [rainmakerr](https://github.com/rainmakerr/neural_art) using Caffe

### Deep learning libraries

[reference](http://www.kdnuggets.com/2015/06/popular-deep-learning-tools.html)

- Caffe (c++, python, matlab)
- theano (python)
- DL4J (java)
- Torch7 (lua)

### Failure

- I picked rainmakerr's repository
  - pulling docker failed
  - build from github failed
- you can pick suitable docker at [docker hub](https://hub.docker.com/)
  - I also tried [kchentw](https://hub.docker.com/r/kchentw/neural-style/). Failed, again.

### [DIY] build caffe

[Build Caffe for Google DeepDream](extra/Build Caffe for Google DeepDream.md)

## Let's Play

[fzliu/style-transfer](https://github.com/fzliu/style-transfer)

- scripts/download_models.sh
- play with style.py

## Concept

- neural network
- convolutional neural network
- style由小到大，content由大到小

### Other Keywords

- [imagenet](http://www.image-net.org)
- [what's vgg](http://www.robots.ox.ac.uk/~vgg/research/deep_eval/)

## Extra

### Google DeepDream

- what's google deepdream really does ?


- comparison with neural network artistic style ?

### Deep Learning Resources

- [ICML 2015压轴讨论总结：6大神畅谈深度学习的未来](http://toutiao.com/a4906733241/)
- [tutorial](http://deeplearning.stanford.edu/wiki/index.php/UFLDL教程) by Andrew Ng / Stanford
- [A Neural Network in 11 lines of Python (Part 1)](http://iamtrask.github.io/2015/07/12/basic-python-network/)
- youtube search : Deep Learning
- [Google Research Blog](http://googleresearch.blogspot.tw)
- [Google Deep Mind](http://deepmind.com/publications.html)
- [51個大陸網友的學習筆記](http://www.cnblogs.com/tornadomeet/tag/Deep%20Learning/) @2013
- [tutorial](https://developer.nvidia.com/deep-learning-courses) from NVIDIA
- [十大](http://dataconomy.com/10-machine-learning-experts-you-need-to-know/)
- [八卦](http://www.hdb.com/article/6eju)

### Preparation Hint

1. follow [dstb](http://datasciencetoolbox.org)
   
   1. install virtualbox
   2. install vagrant
   3. create dstb vm
   4. sudo apt-get update
   
2. ```git clone https://github.com/fzliu/style-transfer```
   
   exec https://github.com/fzliu/style-transfer/blob/master/scripts/download_models.sh
   
3. ```wget http://dl.caffe.berkeleyvision.org/bvlc_googlenet.caffemodel```
   
   if you would like to play with google deepdream