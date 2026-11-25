# School Calendar

GitHub Web版対応・フォルダなし構成。ZIPを解凍し、全ファイルをリポジトリ直下にアップロード。Settings → Pages → Deploy from a branch → main → / (root) → Save。

購読URLは公開サイトの calendar.ics。更新時は events.json と calendar.ics の両方を更新する。Python 3 が利用できる場合は python generate.py でICSを再生成可能。GitHub Actionsは不要。

非公式。春休みは推定。公開前に学校の最新情報と照合すること。
https://miyazk-dev.github.io/school-calendar/
