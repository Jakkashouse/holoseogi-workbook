import streamlit as st

st.set_page_config(
    page_title="나의 속도로 걷는 홀로서기",
    page_icon="🌱",
    layout="centered",
)

st.title("🌱 나의 속도로 걷는 홀로서기")
st.markdown("편안한 마음으로 빈칸을 채워주세요. 단어 하나부터 천천히 시작해 보세요.")

# 탭 나누기
tab1, tab2, tab3 = st.tabs(["1장. 현재의 나", "2장. 홀로서기", "3장. 미래와 꿈"])

# 입력 데이터 저장을 위한 딕셔너리
responses = {}

with tab1:
    st.subheader("나라는 사람의 사용 설명서")
    st.info("나를 가장 기분 좋게 만드는 '나만의 소울푸드'는 무엇인가요?")
    responses['q1_word'] = st.text_input("짧은 단어로 적어보기", key="q1_w")
    responses['q1_desc'] = st.text_area("왜 이 음식을 좋아하나요? 언제 주로 생각나나요?", key="q1_d")

    st.info("주말에 아무런 제약이 없다면, 내가 가장 먼저 하고 싶은 일은 무엇인가요?")
    responses['q2_word'] = st.text_input("짧은 단어로 적어보기", key="q2_w")
    responses['q2_desc'] = st.text_area("그 일을 하면 어떤 기분이 들 것 같나요?", key="q2_d")

with tab2:
    st.subheader("나만의 공간, 나만의 속도")
    st.info("완벽하게 나만의 공간(방)이 생긴다면, 꼭 두고 싶은 물건 3가지는 무엇인가요?")
    responses['q3_word'] = st.text_input("세 가지 물건 적어보기", key="q3_w")
    responses['q3_desc'] = st.text_area("왜 이 물건들이 꼭 필요한가요?", key="q3_d")

with tab3:
    st.subheader("내일의 나, 그리고 세상에 띄우는 편지")
    st.info("3년 뒤, 꽤 멋지게 홀로서기에 성공한 나에게 '카톡 메시지'를 보낼 수 있다면?")
    responses['q4_word'] = st.text_input("보내고 싶은 메시지", key="q4_w")
    responses['q4_desc'] = st.text_area("나에게 어떤 칭찬과 격려를 해주고 싶나요?", key="q4_d")

# 결과물 다운로드 섹션
st.divider()
st.subheader("📝 작성 완료")

# 입력된 데이터를 보기 좋게 텍스트로 정리
result_text = f"""[ 1장. 현재의 나 ]

Q. 나만의 소울푸드
- 단어: {responses.get('q1_word', '')}
- 이유: {responses.get('q1_desc', '')}

Q. 가장 하고 싶은 일
- 단어: {responses.get('q2_word', '')}
- 이유: {responses.get('q2_desc', '')}

[ 2장. 홀로서기 ]

Q. 나만의 공간에 둘 물건 3가지
- 단어: {responses.get('q3_word', '')}
- 이유: {responses.get('q3_desc', '')}

[ 3장. 미래와 꿈 ]

Q. 미래의 나에게 보내는 메시지
- 단어: {responses.get('q4_word', '')}
- 이유: {responses.get('q4_desc', '')}
"""

# 다운로드 버튼
st.download_button(
    label="내용 저장하기 (텍스트 파일)",
    data=result_text,
    file_name="나의_홀로서기_기록.txt",
    mime="text/plain",
)
