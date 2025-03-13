import streamlit as st
import speedtest

def main():
    st.header("SpeedTest", divider=True)
    st.write("Clique no botão abaixo para testar sua internet.")

    if st.button("Iniciar"):
        s = speedtest.Speedtest()
        s.get_best_server()

        download = s.download() / 1_000_000  # Convertendo para Mbps
        upload = s.upload() / 1_000_000      # Convertendo para Mbps
        results = s.results.dict()

        max_speed = 100  # Ajuste conforme necessário

        st.write(f"Velocidade de Download: {download:.2f} Mbps")
        st.progress(min(download / max_speed, 1.0))  # Normalizando para barra de progresso

        st.write(f"Velocidade de Upload: {upload:.2f} Mbps")
        st.progress(min(upload / max_speed, 1.0))  # Normalizando para barra de progresso

        st.write(f"Ping: {results['ping']} ms")

# Rodar a função principal
if __name__ == "__main__":
    main()

