mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"kavithagowtham205@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml

echo "[theme]
base='light'" >> ~/.streamlit/config.toml