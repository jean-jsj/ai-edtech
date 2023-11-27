import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import time
from st_pages import show_pages_from_config, add_page_title
add_page_title()
show_pages_from_config()

# def app():
st.write("account page")

if st.session_state['login']== True:
  
  st.write(f"{st.session_state['sid']}님 환영합니다.")
  if st.session_state['admin'] == True:
    st.write("관리자입니다")
  if st.session_state['teacher'] == True:
    # account menu for teacher
    pass
  else: 
    # account menu for student
    pass
else:
  st.write("로그인이 필요합니다.")
  time.sleep(3)
  st.button("Home", on_click=switch_page('main'))
  
  
  
  
def get_student_info(sid):
  pass
  
def get_student_progress(sid):
  pass

def get_student_(sid):
  pass