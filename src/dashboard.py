import streamlit as st
import requests
import json

# ---------------------------------
# Streamlit Page Config
# ---------------------------------
st.set_page_config(
    page_title="LexiScan Auto",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ LexiScan Auto")
st.subheader("Legal Contract Entity Extractor")

st.markdown("---")

# ---------------------------------
# Input Section
# ---------------------------------
st.header("📄 Enter Contract Text")

contract_text = st.text_area(
    "Paste your contract text here:",
    height=200
)

# ---------------------------------
# Extract Button
# ---------------------------------
if st.button("🔍 Extract Entities"):

    if contract_text.strip() == "":
        st.warning("Please enter contract text.")
    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/extract-entities",
                json={"text": contract_text}
            )

            if response.status_code == 200:
                data = response.json()

                st.success("Extraction Successful ✅")

                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("📅 Dates")
                    st.write(data.get("dates", []))

                    st.subheader("💰 Amounts")
                    st.write(data.get("amounts", []))

                with col2:
                    st.subheader("🏢 Parties")
                    st.write(data.get("parties", []))

                    st.subheader("📜 Termination Clauses")
                    st.write(data.get("termination_clauses", []))

                st.markdown("---")
                st.subheader("📦 Raw JSON Output")
                st.code(json.dumps(data, indent=4), language="json")

            else:
                st.error("API Error")

        except Exception as e:
            st.error("Make sure FastAPI server is running.")