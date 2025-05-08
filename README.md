# glim_docker
このリポジトリは、GLIMをDocker上で動作させるための環境を提供します。
本ブランチはCUDAを使用するため、NVIDIA GPUおよびCUDA対応ドライバが必要です。
また、GLIMの動作にはROS 2のbagファイルが必要となりますので、事前にご用意ください。

---
### 事前準備
#### Dockerのインストール
[インストール方法（Ubuntu20.04）](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-ja)

#### NVIDIA Container Toolkit 
```
sudo apt update
sudo apt install -y nvidia-container-toolkit
sudo systemctl restart docker
```

---
### インストール
[公式ドキュメント](https://koide3.github.io/glim/docker.html)をカスタマイズしています．
```
git clone https://github.com/Ryusei-Baba/glim_docker.git

# Pull image from docker hub
docker pull koide3/glim_ros2:humble_cuda12.2
```

---
### Docker 起動
```
xhost +local:
```
```
# your_rosbag_path = $HOME/Downloads/rosbag2_2023_03_09-13_46_54
docker run \
  -it \
  --rm \
  --net=host \
  --ipc=host \
  --pid=host \
  --gpus all \
  -e=DISPLAY \
  -e=ROS_DOMAIN_ID \
  -v $(realpath glim_docker/config):/glim/config \
  -v $(realpath glim_docker/outputs):/tmp/dump \
  -v $HOME/Downloads/rosbag2_2023_03_09-13_46_54:/glim/data \
  koide3/glim_ros2:humble_cuda12.2 \
  ros2 run glim_ros glim_rosbag /glim/data --ros-args -p config_path:=/glim/config
```

---
### 保存方法
rosbagの再生が完了した後、以下の2種類の方法から保存形式を選択できます。
1. ターミナルで Ctrl + C
2. GUIで☓ボタン（ウィンドウの右上にある）

確認
```
ls glim_docker/outputs
```

---
### PLYファイルとして保存
```
docker run \
  -it \
  --rm \
  --net=host \
  --ipc=host \
  --pid=host \
  --gpus all \
  -e=DISPLAY \
  -e=ROS_DOMAIN_ID \
  -v $(realpath glim_docker/outputs):/tmp/dump \
  -v $(realpath glim_docker/maps):/tmp/dump/map \
  koide3/glim_ros2:humble_cuda12.2 \
  ros2 run glim_ros offline_viewer --map_path=/tmp/dump
```
File > Save > Export Points > Other Locations > tmp > dump > map > Name: map.ply > OK

---
### PLYファイルからPCDファイルへの変換
#### インストール
```
pip install open3d

```
#### 変換スクリプト
```
python3 glim_docker/scripts/convert_pcd.py
```

---
### 地図を2次元に圧縮したいですか？
[おすすめリポジトリ](https://github.com/cafeline/pointcloud2pgm_slicer)