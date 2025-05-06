import streamlit as st
from nebula import ask_question

CHAIN_IDS = {
    "Ethereum Mainnet": "1",
    "Sepolia (Testnet)": "11155111",
    "Goerli (Testnet)": "5",
    "Polygon Mainnet": "137",
    "Mumbai (Polygon Testnet)": "80001",
    "Arbitrum One": "42161",
    "Arbitrum Goerli (Testnet)": "421613",
    "Optimism": "10",
    "Optimism Goerli (Testnet)": "420",
    "Binance Smart Chain": "56",
    "BSC Testnet": "97",
    "Avalanche C-Chain": "43114",
    "Avalanche Fuji (Testnet)": "43113",
    "Base": "8453",
    "Base Goerli (Testnet)": "84531",
    "Fantom Opera": "250",
    "Fantom Testnet": "4002",
    "Celo Mainnet": "42220",
    "Celo Alfajores (Testnet)": "44787"
}

st.set_page_config(page_title="Blockchain Explorer AI", page_icon="🧠")
st.title("🔍 Smart Blockchain EXplorer")

st.sidebar.header("🔗 Parámetros de Consulta")
network_name = st.sidebar.selectbox("Selecciona una red", list(CHAIN_IDS.keys()))
chain_id = CHAIN_IDS[network_name]
contract_address = st.sidebar.text_input("Dirección del contrato (0x...)")
modo_corto = st.sidebar.checkbox("🧢 Respuesta breve (<200 caracteres)", value=False)

user_input = st.text_input("💬 ¿Qué quieres preguntarle al contrato?", "")

if st.button("Enviar") and user_input:
    with st.spinner("🔍 Consultando la blockchain..."):
        try:
            # Incluir el contrato y la red en el prompt si se indica
            if contract_address:
                prompt = f"{user_input} (analiza el contrato {contract_address} en la red {network_name})"
            else:
                prompt = user_input

            response = ask_question(prompt, chain_id, contract_address or None, modo_corto)
            st.markdown("### 🤖 Respuesta")
            st.markdown(response)
        except Exception as e:
            st.error(f"❌ Error: {e}")
