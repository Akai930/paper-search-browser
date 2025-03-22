import requests

def search_papers_semantic(query: str, year_from: int = 2023, limit: int = 20) -> list[dict]:
    """
    指定されたクエリでSemantic Scholar APIから論文情報を取得し、辞書のリストを返す関数。

    Args:
        query (str): 検索クエリ
        year_from (int): 取得する論文の開始年（例: 2023）
        limit (int): 取得件数の上限（最大1000件）

    Returns:
        list[dict]: 論文情報の辞書のリスト
    """
    url = "http://api.semanticscholar.org/graph/v1/paper/search/"
    query_params = {
        "query": query,
        "fields": "title,abstract,url,publicationTypes",
        "year": f"{year_from}-",
        "limit": limit,
        "sort": "relevance",
    }

    response = requests.get(url, params=query_params)
    data = response.json()

    if "data" in data:
        return data["data"]
    else:
        print("why?")
        return []

# 使用例（この行は他ファイルで呼び出す場合の参考）
# results = search_papers('"human activity recognition sensor transformer"')
if __name__ == "__main__":
    query = "Time-Series Gene Expression Data Imputation"
    data = search_papers_semantic(query=query, year_from=2023, limit=20)
    print(data)
    print(len(data))