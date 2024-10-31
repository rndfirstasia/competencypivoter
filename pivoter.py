import streamlit as st
import pandas as pd

st.write("#### Deksripsi Kompetensi Pivoter")
uploaded_file = st.file_uploader("", type=["xlsx", "xls"])

if uploaded_file:
    # Step 1: Load the Excel file
    df_initial = pd.read_excel(uploaded_file)

    # Step 2: Expand the DataFrame to handle variable levels
    kompetensi = []
    definisi_kompetensi = []
    level = []
    description = []

    for i in range(len(df_initial)):
        current_kompetensi = df_initial["Kompetensi"].iloc[i]
        current_definisi = df_initial["Definisi Kompetensi"].iloc[i]

        if pd.notna(current_kompetensi):  # New competency section
            kompetensi_name = current_kompetensi
            definisi_text = current_definisi

        # Loop through each level (1-6) and add if data is present
        for lvl in range(1, 7):
            # Check if the level column exists in the DataFrame and has a non-NaN value
            if lvl in df_initial.columns and pd.notna(df_initial.at[i, lvl]):
                kompetensi.append(kompetensi_name)
                definisi_kompetensi.append(definisi_text)
                level.append(lvl)
                description.append(df_initial.at[i, lvl])

    # Create the expanded DataFrame
    df_expanded = pd.DataFrame({
        "Kompetensi": kompetensi,
        "Definisi Kompetensi": definisi_kompetensi,
        "Level": level,
        "Description": description
    })

    # Display the expanded DataFrame
    st.write("Expanded Competency Table:")
    st.dataframe(df_expanded)
    
else:
    st.info("Masukkan file excel untuk memproses.")