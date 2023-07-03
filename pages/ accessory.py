import streamlit as st
import pandas as pd
import numpy as np

df_ksr_buki = pd.read_csv('./sobi/ksr装飾-表1.csv')
df_ssr_buki = pd.read_csv('./sobi/ssr装飾-表1.csv')
df_category = pd.read_csv('./sobi/アビリティカテゴリ分類-表1.csv')

df = pd.concat([df_ksr_buki,df_ssr_buki])

output = df.copy()



submit_btn1 = st.radio("レアリティ", ("絞る", "絞らない"), index=1)

rare_filter = None
rare_list = []

if submit_btn1 == "絞る":
    # check box
    col = st.columns(2)
    ksr = col[0].checkbox(label='KSR')
    ssr = col[1].checkbox(label='SSR')

    if ksr:
        rare_list.append('KSR')
    if ssr:
        rare_list.append('SSR')
    # 条件が選択されている場合だけ、outputを条件に合致するレコードだけのDFに置き換える
    if ksr or ssr:
        rare_filter = df['レアリティ'].isin(rare_list)
        output = df[rare_filter]
submit_btn2 = st.radio("ステータス", ("絞る", "絞らない"), index=1)

status = True
if submit_btn2 == "絞る":
    # check box
    col = st.columns(6)
    hp = col[0].checkbox(label='体力')

    attack = col[1].checkbox(label='攻撃力')

    defense = col[2].checkbox(label='防御力')
    
    critical = col[3].checkbox(label='会心率')

    avoidance = col[4].checkbox(label='回避率')

    hit = col[5].checkbox(label='命中率')

    if hp:
        status = status & (output['体力'] > 0)
    
    if attack:
        status = status & (output['攻撃力'] > 0)
    
    if defense:
        status = status & (output['防御力'] > 0)

    if critical:
        status = status & (output['会心率'] > 0)

    if avoidance:
        status = status & (output['回避率'] > 0)

    if hit:
        status = status & (output['命中率'] > 0)
    # 条件が選択されている場合だけ、outputを条件に合致するレコードだけのDFに置き換える
    if hp or attack or defense or critical or avoidance or hit:
        output = output[status]

submit_btn3 = st.radio("アビリティ", ("絞る", "絞らない"), index=1)
#アビリティフィルタ
# アビリティ名のリストを作成
ability_name_list = df_category['アビリティカテゴリ分類'].unique()
# Nanを削除
ability_name_list = ability_name_list[1:]

if submit_btn3 == "絞る":
    #複数選択
    type_color3 = st.multiselect('アビリティ種類',(ability_name_list))
    if type_color3:
        # 選択されたアビリティが含まれている行を抽出
        ability_filter = output['アビリティカテゴリ'].apply(lambda x: any(ab in x for ab in type_color3) if pd.notnull(x) else False)

        output = output[ability_filter]

    
# outputが空でないならソートを実行
if not output.empty:
    output = output.sort_values('装備番号')
    output = output.reset_index(drop=True)  # インデックスをリセット
    output = output.drop(columns =['装備番号','レアリティ','アビリティカテゴリ'])

# 装備名のカラムを含める
# output_columns = output.columns.tolist()
# output = output[output_columns]

st.write(output)
