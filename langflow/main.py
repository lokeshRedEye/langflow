import requests
import streamlit as st


BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "59a5eeb8-4f77-4369-b3b0-fc763acbabe7"
FLOW_ID = "0c856cbb-29ac-4677-9cb7-08ed3b502887"
APPLICATION_TOKEN = "AstraCS:ojmKsNGRuZkUQhftqgvvBean:aae537b5b4f52db27904e546f8740c2404a9c49347a6183afb8c23f4be12bbf1"
ENDPOINT = "customer" # The endpoint name of the flow


def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }

    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    st.title("Chat Interface")
    
    message = st.text_area("Message", placeholder="Ask something...")
    
    if st.button("Run Flow"):
        if not message.strip():
            st.error("Please enter a message")
            return
    
        try:
            with st.spinner("Running flow..."):
                response = run_flow(message)
            
            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(str(e))

if __name__ == "__main__":
    main()