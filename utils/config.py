# 実験用のmessage　ユーザー論文あり
experiment_message = '''
以下は論文の情報です。  
"論文のタイトル、論文のアブストラクト"  
の順で与えられます。  

まずは論文をよく読んで、その論文が意味する核の部分をとらえてください。  
この論文について、以下の4つの情報を出力してください。出力は必ず指定されたJSON構造に従ってください。  
また、出力された情報は、その論文に関連した論文を効率的に検索するために使用されます。  
そのために有効だと思われるワードなどを意識して、出力結果を返してください。

---

1. **分野分類（fields）**  
　最も関連性が高いと思われる分野を「score: 1.0」としてください。  
　他の分野のスコアは、それに対して**どの程度関連しているか**を0.0〜1.0の範囲で設定してください。  
　2つ以上の分野を出力してください。  

選択可能な分野（fields）：  
人工知能, ロボティクス, 電子工学, 機械工学, 材料工学, 化学, 物理学, 生物学, 医学, 薬学, 環境科学, 農学, 数学, 地球科学, 哲学, 心理学, 社会学, 教育学, 法学, 政治学, 経済学, 経営学, 言語学, 文学, 歴史学, 文化人類学, メディア学, 芸術学, 土木工学, 交通工学, 建築工学

---

2. **研究対象（target）**  
　この論文が何を対象にしているかを、日本語と英語のペアで1つ出してください。  
　検索性を重視し、**抽象的すぎず具体的すぎない表現**を選んでください。  
　例：「人間行動認識」「創薬」「タンパク質」「グラフ構造」など。

---

3. **主な技術的アプローチ（approaches）**  
　この論文で研究対象にアプローチするために使われた**手法・要因・指標**を、以下の3カテゴリに分類してそれぞれ最低1つ以上、日本語・英語のペアで出力してください：  

- `"methods"`：分析技術やアルゴリズム、モデルなど（例：回帰分析、時系列解析、LDA、Transformerなど）  
- `"factors"`：分析における要因や変数（例：縦断勾配、大型車混入率、湿度、年齢など、なにを対象としているのか具体的に）  
- `"metrics"`：指標・評価軸（例：精度、F1スコア、飽和交通流率、語彙数など、この研究の最終的な目的を表すもの）  

出力順は、**関連性の強い順に並べてください**。  
また、**論文で独自に命名された新語（モデル名など）は含めないでください。**  
また、「機械学習」など抽象的な用語は避け、検索に役立つ具体的な語を優先してください。

---

4. **検索キーワード（search_keywords）**  
　上記の情報（fields、target、approaches）をもとに、論文検索（例：CiNii、Google Scholarなど）で有効な検索キーワードを考えてください。  
　日本語と英語それぞれで、**3つ以上のキーワードまたはフレーズ**を出力してください。  
　検索性向上のため、具体性と網羅性を意識してください。

---

### 出力形式（例）：
```json
{
  "fields": [
    { "name": "土木工学", "score": 1.0 },
    { "name": "交通工学", "score": 0.9 }
  ],
  "labels": {
    "target": { "ja": "飽和交通流率解析", "en": "Saturation Flow Rate Analysis" },
    "approaches": {
      "methods": [
        { "ja": "回帰分析", "en": "Regression Analysis" },
        { "ja": "実測データ収集", "en": "Field Data Collection" }
      ],
      "factors": [
        { "ja": "大型車混入率", "en": "Heavy Vehicle Penetration Rate" },
        { "ja": "縦断勾配", "en": "Vertical Gradient" }
      ],
      "metrics": [
        { "ja": "飽和交通流率", "en": "Saturation Flow Rate" },
        { "ja": "車頭時間", "en": "Headway Time" }
      ]
    },
    "search_keywords": {
      "ja": [
        "飽和交通流率解析",
        "土木工学 交通工学",
        "大型車混入率 縦断勾配"
      ],
      "en": [
        "Saturation Flow Rate Analysis",
        "Civil and Transportation Engineering",
        "Heavy Vehicle Penetration Vertical Gradient"
      ]
    }
  }
}
```

”””
多次元センサデータ処理のためのTransformerを用いた自己教師あり学習手法,センサ信号を入力として,人間行動認識を行う深層学習アルゴリズムを開発した. ここでは自然言語で用いられるTransformerに基づいた事前学習言語モデルを構築して, その事前学習言語モデルを用いて,下流タスクである人間行動認識タスクを解く形を追求する. VanillaのTransformerでもこれは可能であるが, ここでは, 線形層によるn次元数値データの埋め込み、ビン化処理、出力層の線形処理層という３つの要素を特色とするｎ次元数値処理トランスフォーマーを提案する。5種類のデータセットに対して、このモデルの効果を確かめた. VanillaのTransformerと比較して, 精度で10%～15%程度, 向上させることができた
”””'''
# json出力(検索クエリまで出力)するためのユーザー論文指定なしのもの
experiment_message_without_paper = """
以下は論文の情報です。  
"論文のタイトル、論文のアブストラクト"  
の順で与えられます。  

まずは論文をよく読んで、その論文が意味する核の部分をとらえてください。  
この論文について、以下の4つの情報を出力してください。出力は必ず指定されたJSON構造に従ってください。  
また、出力された情報は、その論文に関連した論文を効率的に検索するために使用されます。  
そのために有効だと思われるワードなどを意識して、出力結果を返してください。

---

1. **分野分類（fields）**  
　最も関連性が高いと思われる分野を「score: 1.0」としてください。  
　他の分野のスコアは、それに対して**どの程度関連しているか**を0.0〜1.0の範囲で設定してください。  
　2つ以上の分野を出力してください。  

選択可能な分野（fields）：  
人工知能, ロボティクス, 電子工学, 機械工学, 材料工学, 化学, 物理学, 生物学, 医学, 薬学, 環境科学, 農学, 数学, 地球科学, 哲学, 心理学, 社会学, 教育学, 法学, 政治学, 経済学, 経営学, 言語学, 文学, 歴史学, 文化人類学, メディア学, 芸術学, 土木工学, 交通工学, 建築工学

---

2. **研究対象（target）**  
　この論文が何を対象にしているかを、日本語と英語のペアで1つ出してください。  
　検索性を重視し、**抽象的すぎず具体的すぎない表現**を選んでください。  
　例：「人間行動認識」「創薬」「タンパク質」「グラフ構造」など。

---

3. **主な技術的アプローチ（approaches）**  
　この論文で研究対象にアプローチするために使われた**手法・要因・指標**を、以下の3カテゴリに分類してそれぞれ最低1つ以上、日本語・英語のペアで出力してください：  

- `"methods"`：分析技術やアルゴリズム、モデルなど（例：回帰分析、時系列解析、LDA、Transformerなど）  
- `"factors"`：分析における要因や変数（例：縦断勾配、大型車混入率、湿度、年齢など、なにを対象としているのか具体的に）  
- `"metrics"`：指標・評価軸（例：精度、F1スコア、飽和交通流率、語彙数など、この研究の最終的な目的を表すもの）  

出力順は、**関連性の強い順に並べてください**。  
また、**論文で独自に命名された新語（モデル名など）は含めないでください。**  
また、「機械学習」など抽象的な用語は避け、検索に役立つ具体的な語を優先してください。

---

4. **検索キーワード（search_keywords）**  
　上記の情報（fields、target、approaches）をもとに、論文検索（例：CiNii、Google Scholarなど）で有効な検索キーワードを考えてください。  
　日本語と英語それぞれで、**3つ以上のキーワードまたはフレーズ**を出力してください。  
　検索性向上のため、具体性と網羅性を意識してください。

---

### 出力形式（例）：
```json
{
  "fields": [
    { "name": "土木工学", "score": 1.0 },
    { "name": "交通工学", "score": 0.9 }
  ],
  "labels": {
    "target": { "ja": "飽和交通流率解析", "en": "Saturation Flow Rate Analysis" },
    "approaches": {
      "methods": [
        { "ja": "回帰分析", "en": "Regression Analysis" },
        { "ja": "実測データ収集", "en": "Field Data Collection" }
      ],
      "factors": [
        { "ja": "大型車混入率", "en": "Heavy Vehicle Penetration Rate" },
        { "ja": "縦断勾配", "en": "Vertical Gradient" }
      ],
      "metrics": [
        { "ja": "飽和交通流率", "en": "Saturation Flow Rate" },
        { "ja": "車頭時間", "en": "Headway Time" }
      ]
    },
    "search_keywords": {
      "ja": [
        "飽和交通流率解析",
        "土木工学 交通工学",
        "大型車混入率 縦断勾配"
      ],
      "en": [
        "Saturation Flow Rate Analysis",
        "Civil and Transportation Engineering",
        "Heavy Vehicle Penetration Vertical Gradient"
      ]
    }
  }
}
```"""
# ユーザー論文と検索クエリなしのもの。
experiment_message_without_paper_searchword = """
以下は論文の情報です。  
"論文のタイトル、論文のアブストラクト"  
の順で与えられます。  

まずは論文をよく読んで、その論文が意味する核の部分をとらえてください。
この論文について、以下の4つの情報を出力してください。出力は必ず指定されたJSON構造に従ってください。
また、出力された情報は、その論文に関連した論文を効率的に検索するために使用されます。
そのために有効だと思われるワードなどを意識して、出力結果を返してください。

---

1. **分野分類（fields）**  
　最も関連性が高いと思われる分野を「score: 1.0」としてください。  
　他の分野のスコアは、それに対して**どの程度関連しているか**を0.0〜1.0の範囲で設定してください。  
　2つ以上の分野を出力してください。  

選択可能な分野（fields）：  
人工知能, ロボティクス, 電子工学, 機械工学, 材料工学, 化学, 物理学, 生物学, 医学, 薬学, 環境科学, 農学, 数学, 地球科学, 哲学, 心理学, 社会学, 教育学, 法学, 政治学, 経済学, 経営学, 言語学, 文学, 歴史学, 文化人類学, メディア学, 芸術学, 土木工学, 交通工学, 建築工学

---

2. **研究対象（target）**  
　この論文が何を対象にしているかを、日本語と英語のペアで1つ出してください。  
　検索性を重視し、**抽象的すぎず具体的すぎない表現**を選んでください。  
　例：「人間行動認識」「創薬」「タンパク質」「グラフ構造」など。

---

3. **主な技術的アプローチ（approaches）**  
　この論文で研究対象にアプローチするために使われた**手法・要因・指標**を、以下の3カテゴリに分類してそれぞれ最低1つ以上、日本語・英語のペアで出力してください：  

- `"methods"`：分析技術やアルゴリズム、モデルなど（例：回帰分析、時系列解析、LDA、Transformerなど）  
- `"factors"`：分析における要因や変数（例：縦断勾配、大型車混入率、湿度、年齢など、なにを対象としているのか具体的に）  
- `"metrics"`：指標・評価軸（例：精度、F1スコア、飽和交通流率、語彙数など、この研究の最終的な目的を表すもの）  

出力順は、**関連性の強い順に並べてください**。  
また、**論文で独自に命名された新語（モデル名など）は含めないでください。**  
また、「機械学習」など抽象的な用語は避け、検索に役立つ具体的な語を優先してください。

---



### 出力形式（例）：
```json
{
  "fields": [
    { "name": "土木工学", "score": 1.0 },
    { "name": "交通工学", "score": 0.9 }
  ],
  "labels": {
    "target": { "ja": "飽和交通流率解析", "en": "Saturation Flow Rate Analysis" },
    "approaches": {
      "methods": [
        { "ja": "回帰分析", "en": "Regression Analysis" },
        { "ja": "実測データ収集", "en": "Field Data Collection" }
      ],
      "factors": [
        { "ja": "大型車混入率", "en": "Heavy Vehicle Penetration Rate" },
        { "ja": "縦断勾配", "en": "Vertical Gradient" }
      ],
      "metrics": [
        { "ja": "飽和交通流率", "en": "Saturation Flow Rate" },
        { "ja": "車頭時間", "en": "Headway Time" }
      ]
    },
  }
}
```"""

# 使う予定なし
unified_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "StructuredResearchMetadata",
    "type": "object",
    "properties": {
        "fields": {
            "type": "array",
            "minItems": 2,
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "enum": [
                            "人工知能",
                            "情報科学",
                            "ロボティクス",
                            "電子工学",
                            "機械工学",
                            "材料工学",
                            "化学",
                            "物理学",
                            "生物学",
                            "医学",
                            "薬学",
                            "環境科学",
                            "農学",
                            "数学",
                            "地球科学",
                            "哲学",
                            "心理学",
                            "社会学",
                            "教育学",
                            "法学",
                            "政治学",
                            "経済学",
                            "経営学",
                            "言語学",
                            "文学",
                            "歴史学",
                            "文化人類学",
                            "メディア学",
                            "芸術学",
                            "土木工学",
                            "交通工学",
                            "建築工学"
                        ]
                    },
                    "score": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 1
                    }
                },
                "required": ["name", "score"]
            }
        },
        "labels": {
            "type": "object",
            "properties": {
                "target": {
                    "type": "object",
                    "properties": {
                        "ja": {"type": "string"},
                        "en": {"type": "string"}
                    },
                    "required": ["ja", "en"]
                },
                "approaches": {
                    "type": "object",
                    "properties": {
                        "methods": {
                            "type": "array",
                            "minItems": 1,
                            "items": {
                                "type": "object",
                                "properties": {
                                    "ja": {"type": "string"},
                                    "en": {"type": "string"}
                                },
                                "required": ["ja", "en"]
                            }
                        },
                        "factors": {
                            "type": "array",
                            "minItems": 1,
                            "items": {
                                "type": "object",
                                "properties": {
                                    "ja": {"type": "string"},
                                    "en": {"type": "string"}
                                },
                                "required": ["ja", "en"]
                            }
                        },
                        "metrics": {
                            "type": "array",
                            "minItems": 1,
                            "items": {
                                "type": "object",
                                "properties": {
                                    "ja": {"type": "string"},
                                    "en": {"type": "string"}
                                },
                                "required": ["ja", "en"]
                            }
                        }
                    },
                    "required": ["methods", "factors", "metrics"]
                },
                "search_keywords": {
                    "type": "object",
                    "properties": {
                        "ja": {
                            "type": "array",
                            "minItems": 1,
                            "items": {"type": "string"}
                        },
                        "en": {
                            "type": "array",
                            "minItems": 1,
                            "items": {"type": "string"}
                        }
                    },
                    "required": ["ja", "en"]
                }
            },
            "required": ["target", "approaches", "search_keywords"]
        }
    },
    "required": ["fields", "labels"],
    "additionalProperties": False
}

# 使う予定なし
# 統一スキーマを tools に含める
experiment_tools = [
    {
        "type": "function",
        "function": {
            "name": "extract_paper_metadata",
            "description": "論文から分野分類、研究対象、技術的アプローチ、検索キーワードを抽出する",
            "parameters": unified_schema  # 統一スキーマをそのまま使用
        }
    }
]
