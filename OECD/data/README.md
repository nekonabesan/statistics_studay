# OECD 取得データ概要

このディレクトリには、OECD SDMX API から取得した経済統計データを CSV 形式で格納しています。

## 収録データサマリ

| データ項目 | ファイル名 | 行数 | 期間 | 国カバレッジ |
|---|---|---:|---|---|
| GDP（年次、PPP ベース） | gdp_annual.csv | 2,932 | 1970-2025 | 68 ヵ国（OECD 38/38） |
| 鉱工業生産指数 IIP（月次） | iip_monthly.csv | 139,375 | 1970-2025 | 50 ヵ国（OECD 36/38） |
| 鉱工業生産指数 IIP（四半期） | iip_quarterly.csv | 50,406 | 1970-2025 | 52 ヵ国（OECD 38/38） |
| 労働生産性（年次） | labor_productivity_annual.csv | 33,047 | 1970-2024 | 51 ヵ国（OECD 38/38） |
| 労働生産性・単位労働コスト（四半期） | labor_productivity_ulc_quarterly.csv | 58,852 | 1970-2025 | 37 ヵ国（OECD 34/38） |

備考:
- IIP は月次データのみだと AUS, NZL が欠落するため、四半期データを併置して OECD 全加盟国をカバーしています。
- 労働生産性・単位労働コスト（四半期）は CHL, COL, ISL, MEX が OECD 側データフローで未提供です。

## CSV ファイルの列構造（インターフェース定義）

### 1) gdp_annual.csv

| No | カラム名 | 型 | 必須 | 説明 |
|---:|---|---|---|---|
| 1 | FREQ | string | Yes | 頻度コード（A=年次） |
| 2 | REF_AREA | string | Yes | 国・地域コード（ISO3 準拠） |
| 3 | SECTOR | string | Yes | 制度部門コード |
| 4 | COUNTERPART_SECTOR | string | Yes | 相手部門コード |
| 5 | TRANSACTION | string | Yes | 取引項目コード（例: B1GQ） |
| 6 | INSTR_ASSET | string | Yes | 資産分類コード |
| 7 | ACTIVITY | string | Yes | 産業分類コード |
| 8 | EXPENDITURE | string | Yes | 支出分類コード |
| 9 | UNIT_MEASURE | string | Yes | 単位コード（例: USD_PPP） |
| 10 | PRICE_BASE | string | Yes | 価格基準コード（例: LR） |
| 11 | TRANSFORMATION | string | Yes | 変換コード（例: N） |
| 12 | TABLE_IDENTIFIER | string | Yes | 表識別子（例: T0102） |
| 13 | TIME_PERIOD | string | Yes | 観測時点（YYYY） |
| 14 | OBS_VALUE | number | Yes | 観測値 |

### 2) iip_monthly.csv

| No | カラム名 | 型 | 必須 | 説明 |
|---:|---|---|---|---|
| 1 | REF_AREA | string | Yes | 国・地域コード |
| 2 | FREQ | string | Yes | 頻度コード（M=月次） |
| 3 | MEASURE | string | Yes | 指標コード（例: PRVM） |
| 4 | UNIT_MEASURE | string | Yes | 単位コード（例: IX） |
| 5 | ACTIVITY | string | Yes | 産業分類コード（例: BTE, C, F） |
| 6 | ADJUSTMENT | string | Yes | 季節調整コード（例: N, Y） |
| 7 | TRANSFORMATION | string | Yes | 変換コード |
| 8 | TIME_HORIZ | string | Yes | 時間視点コード |
| 9 | METHODOLOGY | string | Yes | 算出方法コード |
| 10 | TIME_PERIOD | string | Yes | 観測時点（YYYY-MM） |
| 11 | OBS_VALUE | number | Yes | 観測値 |

### 3) iip_quarterly.csv

| No | カラム名 | 型 | 必須 | 説明 |
|---:|---|---|---|---|
| 1 | REF_AREA | string | Yes | 国・地域コード |
| 2 | FREQ | string | Yes | 頻度コード（Q=四半期） |
| 3 | MEASURE | string | Yes | 指標コード（例: PRVM） |
| 4 | UNIT_MEASURE | string | Yes | 単位コード（例: IX） |
| 5 | ACTIVITY | string | Yes | 産業分類コード |
| 6 | ADJUSTMENT | string | Yes | 季節調整コード |
| 7 | TRANSFORMATION | string | Yes | 変換コード |
| 8 | TIME_HORIZ | string | Yes | 時間視点コード |
| 9 | METHODOLOGY | string | Yes | 算出方法コード |
| 10 | TIME_PERIOD | string | Yes | 観測時点（YYYY-Qn） |
| 11 | OBS_VALUE | number | Yes | 観測値 |

### 4) labor_productivity_annual.csv

| No | カラム名 | 型 | 必須 | 説明 |
|---:|---|---|---|---|
| 1 | REF_AREA | string | Yes | 国・地域コード |
| 2 | FREQ | string | Yes | 頻度コード（A=年次） |
| 3 | MEASURE | string | Yes | 指標コード（例: GDPPOP） |
| 4 | ACTIVITY | string | Yes | 産業分類コード（例: _T） |
| 5 | UNIT_MEASURE | string | Yes | 単位コード（例: USD_PPP_PS, XDC_PS） |
| 6 | PRICE_BASE | string | Yes | 価格基準コード（例: V） |
| 7 | TRANSFORMATION | string | Yes | 変換コード（例: _Z） |
| 8 | ADJUSTMENT | string | Yes | 季節調整コード（例: _Z） |
| 9 | CONVERSION_TYPE | string | Yes | 変換方式コード（例: _Z） |
| 10 | TIME_PERIOD | string | Yes | 観測時点（YYYY） |
| 11 | OBS_VALUE | number | Yes | 観測値 |

### 5) labor_productivity_ulc_quarterly.csv

| No | カラム名 | 型 | 必須 | 説明 |
|---:|---|---|---|---|
| 1 | REF_AREA | string | Yes | 国・地域コード |
| 2 | FREQ | string | Yes | 頻度コード（Q=四半期） |
| 3 | MEASURE | string | Yes | 指標コード（例: GDPEMP, LCEMP, ULCE） |
| 4 | ACTIVITY | string | Yes | 産業分類コード（例: _T） |
| 5 | UNIT_MEASURE | string | Yes | 単位コード（例: PP） |
| 6 | PRICE_BASE | string | Yes | 価格基準コード（例: Q, V） |
| 7 | TRANSFORMATION | string | Yes | 変換コード（例: G1） |
| 8 | ADJUSTMENT | string | Yes | 季節調整コード（例: S） |
| 9 | CONVERSION_TYPE | string | Yes | 変換方式コード（例: NC） |
| 10 | TIME_PERIOD | string | Yes | 観測時点（YYYY-Qn） |
| 11 | OBS_VALUE | number | Yes | 観測値 |

## カラム毎のデータ説明（共通辞書）

| カラム名 | 主な格納値（例） | 説明 | 主な出現ファイル |
|---|---|---|---|
| FREQ | A, M, Q | 観測頻度。A=年次、M=月次、Q=四半期。 | gdp_annual.csv, iip_monthly.csv, iip_quarterly.csv, labor_productivity_annual.csv, labor_productivity_ulc_quarterly.csv |
| REF_AREA | JPN, USA, DEU など | 国・地域コード。主に ISO3 コード。 | 全ファイル |
| SECTOR | S1 | 制度部門。国民経済計算の部門軸。 | gdp_annual.csv |
| COUNTERPART_SECTOR | S1 | 相手部門。対称軸として使われる部門コード。 | gdp_annual.csv |
| TRANSACTION | B1GQ | 取引項目。B1GQ は GDP 関連コード。 | gdp_annual.csv |
| INSTR_ASSET | _Z | 資産分類。_Z は総計または該当なしを示すことが多い。 | gdp_annual.csv |
| ACTIVITY | _Z, _T, BTE, C, F など | 産業分類。データセットにより集計レベルが異なる。 | gdp_annual.csv, iip_monthly.csv, iip_quarterly.csv, labor_productivity_annual.csv, labor_productivity_ulc_quarterly.csv |
| EXPENDITURE | _Z | 支出分類。_Z は総計または該当なし。 | gdp_annual.csv |
| UNIT_MEASURE | USD_PPP, IX, PP, USD_PPP_PS, XDC_PS | 単位。PPP ドル、指数、ポイント等。 | 全ファイル |
| PRICE_BASE | LR, V, Q | 価格基準コード。連鎖価格、基準年価格など。 | gdp_annual.csv, labor_productivity_annual.csv, labor_productivity_ulc_quarterly.csv |
| TRANSFORMATION | N, _Z, G1 | 変換種別。水準、成長率など。 | gdp_annual.csv, iip_monthly.csv, iip_quarterly.csv, labor_productivity_annual.csv, labor_productivity_ulc_quarterly.csv |
| TABLE_IDENTIFIER | T0102 | 表 ID。同一データフロー内の表識別子。 | gdp_annual.csv |
| ADJUSTMENT | N, Y, S, _Z | 調整方法。季節調整の有無など。 | iip_monthly.csv, iip_quarterly.csv, labor_productivity_annual.csv, labor_productivity_ulc_quarterly.csv |
| TIME_HORIZ | _Z | 時間視点（期間解釈）コード。 | iip_monthly.csv, iip_quarterly.csv |
| METHODOLOGY | N | 算出方法コード。 | iip_monthly.csv, iip_quarterly.csv |
| CONVERSION_TYPE | NC, _Z | 換算方式コード。名目/実質や通貨換算ルールの補助軸。 | labor_productivity_annual.csv, labor_productivity_ulc_quarterly.csv |
| MEASURE | PRVM, GDPPOP, GDPEMP, LCEMP, ULCE | 指標コード。系列の意味を定義する主要軸。 | iip_monthly.csv, iip_quarterly.csv, labor_productivity_annual.csv, labor_productivity_ulc_quarterly.csv |
| TIME_PERIOD | 1970, 2025-06, 2025-Q4 | 観測時点。頻度に応じて YYYY / YYYY-MM / YYYY-Qn 形式。 | 全ファイル |
| OBS_VALUE | 1283313.343, 104.8557 など | 観測値（数値）。統計値本体。 | 全ファイル |

## 利用時の注意

- 各コード値の厳密な定義は OECD の codelist に依存します。
- 同じカラム名でもデータセットによって有効コード集合が異なる場合があります。
- 分析時は REF_AREA と TIME_PERIOD で整形し、必要に応じて FREQ をそろえて結合してください。
