# OECD Data API documentation
<!-- page: 1 -->
未分類 – 非機密

## OECDデータAPIドキュメント

## API インスタンス。

OECD は、SDMX 標準に基づく RESTful アプリケーション プログラミング インターフェイス (API) を通じて、OECD 諸国および一部の

## 非加盟国に対して OECD データへのプログラムによるアクセスを提供しています。

最終更新日: 2024年7月22日

## API を使用すると、開発者はさまざまな方法で OECD データを簡単に照会し、動的に更新される OECD データを使用する革新的なソフト

ウェア アプリケーションを作成できます。

## OECDをはじめとする国際機関は、統計データの記述と伝送のためのISO標準フォーマットを定義しており、これはインターネットを介し

## たユーザーや第三者との電子通信に使用できます。SDMX API標準は、JSON、XML、CSV形式をサポートしています。詳細は以下をご覧く

ださい。

## OECD データおよび API サービスは、OECD利用規約に同意することを条件として提供されます。

RESTful SDMX API標準には異なるバージョンがあり、OECDによって部分的にサポートされていることに注意してください。

## SDMX では、現象の測定 (例: 個体数カウント) は「観測」と呼ばれます。

観測データは「ディメンション」値（国と年など）の組み合わせによって記述され、一意に識別されます。「属性」を使用することで、さらに 有用な情報を追加できますが、統計データ（観測ステータスなど）の識別には役立ちません。同じ種類の観測データ（同じディメンション

## で識別可能）は、「データセット」にグループ化されます。SDMX‑ML および SDMX‑JSON 形式では、「シリーズ」と呼ばれる、ディメンシ

ョンのいずれかの値すべてについて観測データを中間的にグループ化することもできます。具体的には、利用可能なすべての期間の観測 データをグループ化したものを「時系列」と呼びます（たとえば、特定の国のすべての年の人口数）。同様に、任意のディメンションでグ ループ化できます。グループ化を行わない場合は、データセット内のすべての観測データのフラットなリストになります。

## 実際に返される観測値の構造メタデータは、SDMX‑JSONレスポンスメッセージに含まれています。可能な場合は、繰り返しを最小限に抑

えるために、各次元/属性を指定します。 1 データセット、ディメンション、属性に関する記述情報は「構造メタデータ」と呼ばれます。これは、構造クエリへのレスポンスとして返さ

## れるほか、データクエリに対するSDMX‑JSONレスポンスの「構造」部分にも含まれます。

## ©OECD 2024

詳細は下記をご覧ください。

## SDMX 規格とは何ですか?

## APIについて

利用規約

## SDMX‑JSON形式の特徴

Machine Translated by Google

<!-- page: 2 -->
未分類 – 非機密 例えば、セミコロン「;」は、クライアントのロケール（http Accept‑Language ヘッダーで指定）によって異なります。メッセージで使用される

## 区切り文字は、最初の列ヘッダーの固定用語「STRUCTURE」または「DATAFLOW」（角括弧で囲まれた用語で拡張される場合があります）

に続く文字を取得することで判別できます。

## SDMX‑JSONメッセージ内の観測値を一意に識別するために、メッセージの「構造」部分でシリーズレベルおよび観測レベルで定義されている

対応するディメンション値のインデックスが、シリーズまたは観測値のプロパティ名に連結されます。ここで、インデックスはメッセージの「構 造」部分で定義されているディメンションの事前定義された順序で並べられ、各インデックスはコロン文字で区切られます。 メッセージに含まれるデータの識別可能性を確保するため、ヘッダー行には列ヘッダーが含まれています。このヘッダー行に続く各行には、特 定の観測値、またはディメンションのサブセットの値に付加された1つ以上の属性値に関する情報（ディメンション値、観測値、属性値）が含ま れます。データベース同期を目的とした⾼度なクエリを使用することで、以前に削除されたデータに関する情報を取得することもできます。この ようなメッセージでは、ディメンション値が省略されている場合、1つの行が複数の観測値に関係することもあります。 シリーズおよび観測レベルの属性の具体的な値も、メッセージの「構造」部分で定義されているインデックスを通じて返されます。

## SDMX API バージョン 2

## ©OECD 20242

## データまたは参照メタデータ クエリを作成するには、次のパラメータを次の形式で URL に指定する必要があります: 代理店 ID、データフロー

## ID、データフロー バージョン、フィルタを使用する場合のディメンション値のリスト、およびオプションの追加パラメータ。

csvは「カンマ区切り値」を意味しますが、SDMX‑CSVではローカライズされたフィールド区切り文字を使用できます。 可能な限り最⾼のグループ化レベルで。データセットレベルとシリーズレベルで指定されたディメンションと属性は、データセット全体または シリーズ全体のすべての観測値に対して同じ値を持ちます。 最終更新日: 2024年7月22日

## この RFC 4180 互換形式は、フラット化されたテーブルでのデータの送信に限定されています。

## SDMX API バージョン 1

https://sdmx.oecd.org/public/rest/v2/data/dataflow/ <機関識別子>/<データフロー識別子>/<データフローバー ジョン>/<フィルター式>[?<オプションパラメータ>] https://sdmx.oecd.org/public/rest/data/<機関識別子>,<データフロー識別子>,<データフローバージョン>/<フィルター式>[? <オプションパラメータ>] データまたは参照メタデータをクエリするための構文

## SDMX‑CSV形式の特徴

Machine Translated by Google

<!-- page: 3 -->
未分類 – 非機密

## ‑参照メタデータは、SDMX API バージョン 2 を使用してのみクエリできます。

## ‑ SDMX のデータフローは、潜在的に大きなデータセットまたはデータ キューブのスライスまたは部分ビューです。

バージョン 例:

## SDMX API バージョン 2

- 「ABC+DEF..A」: 期間のない3つのディメンション。最初のディメンションの値として「ABC」と「DEF」、2

## 番目のディメンションに使用可能なすべての値、3番目のディメンションの値として「A」を使用します。

• バージョン1と同じですが、フィルタリングされていないコンテンツを取得するには、アスタリスク文字「*」を使用します。各 ディメンションは1つの値しか持てません。特定のディメンションについて、そのディメンションのすべての利用可能な値を 返す場合は、アスタリスク文字「*」を使用してディメンションをワイルドカードとして指定します。 識別子（コード化されていない場合）を使用して、応答に含めるディメンション値（期間を除く）のリストを指定します。フィ ルタリングされていないコンテンツを取得するには、「all」キーワードを使用します。ディメンションはドット（「.」）で区 切り、各ディメンションの値はプラス記号（「+」）で区切ります。特定のディメンションにディメンション値識別子が指定 されていない場合は、そのディメンションで使用可能なすべての値が返されます。 注: 最新のデータフローバージョンが使用されます。これにより多くの場合、より新しいデータを取得できますが、 新しいデータフローバージョンには下位互換性のない構造変更が含まれている可能性があることに注 意してください。 データフロー クエリされるデータフローの構造定義のバージョン。 'all': すべてのディメンションで使用可能なすべての値 識別子 クエリするデータフローの識別子。 3 最終更新日: 2024年7月22日 ディメンションとディメンション値のリストを取得するには、以下で説明する構造クエリを使用します。

- 'ABC.*.A': 期間のない3つのディメンション。最初のディメンションの値は 'ABC'、2番目のディメンションの値はす

## べての利用可能な値、3番目のディメンションの値は 'A'

## 空のままにした場合（SDMX APIバージョン1の場合）、または「+」に置き換えた場合（SDMX APIバージョン2の場合）、

## SDMX API バージョン 1

## ©OECD 2024

フィル ター式

- '*': すべてのディメンションで利用可能なすべての値

代理店 パラメータの使用 クライアントは、これを自己完結型の古典的な統計データセットとして理解できます。これは、機関識別子、データフロー識別 子、データフローバージョンの3つの組み合わせで完全に識別されます。 クエリの対象となるデータフローを所有する機関の識別子。 例: データフロ ー識別子 Machine Translated by Google

<!-- page: 4 -->
観測時の次元 結果を返す開始期間（その期間を含む）。指定しない場合は、先頭からデータが返されます。値 は、dateTime、グレゴリオ暦、またはSDMXレポート期間で表すことができます。 最終更新日: 2024年7月22日

- 'ge:2018+le:2024'

- '2015‑01‑01'

期間でデータをフィルタリングします。プラス記号「+」で区切られた2つの期間のリストと比較演 算子「ge」（以上）と「le」（以下）を、dateTime、グレゴリオ暦期間、またはSDMXレポート期間と 組み合わせて使用することで、開始期間と終了期間を設定できます。

- '2015‑A1'

- 'AllDimensions': データに期間ディメンションがない場合

開始期間

## SDMX API バージョン 2 のみ

オプションパラメータ

## SDMX API バージョン 1 のみ

- 'TIME_PERIOD: 観測値を時系列にグループ化する

例：

- '2015‑M01'

観測データを「series」にグループ化する目的で「AllDimensions」を指定するか、観測データをフラットに表 現するために「AllDimensions」を指定します。このパラメータが設定されていない場合、デフォルトの値の順 序は以下のとおりです。

## ©OECD 2024

## SDMX API バージョン 1 のみ

例:

- '2015'

- '2015‑S1'

- '2015‑01'

c[期間] 4 使用 観測レベルで提示される次元の識別子 終了期間

- '2015‑01‑01T00:00:00'

結果を返す終了期間（その期間を含む）。指定しない場合は、現在最後の期間までのデータが返 されます。使用可能な値の型については、 startPeriod を参照してください。

- 2015年第1四半期

一致する時系列ごとに返される観測値の最大値を指定する整数。このパラメータは、最新の観測

## 値から遡って数えます。このパラメータには正の整数を指定します。最後のNO観測

未分類 – 非機密 Machine Translated by Google

<!-- page: 5 -->
オプションパラメータ

- 'none': 通常の属性と参照属性の値

使用 詳細

## ©OECD 2024

このパラメータは、観測値を返すかどうかを指定します。

- 'none': 観測値は返されません

5

- 'NoData': 属性とデータを含むグループとシリーズを返します。

メタデータ属性は返されません SDMX‑CSV v2のみ（下記参照） 最終更新日: 2024年7月22日 属性

- 'all': 観測値が返される

「完全」: 注釈を含むすべてのデータとドキュメント (デフォルト)

- 'SeriesKeysOnly': シリーズキーを構成するシリーズ要素とディメンションのみ

- 'all': すべての通常属性（データ構造で定義）とすべての参照メタデータ属性（メタデータ

構造で定義）の値が返されます。

## SDMX API バージョン 2 のみ

可能なオプションは次のとおりです:

## SDMX API バージョン 1 のみ

この属性は、返される情報の量を指定します。可能な値は次のとおりです。 更新後

- 'msd': すべての参照メタデータ属性の値のみが

- 「2015‑12‑31T23:59:59.9999‑01:00」

このパラメータは、返される属性値を指定します。 対策

- 「データのみ」: 属性（つまりグループ）は除外されます

返された このパラメータを使用すると、返されるレスポンスには、その時点以降に挿入、更新、または削除さ れた観測データのみが含まれます。値は、クライアントのタイムゾーンを含むdateTimeで表現で きます。

## SDMX API バージョン 2 のみ

- 'dsd': すべての通常属性の値のみが返されます

頻繁にデータベースを同期するシナリオでは、転送されるデータの量を減らすためにこのパラメー タを使用することを強くお勧めします。 注釈、観察なし 可能なオプションは次のとおりです: • 未分類 – 非機密 Machine Translated by Google

<!-- page: 6 -->
未分類 – 非機密 https://sdmx.oecd.org/public/rest/v2/data/dataflow/OECD.ENV.EPI/DSD_ECH@EXT_DROUGHT/+/A

## SDMX API バージョン 2

## SDMX API バージョン 2 の詳細については、ここを参照してください。

## SDMX API バージョン 1:

## SDMX API バージョン 2:

## SDMX 構造 API バージョン 2 の詳細については、ここを参照してください。

観察とその通常の属性 US.A.ED_CROP_ANOM.*.*.*.*.*?c[TIME_PERIOD]=ge:2018+le:2021&attributes=dsd&measures=all& &updatedAfter=2015‑01‑01T00:00:00.000‑01:00

## ©OECD 2024

例: https://sdmx.oecd.org/public/rest/dataflow/ <機関識別子>/<データフロー識別子>/<バージョン番号>? references=all&detail=referencepartial

## SDMX 構造 API バージョン 1 の詳細については、ここを参照してください。

## SDMX API バージョン 1

## 更新後=2015‑01‑01T00:00:00.000‑01:00

## データ構造クエリを作成するには、データセット識別子と機関名を次の形式で URL に指定する必要があります。

## SDMX API バージョン 1 の詳細については、ここを参照してください。

最終更新日: 2024年7月22日 これらのパラメータの定義については、上記のデータクエリ構文のセクションを参照してください。 6 観察とその通常の属性 参照メタデータ属性 https://sdmx.oecd.org/public/rest/v2/data/dataflow/OECD.ENV.EPI/DSD_ECH@EXT_DROUGHT/1.0/ AFG.A.ED_CROP_IND.*.*.*.*.*?c[TIME_PERIOD]=ge:1981+le:2021&attributes=dsd&measures=all&u

## 更新日時=2015‑01‑01T00:00:00.000‑01:00

## D_CROP_IND.....?開始期間=1981&終了期間=2021&観測時の寸法=全寸法&更新

atedAfter=2015‑01‑01T00:00:00.000‑01:00 https://sdmx.oecd.org/public/rest/v2/data/dataflow/OECD.ENV.EPI/DSD_ECH@EXT_DROUGHT/1.0/ 識別子>/<バージョン番号>?references=all&detail=referencepartial https://sdmx.oecd.org/public/rest/v2/structure/dataflow/ <機関識別子>/<データフロー https://sdmx.oecd.org/public/rest/data/OECD.ENV.EPI,DSD_ECH@EXT_DROUGHT,1.0/AFG+BFA.AE AFG.A.ED_CROP_IND.*.*.*.*.*?c[TIME_PERIOD]=ge:1981+le:2021&attributes=msd&measures=なし 観測値とその通常の属性、最新のデータフローバージョン データ構造をクエリするための構文 Machine Translated by Google

<!-- page: 7 -->
## APIクエリビルダー

## 特定の応答形式を要求する: XML、JSON、または CSV

- SDMX‑CSV v1: 'csv'

- SDMX‑JSON v1: 'application/vnd.sdmx.data+json; 文字セット=utf‑8; バージョン=1.0'

## ©OECD 2024

- SDMX‑ML v3 構造固有のデータ形式（実験的）:

es=すべて&詳細=参照部分

- '; labels=both' は、レスポンス内のオブジェクトの名前に加えて、

- SDMX‑CSV v2: 'application/vnd.sdmx.data+csv; 文字セット=utf‑8; バージョン=2'

- SDMX‑CSV v1: 'application/vnd.sdmx.data+csv; 文字セット=utf‑8'

https://sdmx.oecd.org/public/rest/dataflow/OECD.ENV.EPI/DSD_ECH@EXT_DROUGHT/1.0?referenc

- SDMX‑ML v2.1 汎用データ形式（廃止）: 'genericdata'

- 添付ファイルとしてのSDMX‑CSV v1: 'csvfile'

## SDMX API バージョン 2:

## データおよび構造クエリは、OECD データエクスプローラーの開発者 API機能を使用して生成できます。

## SDMX‑CSV の場合は、オプションで設定を追加します。

- SDMX‑ML v2.1 汎用データ形式 (廃止): 'application/vnd.sdmx.genericdata+xml;

文字セット=utf‑8; バージョン=2.1' 'application/vnd.sdmx.structurespecificdata+xml; 文字セット=utf‑8; バージョン=2.1' /1.0?references=すべて&詳細=reference部分

## SDMX API バージョン 1:

例:

## あるいは、次の非 SDMX 標準の「フォーマット」URL パラメータを使用することもできます。

## 希望する応答形式 (SDMX‑ML、SDMX‑JSON、または SDMX‑CSV)、コンテンツ言語、および圧縮設定は通常、HTTP コンテンツ ネゴシエ

## ーションを通じて API に提供されます。

適切な代表者の選択

- SDMX‑ML v2.1構造固有のデータ形式：

7

- ピボット可能な期間形式を取得するには、「timeformat=normalized」を使用します

識別子。 最終更新日: 2024年7月22日

- SDMX‑ML v2.1 構造固有データ形式: 'structurespecificdata'

- SDMX‑JSON v2: 'application/vnd.sdmx.data+json; 文字セット=utf‑8; バージョン=2'

https://sdmx.oecd.org/public/rest/v2/structure/dataflow/OECD.ENV.EPI/DSD_ECH@EXT_DROUGHT 'application/vnd.sdmx.structurespecificdata+xml; 文字セット=utf‑8; バージョン=3.0'

- SDMX‑JSON v2: 'jsondata'

データおよび参照メタデータクエリの 'Accept' ヘッダーには、次のいずれかの値を使用します。 未分類 – 非機密 Machine Translated by Google

<!-- page: 8 -->
追加のドキュメントとサポート Accept‑Encoding: gzip、deflate、br 最終更新日: 2024年7月22日

## ‑ SDMX‑JSON仕様

注:参照メタデータは、SDMX‑JSON v2 および SDMX‑CSV v2 でのみサポートされます。 オプションで、設定 '; urn=true' を追加して、応答内に各構造の URN を含めます。 Accept‑Language: ru、en‑gb;q=0.8、en;q=0.7

## ‑ SDMX‑ML仕様

構造クエリの「Accept」ヘッダーには、次のいずれかの値を使用します。 'ラベル付きcsvファイル' 永続的な問題を報告したり、SDMX 標準に基づいて技術的な機能強化を提案したりするには、 https://gitlab.com/sis‑cc/.stat‑ suite/dotstatsuite‑core‑sdmxri‑nsi‑ws/‑/issues/ でチケットを作成してください。 標準的な圧縮方式は、適切な「Accept‑Encoding」ヘッダーを使用することで有効にできます。インターネット帯域幅の使用量を最小限 に抑え、ダウンロード速度を向上させるため、この機能を体系的に使用することを強くお勧めします。例： 次の非 SDMX 標準'formatVersion' URL パラメータを使用することもできます。

- SDMX‑ML v2.0: '2.0'

- SDMX‑ML v2.1: '2.1'

- SDMX‑JSON v1: 'application/vnd.sdmx.structure+json; 文字セット=utf‑8; バージョン=1.0'

## SDMX 標準の詳細については、次のリソースを参照してください。

‑ .Stat SDMX RESTful Web サービス チートシート

- オブジェクトの名前と識別子を含む添付ファイルとしての SDMX‑CSV v1:

## ©OECD 2024

- SDMX‑ML v2.1: 'application/vnd.sdmx.structure+xml; charset=utf‑8; version=2.1'

- SDMX‑ML v2.0およびv2.1：「構造」

「Accept‑Language」ヘッダーは、クライアントの言語設定を示すために使用されます。複数の値と、それぞれの重み付けが可能です。 例： これらのリソースは、クエリ構造、データ、追加情報 (参照メタデータ) のほか、エラー コードなどの詳細を提供します。 ただし、このドキュメントに記載されている構文のみがサポートされることが保証されていることに注意してください。 ‑ SDMX RESTful API仕様 サポートに関するご質問は、OECDdotStat@oecd.org までお問い合わせください。 8

- SDMX‑ML v2.0: 'application/vnd.sdmx.structure+xml; 文字セット=utf‑8; バージョン=2.0'

適切な言語の選択 データ圧縮を有効にする

## ‑ SDMX‑CSV仕様

## あるいは、次の非 SDMX 標準「フォーマット」URL パラメータを使用することもできます。

未分類 – 非機密 Machine Translated by Google

<!-- page: 9 -->
未分類 – 非機密 OECDデータエクスプローラー.Stat Suiteを搭載この API によってソースされます。 最終更新日: 2024年7月22日 こちらをご覧くださいクエリを従来の OECD.Stat API から新しい OECD Data API にアップグレードする方法についてのドキュメント。

## ©OECD 20249

## APIショーケース

従来のOECD.Stat APIからのクエリのアップグレード Machine Translated by Google


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
- 例1（軸を絞らず確認）
  - key: ............
- 例2（年次・日本・GDP関連トランザクションなどを指定する運用形）
  - key: A.JPN....{TRANSACTION}...Q._Z.{TABLE_IDENTIFIER}
- 実行例
  - /public/rest/data/OECD.SDD.NAD,DSD_NAMAIN10@DF_TABLE1_EXPENDITURE_VPVOB,2.0/{key}?startPeriod=1990&endPeriod=2024

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
- 例1（軸を絞らず確認）
  - key: .........
- 例2（月次・日本・生産量系MEASUREを指定）
  - key: JPN.M.{MEASURE}.{UNIT_MEASURE}.{ACTIVITY}.{ADJUSTMENT}.{TRANSFORMATION}.{TIME_HORIZ}.{METHODOLOGY}
- 実行例
  - /public/rest/data/OECD.SDD.STES,DSD_STES@DF_INDSERV,4.3/{key}?startPeriod=1990-01&endPeriod=2024-12

### トピック: 軸（DSD_STES）

#### 軸: REF_AREA
- 位置: 1
- 意味: 国・地域
- コード表: CL_AREA

#### 軸: FREQ
- 位置: 2
- 意味: 頻度（M, Q, A など）
- コード表: CL_FREQ

#### 軸: MEASURE
- 位置: 3
- 意味: 指標種別
- コード表: CL_MEASURE（agency=OECD.SDD.STES, version=1.2）
- 参考候補（metadata で確認できたもの）: PR, PRVM, LOCOBP, LOCOPE, LOCOPG, LOCOPM

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
