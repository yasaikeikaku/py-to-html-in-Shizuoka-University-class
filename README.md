# Python to HTML Converter

このツールは、Python コードを HTML 形式に変換し、シンタックスハイライトを適用します。Pygments を使用して美しい HTML 出力を生成します。

## 特徴

- Python コードのシンタックスハイライト付き HTML 変換
- コマンドラインから簡単に使用可能
- フルパス、相対パス、ファイル名のみの指定に対応
- 出力ファイル名の指定が可能
- 自動出力フォルダ作成

## インストール

1. スクリプトを `~/bin/pytohtml` にコピー
2. 実行権限を付与: `chmod +x ~/bin/pytohtml`
3. PATH に `~/bin` を追加（`~/.bashrc` に `export PATH="$HOME/bin:$PATH"` を追加）

## 使用方法

```bash
pytohtml <input.py> [output.html]
```

### 引数

- `<input.py>`: 変換する Python ファイル（フルパス、相対パス、ファイル名）
- `[output.html]`: 出力ファイル名（オプション、デフォルトは入力ファイル名 + `.html`）

### 例

```bash
# 基本的な使用（デフォルト出力名）
pytohtml script.py

# カスタム出力名
pytohtml script.py my_output.html

# フルパス指定
pytohtml /home/yuki/project/main.py

# 相対パス指定
pytohtml ../other/script.py custom.html

# カレントディレクトリのファイル
cd /path/to/project && pytohtml main.py
```

出力ファイルは `~/pytohtml_output/` フォルダに保存されます。

## 依存関係

- Python 3.x
- Pygments (`pip install pygments`)

## エラーハンドリング

- 入力ファイルが存在しない場合: エラーメッセージを表示して終了
- 出力フォルダが存在しない場合: 自動作成

## 出力例

変換された HTML はブラウザで開くと、以下のように表示されます：

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        /* Pygments CSS styles */
    </style>
</head>
<body>
    <div class="highlight">
        <pre><span></span><span class="k">def</span> <span class="nf">hello</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Hello, World!"</span><span class="p">)</span>
</pre>
    </div>
</body>
</html>
```

## ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。
