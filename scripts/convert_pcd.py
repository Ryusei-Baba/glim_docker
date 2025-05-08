from pathlib import Path
import open3d as o3d

# ベースパスを Path で定義（任意で変更）
base_path = Path.home() / "glim_docker/maps"
ply_file = base_path / "map.ply"
pcd_file = base_path / "map.pcd"

# PLYファイルをPointCloudとして読み込む
point_cloud = o3d.io.read_point_cloud(str(ply_file))

# 読み込んだPointCloudをPCD形式で保存
o3d.io.write_point_cloud(str(pcd_file), point_cloud)

print(f"{ply_file} を {pcd_file} に変換しました。")
