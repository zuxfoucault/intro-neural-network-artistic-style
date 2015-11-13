# Build OpenCV 3.0.0-bate for Python

## Base Environment

[data science toolbox](http://datasciencetoolbox.org/)

## Reference

1. opencv官方網站的[安裝指南](http://docs.opencv.org/doc/tutorials/introduction/linux_install/linux_install.html)
2. [安裝其他模組](http://stackoverflow.com/questions/26059134/adding-modules-from-opencv-contrib-to-opencv)的指令以及測試方式

## Installation

``` shell
sudo apt-get update

# requirements
sudo apt-get install -y cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev

# clone source code & checkout 3.0.0-beta
git clone https://github.com/Itseez/opencv
cd opencv
git checkout 3.0.0-beta
cd ..

# clone source code & checkout 3.0.0-beta
git clone https://github.com/Itseez/opencv_contrib
cd opencv_contrib
git checkout 3.0.0-beta
cd ..

# let's build
cd opencv
mkdir release
cd release
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D OPENCV_EXTRA_MODULES_PATH=/home/vagrant/opencv_contrib/modules \
      -D BUILD_opencv_xfeatures2d=ON \
      -D WITH_OPENCL=OFF \
      ..  
make
sudo make install
```

