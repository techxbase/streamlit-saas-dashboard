
import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
import io, ssl, smtplib, yaml
from email.message import EmailMessage
from yaml.loader import SafeLoader

# Load config
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'], config['cookie']['name'],
    config['cookie']['key'], config['cookie']['expiry_days']
)

#name, auth_status, username = authenticator.login("Login", location="main")
# Perform login
authenticator.login(location="main")

#if auth_status:
if st.session_state["authentication_status"]:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.success(f"Welcome {name}!")

    st.title("SaaS Dashboard with Excel + Gmail Integration")

    # Upload Excel
    uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        st.subheader("Filter & View Data")

        # Filtering
        filters = {}
        for col in df.select_dtypes(include=["object"]).columns:
            options = df[col].dropna().unique().tolist()
            selected = st.multiselect(f"Filter {col}", options, default=options)
            filters[col] = selected
        for col, selected in filters.items():
            df = df[df[col].isin(selected)]

        st.dataframe(df)

        # Export filtered data
        def to_excel(dataframe):
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine="openpyxl") as writer:
                dataframe.to_excel(writer, index=False, sheet_name="Filtered")
            return output.getvalue()

        excel_data = to_excel(df)
        st.download_button("Download Filtered Data", data=excel_data,
            file_name="filtered_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

        st.markdown("---")
        st.subheader("Send Filtered Report via Gmail")

        email_from = st.text_input("Sender Gmail")
        email_pass = st.text_input("App Password", type="password")
        email_to = st.text_input("Recipient Email")
        subject = st.text_input("Subject", "Filtered Report")
        body = st.text_area("Email Body", "See attached filtered Excel report.")

        if st.button("Send Email"):
            msg = EmailMessage()
            msg["Subject"] = subject
            msg["From"] = email_from
            msg["To"] = email_to
            msg.set_content(body)
            msg.add_attachment(excel_data, maintype="application",
                               subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                               filename="filtered_report.xlsx")

            context = ssl.create_default_context()
            try:
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(email_from, email_pass)
                    server.send_message(msg)
                st.success("Email sent successfully!")
            except Exception as e:
                st.error(f"Error sending email: {e}")

    else:
        st.info("Please upload an Excel file.")

elif auth_status == False:
    st.error("Invalid credentials")
elif auth_status == None:
    st.warning("Please log in to continue.")
