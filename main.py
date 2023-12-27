import streamlit as st
from PIL import Image
import base64
from stfunction import st_button, load_css

data = st.experimental_get_query_params()
st.set_page_config(layout='wide')
load_css()
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def setpage(img):
    page_bg = f'''
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 101%;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
    }}
    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}
    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    '''

    st.markdown(page_bg, unsafe_allow_html=True)


if data['df'][0] == 'contact':
    img = get_img_as_base64("backvs.png")
    setpage(img)
    st.write('')
    st.write('')
    st.markdown('</br>',unsafe_allow_html=True)
    st.markdown('</br>',unsafe_allow_html=True)
    st.markdown('</br>',unsafe_allow_html=True)
    st.markdown('</br>',unsafe_allow_html=True)
    col1, col2 = st.columns([1.7,1])
    with col2:
        st.write('#### Contact-Mail id: info@visualskill.in')
        # st.markdown('# ')
        st_button('newsletter', 'mailto:info@visualskill.in',
              'Click here to!', 22)
        st_button('linkedin', 'https://www.linkedin.com/in/visual-skill-0968082a6',
              'check out our!', 22)
        st_button('instagram', 'https://www.instagram.com/visualskill79',
              'Follow us on!', 22)
        st_button('youtube', 'https://www.youtube.com/@visualskill97',
              'Subscribe to our!', 22)
        st_button('github', 'https://github.com/visualskill',
              'For projects!', 22)
elif data['df'][0] == 'policy':
    st.write('Privacy & policy')
elif data['df'][0] == 'terms':
    st.write('Terms & Cond.')
elif data['df'][0] == 'faq':
    st.write('Frequently Asked Qeustions')