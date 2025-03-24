# ui/search_bar.py
import streamlit as st
from utils import paper_controller, llm_controller

def render_search_section():
    st.radio(
        "検索モード選択:",
        ("キーワード検索", "AI検索"),
        horizontal=True,
        key="search_mode"
    )
    
    st.caption(
        '※ キーワード検索 : 指定されたキーワードで検索を行います。<span style="color:coral; font-weight:bold;">（例：「genarative ai transformer」）</span>',
        unsafe_allow_html=True
    )
    st.caption(
        '※ AI検索 : 入力された文章から関連度の高い論文を自動で解析し検索します。<span style="color:coral; font-weight:bold;">（例：「～～に関する論文が知りたい」）</span>',
        unsafe_allow_html=True
    )
    st.caption(
        '※ AI検索 : 論文で論文を検索する場合は例のようにしてください。<span style="color:coral; font-weight:bold;">（例：「(論文タイトル),(論文アブストラクト)」）</span>',
        unsafe_allow_html=True
    )

    input_col, search_button = st.columns([8, 2])
    with input_col:
        st.text_area("入力:", value="", placeholder="ここに入力...", key="first_user_input")
    
    with search_button:
        if st.session_state["search_mode"] == "キーワード検索" and st.button("キーワード検索"):
            if st.session_state["search_engine"] == "semantic scholar":
                st.session_state["papers"] = paper_controller.semantic_controller(
                    query=st.session_state["first_user_input"],
                    year_range=st.session_state["year_range"],
                    limit=st.session_state["num_search_papers"]
                )
        
        if st.session_state["search_mode"] == "AI検索" and st.button("AI検索"):
            st.session_state["user_input_analysis"] = llm_controller.user_paper_controllar(
                st.session_state["first_user_input"]
            )
            # 結果確認用にフィールド情報を表示
            #st.write(st.session_state["user_input_analysis"].fields)
            if st.session_state["search_engine"] == "semantic scholar":
                st.session_state["papers"] = paper_controller.semantic_controller(
                    query=st.session_state["user_input_analysis"].search_keywords[0].en,
                    year_range=st.session_state["year_range"],
                    limit=st.session_state["num_search_papers"]
                )

def render_search_info_selection_section():
    with st.expander("オプション設定"):
        search_num_col, year_col, search_engine_col = st.columns([1, 1, 1])
        with search_num_col:
            st.slider("検索する論文数", min_value=1, max_value=50, value=10, key="num_search_papers")
        with year_col:
            st.slider("発行年の範囲", min_value=1970, max_value=2025, value=(2023, 2025), key="year_range")
        with search_engine_col:
            st.radio(
                "検索エンジン選択:",
                ("semantic scholar", "Google Scholar"),
                horizontal=True,
                key="search_engine"
            )
