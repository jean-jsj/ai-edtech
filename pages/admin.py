import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import src.db as db

st.write('admin page')

if st.session_state['login'] == True:
    if st.session_state['admin'] == True: # Admin page
        
        with st.form("delete_user"):
            delete_id = st.text_input('Delete ID:', autocomplete="on", placeholder="아이디 입력", max_chars=10)
            submitted = st.form_submit_button("Delete user")
            if submitted:
                success = db.delete_user(delete_id)
                if success: 
                    st.success(f"User '{delete_id}' deleted")
                else:
                    st.error("User not found")
            
        
        
        
        submitted = st.button('View all users')
        if submitted:
            st.write(db.view_all_users())
        
    
    else:
        st.write("Not authorized")
        clicked = st.button('Go to main page')
        if clicked:
            switch_page("main")
        
    
else: # not logged in
    st.write("로그인이 필요합니다.")
    clicked = st.button('Go to main page')
    if clicked:
        switch_page("main")

    # switch_page("main")



def delete_user(sid):
    return db.delete_user(sid)
    