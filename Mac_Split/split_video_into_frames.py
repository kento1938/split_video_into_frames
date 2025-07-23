import cv2
import os

# 使い方例
video_path = "sample_video.mp4"      # 動画のパス
output_dir = "output_frames"         # 保存先フォルダ
X = 5  


def split_video_into_frames(video_path, output_dir, X):
    # 保存先ディレクトリの作成
    os.makedirs(output_dir, exist_ok=True)

    # 動画を読み込む
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 分割位置のフレーム番号を計算
    frame_indices = [int(i * total_frames / X) for i in range(X)]

    print(f"動画の総フレーム数: {total_frames}")
    print(f"{X}分割するフレーム位置: {frame_indices}")

    current_frame = 0
    saved_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if current_frame in frame_indices:
            filename = os.path.join(output_dir, f"frame_{saved_count + 1:03d}.jpg")
            cv2.imwrite(filename, frame)
            saved_count += 1
            print(f"{filename} を保存しました")

        current_frame += 1

        # 全て保存し終えたら終了
        if saved_count >= X:
            break

    cap.release()
    print("動画の分割が完了しました。")

                              # 分割数（例: 5分割）

split_video_into_frames(video_path, output_dir, X)
