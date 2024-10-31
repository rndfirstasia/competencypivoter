import streamlit as st
import pandas as pd

st.write("#### Deksripsi Kompetensi Pivoter")
uploaded_file = st.file_uploader("", type=["xlsx", "xls"])

if uploaded_file:
    df_initial = pd.read_excel(uploaded_file)

    kompetensi = []
    definisi_kompetensi = []
    level = []
    description = []

    for i in range(len(df_initial)):
        current_kompetensi = df_initial["Kompetensi"].iloc[i]
        current_definisi = df_initial["Definisi Kompetensi"].iloc[i]

        if pd.notna(current_kompetensi): 
            kompetensi_name = current_kompetensi
            definisi_text = current_definisi

        for lvl in range(1, 7):
            if lvl in df_initial.columns and pd.notna(df_initial.at[i, lvl]):
                kompetensi.append(kompetensi_name)
                definisi_kompetensi.append(definisi_text)
                level.append(lvl)
                description.append(df_initial.at[i, lvl])

    df_expanded = pd.DataFrame({
        "Kompetensi": kompetensi,
        "Definisi Kompetensi": definisi_kompetensi,
        "Level": level,
        "Description": description
    })

    st.write("Hasil Pivot:")
    st.dataframe(df_expanded)
    
else:
    st.info("Masukkan file excel untuk memproses.")
