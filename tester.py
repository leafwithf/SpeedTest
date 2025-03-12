import streamlit as st
import speedtest

def main ():
    st.header("SpeedTest", divider=True)
    st.write("Clique no botao abaixo para testar sua internet.")

    if st.button("Iniciar"):
        s = speedtest.Speedtest()
        s.get_best_server()
        download = s.download() / 1_000_000
        upload = s.upload() / 1_000_000
        st.write(f"Download: {download:.2f} Mbps")
        st.write(f"Upload: {upload:.2f} Mbps")  
        results = s.results.dict()

        max_speed = 100
        st.wrtie(f"Velocidade de download: {download_speed:.2f} Mbps")
        st.progress(min(download_speed, max_speed, 1.0))
    

        st.write(f"Velocidade de upload: {upload_speed:.2f} Mbps")
        st.progress(min(upload_speed, max_speed, 1.0))

        st.write(f"Ping: {results['ping']} ms")
   
main()