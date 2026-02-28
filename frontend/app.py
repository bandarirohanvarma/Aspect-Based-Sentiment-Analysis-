import streamlit as st
import requests

st.set_page_config(page_title="Retail ABSA", page_icon="🛍️", layout="centered")

st.title("🛍️ Aspect-Based Sentiment Analysis")
st.markdown("Analyze reviews at aspect level.")

st.divider()

review = st.text_area("Enter Review", height=150)

if st.button("Analyze Review"):

    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        try:
            response = requests.post(
                "https://aspect-based-sentiment-analysis-0cm1.onrender.com",
                json={"text": review}
            )

            data = response.json()

            st.subheader("Analysis Result")

            for item in data["results"]:
                aspect = item["aspect"]
                sentiment = item["sentiment"]["label"]
                score = item["sentiment"]["score"]

                col1, col2 = st.columns([2,1])

                with col1:
                    st.write(f"**Aspect:** {aspect}")

                with col2:
                    if sentiment == "POSITIVE":
                        st.success(f"{sentiment} ({score})")
                    else:
                        st.error(f"{sentiment} ({score})")

        except:
            st.error("Backend not running. Please start FastAPI server.")
