import json
from openai import OpenAI
import config

def get_structured_response(client: OpenAI, model: str, messages: list) -> dict:
    """
    lm studio jsonスキーマ固定出力
    指定したモデルとメッセージでチャット補完を実行し、
    返ってきたJSON形式のレスポンスを辞書型に変換して返す関数。
    
    Parameters:
        client (OpenAI): OpenAIクライアントインスタンス
        model (str): 使用するモデル名
        messages (list): チャットで送信するメッセージのリスト
    
    Returns:
        dict: 整形されたレスポンス（例: fields, labels など）
    
    Raises:
        ValueError: JSONのパースに失敗した場合
    """
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        # 必要に応じて追加パラメータを設定
    )
    

    # message.content全体を取得
    result = response.choices[0].message.content
    clean_lines = [line for line in result.splitlines() if not line.strip().startswith("```")]
    result = "\n".join(clean_lines)
    print(result)


    try:
        structured_data = json.loads(result)
    except json.JSONDecodeError as e:
        raise ValueError("レスポンスのJSON形式に誤りがあります") from e

    return structured_data

# 使用例
if __name__ == "__main__":
    client = OpenAI(base_url="http://192.168.11.26:1234/v1", api_key="lm-studio")
    MODEL = "my-model"
    #MODEL = "gemma-3-12b-it@q3_k_l"
    user_paper = '''"""感度解析を介した時系列遺伝子発現データ補完法の開発と創薬応用,承認薬を含む生物活性化合物は治療標的となるタンパク質に作用することで疾患治療のための作用を示す。しか し、それ以外のタンパク質に作用することで副作用のような期待していない作用を示す場合がある。したがって、 化合物の作用メカニズムを明らかにすることは、創薬における重要課題になっている。近年、オミクス情報に基づく、化合物の作用メカニズム予測が注目されている。例えば、化合物をヒト由来細胞に 添加して、一定時間後に遺伝子発現を観測した、化合物応答遺伝子発現データは、化合物の作用メカニズムの予測 に用いられている。しかしながら、このような遺伝子発現データは、コストや時間の制約により、特定の時間点で のみ観測され時系列で観測されていない。これによって、特定の時間点での解析を行うことはできるが、経時的に 解析を行うことができない。したがって、現状のデータから、化合物の経時的な影響を予測することは限界がある。そこで本研究では、細胞内システムに対して構築された数理モデルの感度解析を行い、得られた結果に基づき、 観測されている化合物応答遺伝子発現データから、時系列の遺伝子発現データを補完する新たな手法を開発することを目指した。"""'''
    messages = [
        {
            "role": "user",
            "content": config.experiment_message_without_paper + user_paper
        }
    ]
    
    data = get_structured_response(client, MODEL, messages)
    #print(data)
    print(data.keys())
    for item in data['fields']:
        print(f"{item['name']}:{item['score']}")
