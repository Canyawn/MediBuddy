import streamlit as st
from backend import generate_summary
import tempfile

st.set_page_config(page_title="🩺 MediBuddy", layout="centered")

# Optional: UI styling
st.markdown("""
    <style>
    .stApp { background-color: #f0f8ff;
            color : black }
    </style>
""", unsafe_allow_html=True)

st.title("🩺 MediBuddy ")
st.subheader("Medication Made Easy")

st.markdown("Upload a clinical note, discharge summary, or research paper in PDF format. The app will return a simple explanation.")

uploaded_file = st.file_uploader("📤 Upload PDF", type=["pdf"])

if st.button("📘 Generate Summary"):
    if not uploaded_file:
        st.warning("⚠ Please upload a medical report PDF.")
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            pdf_path = tmp_file.name

        with st.spinner("🧠 Summarizing..."):
            try:
                summary = generate_summary(pdf_path)
                st.text_area("📝 Patient-Friendly Summary", summary, height=300)

                # ✅ Download button
                st.download_button(
                    label="⬇ Download as txt",
                    data=summary,
                    file_name="summary.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"❌ Error: {e}")