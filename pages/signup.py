import streamlit as st
from streamlit_extras.switch_page_button import switch_page 
import src.db as db
import datetime
from st_pages import show_pages_from_config, add_page_title
# add_page_title()
# show_pages_from_config()


st.set_page_config(
    page_title = "Sign-up",
)

if 'login' in st.session_state:
    if st.session_state['login'] == False:
        st.write("signup page")
        
        # signup form
        with st.form("signup"):
            new_account = st.text_input('ID:', autocomplete="on", placeholder="아이디 입력", max_chars=10)
            new_password = st.text_input('Password:', type='password', placeholder="비밀번호 입력", max_chars=4)
            new_name= st.text_input('Name:', placeholder="이름 입력", max_chars=10)
            new_age = st.text_input('Age:', placeholder="나이 입력", max_chars=2)
            new_grade = st.text_input('Grade:', placeholder="학년 입력", max_chars=2)
            
            submitted = st.form_submit_button("회원가입")
            if submitted:
                if new_account and new_password:
                    # print(datetime.datetime.now(), "signup submitted", new_account, new_password)
                    if not new_grade == '10' or new_grade == '11':
                        st.error("학년은 10, 11만 입력 가능합니다.")
                        switch_page("signup")
                    success = db.add_user(new_account, new_password, new_name, new_age, new_grade)
                    if success:
                        st.success("회원가입 성공! 로그인해주세요")
                        # 회원가입시 학년(grade)에 맞게 subject - area - main unit - sub unit - knowledge 값들이 student_db에 입력됨
                        db.init_db_using_signup(new_account, new_grade)
                        
                        
                        
                        
                        
                        
                        switch_page("home")
                    else:
                        st.error("이미 존재하는 ID입니다.")
                else:
                    st.error("모든 정보를 입력해주세요")
                    # write postgresql query to check if the user_id exists in the database
                    
                    # if it exists, redirect to login page
    else:
        # TODO: redirect to another page
        st.write("이미 로그인중입니다.")
        clicked = st.button("Go to main page")
        if clicked:
            switch_page("home")
else:
    st.session_state['login'] = False
    switch_page("home")

