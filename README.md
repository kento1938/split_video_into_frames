# 📹 Video Splitter Python

このプロジェクトでは、Pythonを使用して動画を指定した数で分割し、各フレームを画像として保存するスクリプトを実行できます。

---

## 🔧 セットアップ手順

### 1. 仮想環境（venv）の作成と有効化

```bash
# 仮想環境を作成（venvは任意の名前）
python -m venv venv

# 仮想環境を有効化（Windowsの場合）
venv\Scripts\activate

# macOS / Linux の場合
source venv/bin/activate
```

### 2. 必要なライブラリをインストール

```bash
pip install opencv-python
```

---

📌 使用方法
このプロジェクトに含まれているPythonスクリプトは、1つの動画を指定した数で均等に分割し、**キーフレーム画像（JPG形式）**として保存するものです。

例えば、X = 40 と設定すれば、動画を40等分し、そのタイミングにあるフレームをそれぞれ画像として保存します。

# 使い方例
video_path = "allmov.mp4"      # 入力動画ファイルのパス
output_dir = "output_frames"   # 保存先フォルダ
X = 40                         # 何分割するか（画像の枚数）

---

## 📁 出力結果

実行後、`output_frames` フォルダに以下のような画像が出力されます：

```
output_frames/
├── frame_001.jpg
├── frame_002.jpg
├── ...
└── frame_040.jpg
```

---

## 📝 注意事項

* 動画ファイル（例: `allmov.mp4`）はプロジェクトディレクトリ直下に配置してください。
* 分割数 `X` を変えることで保存される画像の数を調整できます。
* 長い動画や高解像度動画では処理時間がかかることがあります。

---
