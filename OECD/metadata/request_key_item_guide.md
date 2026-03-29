# OECD API リクエストキー組み立てガイド（データ項目別）

このファイルは、取得済み metadata（dataflow.xml / datastructure.xml / codelist.xml / contentconstraint.xml）をもとに、データ項目ごとのキー組み立て方法を整理したものです。

## 共通ルール

### トピック: エンドポイント形式
- データ取得URL: https://sdmx.oecd.org/public/rest/data/{flow_ref}/{key}
- 期間パラメータ: startPeriod, endPeriod

### トピック: flow_ref の作り方
- 形式: {agencyID},{dataflow_id},{version}
- 例: OECD.SDD.TPS,DSD_PDB@DF_PDB_ULC_Q,1.0

### トピック: key の作り方
- key は DSD の DimensionList の順序どおりに「.」区切りで指定する
- 未指定軸はワイルドカードとして空欄（例: .Q.......）を使う
- 利用可能コードは codelist.xml と contentconstraint.xml で確認する

---

## GDP（年次・実質、US$一定PPP）

### トピック: 対象データフロー
- Dataflow ID: DSD_NAMAIN10@DF_TABLE1_EXPENDITURE_VPVOB
- flow_ref: OECD.SDD.NAD,DSD_NAMAIN10@DF_TABLE1_EXPENDITURE_VPVOB,2.0
- DSD: DSD_NAMAIN10

### トピック: リクエストキー例
- 例1（FREQ=A, TRANSACTION=B1GQ のみ絞り込み ← 推奨）
  - key: A....B1GQ.......
  - 備考: PRICE_BASE=LR（連鎖参照年価格）・UNIT_MEASURE=USD_PPP・TRANSFORMATION=N はこのフローで固定値のため絞り不要
  - 実際の軸コード: SECTOR=S1, COUNTERPART_SECTOR=S1, TABLE_IDENTIFIER=T0102（固定）
- 例2（年次・国を絞る場合）
  - key: A.JPN+USA+DEU.....B1GQ.......
- 実行例
  - /public/rest/data/OECD.SDD.NAD,DSD_NAMAIN10@DF_TABLE1_EXPENDITURE_VPVOB,2.0/A....B1GQ.......
    ?startPeriod=1970&endPeriod=2025&detail=dataonly

### トピック: 軸（DSD_NAMAIN10）

#### 軸: FREQ
- 位置: 1
- 意味: 頻度（A=年次など）
- コード表: CL_FREQ

#### 軸: REF_AREA
- 位置: 2
- 意味: 国・地域
- コード表: CL_AREA

#### 軸: SECTOR
- 位置: 3
- 意味: 制度部門
- コード表: CL_SECTOR

#### 軸: COUNTERPART_SECTOR
- 位置: 4
- 意味: 相手部門
- コード表: CL_SECTOR

#### 軸: TRANSACTION
- 位置: 5
- 意味: 取引項目（GDP関連項目を含む）
- コード表: CL_TRANSACTION

#### 軸: INSTR_ASSET
- 位置: 6
- 意味: 金融資産・負債等
- コード表: CL_INSTR_ASSET

#### 軸: ACTIVITY
- 位置: 7
- 意味: 産業分類
- コード表: CL_ACTIVITY_ISIC4

#### 軸: EXPENDITURE
- 位置: 8
- 意味: 支出分類
- コード表: CL_COICOP_18

#### 軸: UNIT_MEASURE
- 位置: 9
- 意味: 単位
- コード表: CL_UNIT_MEASURE

#### 軸: PRICE_BASE
- 位置: 10
- 意味: 価格基準（実質/名目）
- コード表: CL_PRICES

#### 軸: TRANSFORMATION
- 位置: 11
- 意味: 変換（水準/成長率）
- コード表: CL_TRANSFORMATION

#### 軸: TABLE_IDENTIFIER
- 位置: 12
- 意味: 表識別子
- コード表: CL_TABLEID

#### 軸: TIME_PERIOD
- 位置: 13（時間軸）
- 意味: 年・四半期など
- 指定: クエリパラメータ startPeriod / endPeriod で絞る

### トピック: Response 構造（metadata から判断）
- SeriesKey: 上記の非時間軸（1〜12）
- ObsDimension: TIME_PERIOD
- ObsValue: OBS_VALUE（主観測値）
- 主要観測属性: REF_YEAR_PRICE, CONF_STATUS, DECIMALS, OBS_STATUS, UNIT_MULT, CURRENCY

---

## 鉱工業生産指数（IIP）

### トピック: 対象データフロー
- Dataflow ID: DSD_STES@DF_INDSERV
- flow_ref: OECD.SDD.STES,DSD_STES@DF_INDSERV,4.3
- DSD: DSD_STES

### トピック: リクエストキー例
- 例1（月次・MEASURE=PRVM ← IIP の推奨キー）
  - key: .M.PRVM......
  - 備考: MEASURE=PRVM（生産量指数）が月次 IIP の正式コード。PR は存在しない
  - UNIT_MEASURE=IX（指数）、TRANSFORMATION=_Z（固定）
- 例2（四半期・AUS・NZL など月次非報告国向け）
  - key: AUS+NZL.Q.PRVM......
- 実行例
  - /public/rest/data/OECD.SDD.STES,DSD_STES@DF_INDSERV,4.3/.M.PRVM......
    ?startPeriod=1970-01&endPeriod=2025-12&detail=dataonly
- 注意: AUS・NZL は月次 PRVM を報告せず、四半期 (.Q.PRVM......) で取得

### トピック: 軸（DSD_STES）

#### 軸: REF_AREA
- 位置: 1
- 意味: 国・地域
- コード表: CL_AREA

#### 軸: FREQ
- 位置: 2
- 意味: 頻度（M=月次, Q=四半期）
- コード表: CL_FREQ

#### 軸: MEASURE
- 位置: 3
- 意味: 指標種別
- コード表: CL_MEASURE（agency=OECD.SDD.STES, version=1.2）
- 月次 IIP で有効なコード: PRVM（生産量）, NODW（新規住宅注文）, TOCAPA（稼働率）, TOVM（生産高）, WSDW（卸売住宅）
- 旧ガイドの「PR」は DF_INDSERV では存在しないため削除

#### 軸: UNIT_MEASURE
- 位置: 4
- 意味: 単位
- コード表: CL_UNIT_MEASURE

#### 軸: ACTIVITY
- 位置: 5
- 意味: 産業分類
- コード表: CL_ACTIVITY_ISIC4

#### 軸: ADJUSTMENT
- 位置: 6
- 意味: 季節調整等
- コード表: CL_ADJUSTMENT

#### 軸: TRANSFORMATION
- 位置: 7
- 意味: 変換（指数水準/前月比など）
- コード表: CL_TRANSFORMATION

#### 軸: TIME_HORIZ
- 位置: 8
- 意味: 期間視点
- コード表: CL_TIME_HORIZ

#### 軸: METHODOLOGY
- 位置: 9
- 意味: 算出方法
- コード表: CL_METHODOLOGY

#### 軸: TIME_PERIOD
- 位置: 10（時間軸）
- 意味: 年月/四半期/年

### トピック: Response 構造（metadata から判断）
- SeriesKey: REF_AREA〜METHODOLOGY
- ObsDimension: TIME_PERIOD
- ObsValue: OBS_VALUE
- 主要観測属性: OBS_STATUS, UNIT_MULT, DECIMALS, BASE_PER

---

## 労働生産性（PDB）

### トピック: 対象データフロー
- Dataflow ID: DSD_PDB@DF_PDB_LV
- flow_ref: OECD.SDD.TPS,DSD_PDB@DF_PDB_LV,1.0
- DSD: DSD_PDB

### トピック: リクエストキー例
- 例1（全軸ワイルドカード）
  - key: .........
- 例2（G7・年次・就業者1人あたりGDP・USD PPP）
  - key: CAN+FRA+DEU+ITA+JPN+GBR+USA.A.GDPEMP._T.USD_PPP_PS.Q._Z._Z
- 実行例
  - /public/rest/data/OECD.SDD.TPS,DSD_PDB@DF_PDB_LV,1.0/{key}?startPeriod=1990&endPeriod=2024

### トピック: 軸（DSD_PDB）

#### 軸: REF_AREA
- 位置: 1
- 意味: 国・地域
- コード表: CL_AREA

#### 軸: FREQ
- 位置: 2
- 意味: 頻度
- コード表: CL_FREQ

#### 軸: MEASURE
- 位置: 3
- 意味: 指標（GDPEMP など）
- コード表: CL_MEASURE_PROD

#### 軸: ACTIVITY
- 位置: 4
- 意味: 産業分類（_T など）
- コード表: CL_ACTIVITY_ISIC4

#### 軸: UNIT_MEASURE
- 位置: 5
- 意味: 単位（USD_PPP_PS など）
- コード表: CL_UNIT_MEASURE

#### 軸: PRICE_BASE
- 位置: 6
- 意味: 価格基準（Q, V など）
- コード表: CL_PRICES

#### 軸: TRANSFORMATION
- 位置: 7
- 意味: 変換（水準/成長率）
- コード表: CL_TRANSFORMATION

#### 軸: ASSET_CODE
- 位置: 8
- 意味: 資産コード（多くは _Z）
- コード表: CL_ASSET_CODE

#### 軸: CONVERSION_TYPE
- 位置: 9
- 意味: 変換方式（NC など）
- コード表: CL_CONVERSION_TYPE

#### 軸: TIME_PERIOD
- 位置: 10（時間軸）
- 意味: 年・四半期

### トピック: Response 構造（metadata から判断）
- SeriesKey: REF_AREA〜CONVERSION_TYPE
- ObsDimension: TIME_PERIOD
- ObsValue: OBS_VALUE
- 主要観測属性: OBS_STATUS, UNIT_MULT, BASE_PER, DECIMALS

---

## 労働生産性・単位労働コスト（四半期）

### トピック: 対象データフロー
- Dataflow ID: DSD_PDB@DF_PDB_ULC_Q
- flow_ref: OECD.SDD.TPS,DSD_PDB@DF_PDB_ULC_Q,1.0
- DSD: DSD_PDB（軸構造は上記と同じ）

### トピック: リクエストキー例
- 例（全地域・四半期・全系列）
  - key: .Q.......
- 例（労働生産性指数・季節調整済み）
  - key: .Q.GDPEMP._T.IX.Q._Z.S.NC
- 実行例
  - /public/rest/data/OECD.SDD.TPS,DSD_PDB@DF_PDB_ULC_Q,1.0/{key}?startPeriod=1990-Q1&endPeriod=2024-Q4

### トピック: Response 構造（metadata から判断）
- SeriesKey: REF_AREA, FREQ, MEASURE, ACTIVITY, UNIT_MEASURE, PRICE_BASE, TRANSFORMATION, ASSET_CODE, CONVERSION_TYPE
- ObsDimension: TIME_PERIOD（四半期）
- ObsValue: OBS_VALUE
- 主要観測属性: OBS_STATUS, UNIT_MULT, BASE_PER, DECIMALS

---

## 制約確認（必須）

### トピック: なぜ制約確認が必要か
- DSD で定義される軸コードの全組合せが、実データで有効とは限らないため
- 実際の有効組合せは contentconstraint で制限される

### トピック: 参照ファイル
- metadata/contentconstraint.xml
- metadata/contentconstraint_focus.md
- metadata/request_parameter_structure.md

### トピック: 実務手順
1. dataflow.xml で対象 Dataflow を特定
2. datastructure.xml で軸順序を確認
3. codelist.xml で候補コードを確認
4. contentconstraint.xml で有効な組合せを確認
5. key を組み立てて startPeriod / endPeriod を付けて実行
