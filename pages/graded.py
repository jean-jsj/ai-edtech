import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
import src.db as db
import json
from st_pages import show_pages_from_config, add_page_title
add_page_title()
show_pages_from_config()

# 수식 left align
st.markdown('''
<style>
.katex-html {
    text-align: left;
}
</style>''',
unsafe_allow_html=True
)

# indentation 변경
st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    padding-left:40px;
}
</style>
''', unsafe_allow_html=True
)
 
### 변수 가져오기
#problem_id = st.session_state['problem_id']
#student_id = st.session_state['student_id']
#name = st.session_state['name']
problem_id = 1
student_id = 12345678
name = '홍길동'
answer = db.get_solution(problem_id)
solved_answer = db.get_answer(problem_id, student_id)

### 화면 구성
selected = option_menu(None, ["학습메뉴", "챗봇과 얘기하기", "다음 문제로 이동"],
    icons=['house', 'chat', 'arrow-right-square'],
    menu_icon="cast", default_index=0, orientation="horizontal")

st.subheader("문제 번호: "+problem_id)
st.latex(r'''
    problem['question']
''')
st.markdown("***")

st.subheader("정답 풀이")
st.latex(r'''
    answer['solution']
''')
st.markdown("***")

st.subheader(f"{name}님의 답안") 
st.latex(r'''
    solved_answer['student_answer']
''')
st.markdown("***")

st.subheader("채점 결과")
step_criteria = json.loads(answer['step_criteria'])

for i in range(len(step_criteria)):
    st.markdown("{0}: {1}점 / {2}점".format(step_criteria.values()[i], answer['step_score'][i], solved_answer['score'][i]))

st.subheader(":red[최종 점수: {0}점]".format(answer['total_score']))

if selected == "학습메뉴":
    switch_page('menu')
if selected == "챗봇과 얘기하기":
    switch_page('chatbot')
if selected == "다음 문제로 이동":
    #st.session_state['problem_id'] = recommend_problem(unit_id, student_id, problem_id):
    st.session_state['problem_id'] = 2
    switch_page('practice')