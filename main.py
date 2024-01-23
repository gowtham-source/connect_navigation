import streamlit as st
from PIL import Image
import base64
from stfunction import st_button, load_css
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(layout='wide')

data = st.experimental_get_query_params()
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


try:
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
        if streamlit_js_eval(js_expressions='screen.width', key = 'SCR')<700:
            st.image('top_banner.png',width=400)
        else:
            st.image('top_banner.png',width=1350)
        st.markdown('''# _**Privacy Policy for VisualSkill**_

**Last updated:** Jan 2024,

"Welcome to VisualSkill! This Privacy Policy is designed to help you understand how we collect, use, disclose, and safeguard your personal information when you use our website."

### 1. Information We Collect

We may collect the following types of information:

- **Personal Information:** When you register on VisualSkill, we may collect personal information such as your name, email address, and other relevant details.

- **Usage Data:** We may collect information about how you interact with our website, including the pages you visit, the duration of your visit, and other similar usage data.

- **Device Information:** We may collect information about the device you use to access VisualSkill, including the device type, operating system, and browser type.

### 2. How We Use Your Information

We use the collected information for various purposes, including:

- **Providing Intern Opportunities:** Your personal information may be used to match you with relevant internship opportunities based on your qualifications and preferences.

- **Improving User Experience:** We analyze usage data to enhance and optimize our website's performance, content, and features.

- **Communications:** We may use your email address to send you important updates, newsletters, and information about internship opportunities.

### 3. Data Security

VisualSkill is committed to protecting your information. We implement industry-standard security measures to prevent unauthorized access, disclosure, alteration, and destruction of your personal information.

### 4. Third-Party Disclosure

We do not sell, trade, or otherwise transfer your personal information to third parties without your consent. However, we may share information with trusted third parties who assist us in operating our website, conducting our business, or servicing you.

### 5. Cookies and Similar Technologies

VisualSkill uses cookies and similar technologies to enhance your browsing experience. You can manage your cookie preferences through your browser settings.

### 6. Your Choices

You have the right to update, correct, or delete your personal information. You may also choose to opt-out of certain communications. Contact us at [info@visualskill.com](mailto:info@visualskill.com) for assistance.

### 7. Changes to this Privacy Policy

VisualSkill may update this Privacy Policy periodically. We will notify you of any changes by posting the new policy on this page.

### 8. Contact Us

If you have any questions or concerns about this Privacy Policy, please contact us at [info@visualskill.com](mailto:info@visualskill.com).

By using VisualSkill, you agree to the terms outlined in this Privacy Policy.

Thank you for choosing **VisualSkill** for your internship opportunities!
''')
    elif data['df'][0] == 'terms':
        if streamlit_js_eval(js_expressions='screen.width', key = 'SCR')<700:
            st.image('top_banner.png',width=400)
        else:
            st.image('top_banner.png',width=1350)
        st.markdown('''# **Terms of Use**

## 1. Terms

By accessing this Company, you are agreeing to be bound by these Terms of Use, all applicable laws and regulations, and agree that you are responsible for compliance with any applicable local laws. If you do not agree with any of these terms, you are prohibited from using or accessing this site. The materials contained in this Company are protected by applicable copyright and trademark law.

## 2. Use License

Permission is granted to temporarily download one copy of any downloadable materials on the Company’s website for personal, non-commercial transitory viewing only. This is the grant of a license, not a transfer of title, and under this license you may not:

- modify or copy the materials;
- use the materials for any commercial purpose, or for any public display (commercial or non-commercial);
- attempt to decompile or reverse engineer any software contained on the Company’s web site;
- remove any copyright or other proprietary notations from the materials; or
- transfer the materials to another person or 'mirror' the materials on any other server.

This license shall automatically terminate if you violate any of these restrictions and may be terminated by Company at any time. Upon terminating your viewing of these materials or upon the termination of this license, you must destroy any downloaded materials in your possession whether in electronic or printed format.

## 3. Disclaimer

The materials on the Company’s website are provided 'as is'. The Company makes no warranties, expressed or implied, and hereby disclaims and negates all other warranties, including without limitation, implied warranties or conditions of merchantability, fitness for a particular purpose, or non-infringement of intellectual property or other violation of rights. Further, the Company does not warrant or make any representations concerning the accuracy, likely results, or reliability of the use of the materials on its website or otherwise relating to such materials or on any sites linked to this site.

## 4. Limitations

In no event shall the Company be liable for any damages (including, without limitation, damages for loss of data or profit, or due to business interruption) arising out of the use or inability to use the materials on the Company’s website, even if the Company or an authorized of the Company has been notified orally or in writing of the possibility of such damage. Because some jurisdictions do not allow limitations on implied warranties, or limitations of liability for consequential or incidental damages, these limitations may not apply to you.

## 5. Revisions and Errata

The materials appearing on the Company’s website may include technical, typographical, or photographic errors. The Company does not warrant that any of the materials on its web site are accurate, complete, or current. The Company may make changes to the materials contained on its web site at any time without notice. The Company does not, however, make any commitment to update the materials.

## 6. Links

The Company has not reviewed all of the sites linked to its website and is not responsible for the contents of any such linked site. The inclusion of any link does not imply endorsement by the Company of the site. Use of any such linked website is at the user's own risk.

## 7. Site Terms of Use Modifications

The Company may revise these Terms of Use for its website at any time without notice. By using this website, you are agreeing to be bound by the then-current version of these Terms of Use.

## 8. Governing Law

Any claim relating to the Company’s website shall be governed by the laws of the Company Owner’s home jurisdiction without regard to its conflict of law provisions.

## **Refund Policy!**

**All payments made to the Company are non-refundable. We do not provide refunds for any products or services purchased on our website.**''')
    elif data['df'][0] == 'faq':
        if streamlit_js_eval(js_expressions='screen.width', key = 'SCR')<700:
            st.image('faq.png',width=400)
        else:
            st.image('faq.png',width=1350)
        st.markdown('''# Frequently Asked Questions From Our Students

We've gathered the most commonly asked questions we see in our VisualSkill Community and collected the best answers created by our community guides, moderators, and learners.

Whether you're a new learner seeking information or a seasoned participant looking for a quick refresher, this comprehensive guide aims to address your queries and provide valuable insights. So, let's dive in and explore the wealth of knowledge that will empower you to make the most of your learning experience on VisualSkill.
                    
---
                    
## What types of internships do you offer?

We offer a diverse range of internships across various industries, including technology, marketing, finance, healthcare, and more. This allows students to explore different fields and gain valuable experience.
                    
---
                    
## How can I apply for an internship?

To apply for an internship, simply visit our website and browse through the available opportunities. Click on the internship you're interested in and follow the application instructions provided. Make sure to submit all required documents and information.
                    
---
                    
## Are the internships paid?

While some internships are paid, others may offer academic credit or valuable hands-on experience. The compensation details are specified in each internship listing. We strive to provide a mix of paid and unpaid opportunities to cater to different student needs.
                    
---
                    
## What qualifications do I need to apply for an internship?

The qualifications vary depending on the specific internship. Most positions require applicants to be current college students or recent graduates. Other qualifications may include specific skills, coursework, or relevant experience. Check the individual internship listings for detailed requirements.
                    
---
                    
## How long do the internships last?

The duration of internships varies, with some lasting a few weeks and others spanning several months. The specific time frame will be mentioned once the intern starts. Students can choose opportunities that align with their academic schedules and career goals.
                    
---
                    
## Do you provide support for resume building and interview preparation?

Yes, we offer resources and guidance to help students enhance their resumes and prepare for interviews. Our goal is to equip interns with the skills and confidence needed to succeed in the application and interview process.
                    
---
                    
## Can international students apply for internships?

Yes, we welcome applications from international students. However, certain internships may have specific eligibility criteria or work authorization requirements. It's essential to review the details of each internship to ensure eligibility.
                    
---
                    
## What kind of support is provided during the internship?

Throughout the internship, we provide ongoing support to both students and employers. This includes e-books, course material, step-by-step guides, manuals, regular check-ins, feedback sessions, and resources to ensure a positive and enriching experience for everyone involved.
                    
---
                    
## Can interns receive academic credit for their work?

Many of our internships offer the option for students to receive academic credit. However, it's important for students to coordinate with their academic institutions to ensure that the internship meets their school's requirements.
''')
except Exception as e:
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