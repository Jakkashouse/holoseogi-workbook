import streamlit as st

st.set_page_config(
    page_title="나의 속도로 걷는 홀로서기",
    page_icon="🌱",
    layout="centered",
)

st.title("🌱 [공저 프로젝트] 나의 속도로 걷는 홀로서기 (가제)")
st.markdown(
    "아래 질문들 중 마음에 드는 것을 자유롭게 골라 편안한 마음으로 빈칸을 채워주세요. "
    "이 질문지에는 정답이 없습니다. 여러분이 겪은 일, 좋아하는 것, 상상하는 모든 것이 "
    "곧 훌륭한 책의 내용이 됩니다. 단어 하나부터 천천히 시작해 보세요."
)

# 입력 데이터 저장을 위한 딕셔너리
responses = {}

# 탭 나누기
tab1, tab2, tab3 = st.tabs([
    "제1장. 현재의 나",
    "제2장. 홀로서기",
    "제3장. 미래와 꿈",
])

# ─────────────────────────────────────────────
# 제1장. 나라는 사람의 사용 설명서 (현재의 나)
# ─────────────────────────────────────────────
with tab1:
    st.subheader("제1장. 나라는 사람의 사용 설명서")

    st.info("1. 지금의 나를 해시태그(#) 3개로 표현한다면 무엇인가요?")
    c1, c2, c3 = st.columns(3)
    with c1:
        responses['q1_tag1'] = st.text_input("#", key="q1_t1")
    with c2:
        responses['q1_tag2'] = st.text_input("#", key="q1_t2")
    with c3:
        responses['q1_tag3'] = st.text_input("#", key="q1_t3")
    responses['q1_desc'] = st.text_area("왜 이 해시태그를 골랐는지 적어주세요.", key="q1_d")

    st.info("2. 나를 가장 기분 좋게 만드는 '나만의 소울푸드'는 무엇인가요?")
    responses['q2_word'] = st.text_input("먼저 짧은 단어로 적어보기", key="q2_w")
    responses['q2_desc'] = st.text_area("왜 이 음식을 좋아하나요? 언제 주로 생각나나요?", key="q2_d")

    st.info("3. 요즘 내 스마트폰 플레이리스트에서 가장 많이 듣는 노래는 무엇인가요?")
    responses['q3_word'] = st.text_input("먼저 짧은 단어로 적어보기", key="q3_w")
    responses['q3_desc'] = st.text_area("어떤 가사나 멜로디가 마음에 와닿았나요?", key="q3_d")

    st.info("4. 주말에 아무런 제약(시간, 돈 등)이 없다면, 내가 가장 먼저 하고 싶은 일은 무엇인가요?")
    responses['q4_word'] = st.text_input("먼저 짧은 단어로 적어보기", key="q4_w")
    responses['q4_desc'] = st.text_area("그 일을 하면 어떤 기분이 들 것 같나요?", key="q4_d")

    st.info("5. 내가 생각해도 꽤 괜찮은 나의 장점(성격, 외모, 사소한 기술 등) 딱 한 가지를 자랑해 본다면?")
    responses['q5_word'] = st.text_input("먼저 짧은 단어로 적어보기", key="q5_w")
    responses['q5_desc'] = st.text_area("주로 언제 내 장점이 빛난다고 느끼나요?", key="q5_d")

# ─────────────────────────────────────────────
# 제2장. 나만의 공간, 나만의 속도 (홀로서기에 대하여)
# ─────────────────────────────────────────────
with tab2:
    st.subheader("제2장. 나만의 공간, 나만의 속도")

    st.info("6. '자립'이나 '독립'이라는 단어를 들으면 가장 먼저 떠오르는 감정은 무엇인가요?")
    responses['q6_word'] = st.text_input("먼저 짧은 단어로 적어보기 (예: 설렘, 두려움, 기대 등)", key="q6_w")
    responses['q6_desc'] = st.text_area("왜 그런 감정이 가장 먼저 들었는지 적어주세요.", key="q6_d")

    st.info("7. 내가 생각하는 '진짜 어른'은 어떤 사람인가요?")
    responses['q7_word'] = st.text_input("먼저 짧은 단어로 적어보기", key="q7_w")
    responses['q7_desc'] = st.text_area("내가 그런 어른이 되기 위해 필요한 것은 무엇일까요?", key="q7_d")

    st.info("8. 완벽하게 나만의 공간(방)이 생긴다면, 꼭 두고 싶은 물건 3가지는 무엇인가요?")
    o1, o2, o3 = st.columns(3)
    with o1:
        responses['q8_item1'] = st.text_input("물건 1", key="q8_i1")
    with o2:
        responses['q8_item2'] = st.text_input("물건 2", key="q8_i2")
    with o3:
        responses['q8_item3'] = st.text_input("물건 3", key="q8_i3")
    responses['q8_desc'] = st.text_area("왜 이 물건들이 내 공간에 꼭 필요한가요?", key="q8_d")

    st.info("9. 내가 \"이제 나도 어른이구나\"라고 느꼈던, 아주 사소하지만 뿌듯했던 순간이 있나요?")
    responses['q9_word'] = st.text_input("먼저 짧은 단어로 적어보기", key="q9_w")
    responses['q9_desc'] = st.text_area("그때 어떤 감정을 느꼈는지 생생하게 적어주세요.", key="q9_d")

    st.info("10. 독립의 첫날, 아침에 눈을 떠서 가장 먼저 하고 싶은 일은 무엇인가요?")
    responses['q10_word'] = st.text_input("먼저 짧은 단어로 적어보기", key="q10_w")
    responses['q10_desc'] = st.text_area("상상만 해도 기분 좋아지는 나만의 아침 루틴을 적어보세요.", key="q10_d")

    st.info("11. 홀로서기를 앞두고 가장 설레는 점 한 가지와, 아주 살짝 걱정되는 점 한 가지는 무엇인가요?")
    e1, e2 = st.columns(2)
    with e1:
        responses['q11_excite'] = st.text_input("설레는 점", key="q11_e")
    with e2:
        responses['q11_worry'] = st.text_input("걱정되는 점", key="q11_wo")
    responses['q11_desc'] = st.text_area("그렇게 생각한 이유를 솔직하게 적어주세요.", key="q11_d")

# ─────────────────────────────────────────────
# 제3장. 내일의 나, 그리고 세상에 띄우는 편지 (미래와 꿈)
# ─────────────────────────────────────────────
with tab3:
    st.subheader("제3장. 내일의 나, 그리고 세상에 띄우는 편지")

    st.info("12. 10년 뒤의 나는 어떤 모습으로, 어떤 표정을 짓고 살아가고 있을까요?")
    responses['q12_word'] = st.text_input("먼저 짧은 단어나 문장으로 적어보기", key="q12_w")
    responses['q12_desc'] = st.text_area("내가 꿈꾸는 10년 뒤의 평범한 하루 일과를 적어주세요.", key="q12_d")

    st.info("13. 3년 뒤, 꽤 멋지게 홀로서기에 성공한 나에게 '카톡 메시지'를 보낼 수 있다면?")
    responses['q13_word'] = st.text_input("먼저 짧은 문장으로 적어보기 (\"...\")", key="q13_w")
    responses['q13_desc'] = st.text_area("나에게 어떤 칭찬과 격려를 해주고 싶나요?", key="q13_d")

    st.info("14. 자립을 준비하며 막막함을 느낄 후배나 친구들에게 꼭 해주고 싶은 '나만의 팁'이나 응원은 무엇인가요?")
    responses['q14_word'] = st.text_input("먼저 짧은 단어나 문장으로 적어보기", key="q14_w")
    responses['q14_desc'] = st.text_area("먼저 고민해 본 사람으로서, 어떤 마음을 전하고 싶나요?", key="q14_d")

    st.info("15. 내가 세상에 작게라도 좋은 영향을 줄 수 있다면, 어떤 모습일까요?")
    responses['q15_word'] = st.text_input("먼저 짧은 단어로 적어보기", key="q15_w")
    responses['q15_desc'] = st.text_area("어떤 직업이든, 어떤 태도든 상관없습니다. 자유롭게 상상해 보세요.", key="q15_d")

    st.info("16. 우리들의 이야기가 담긴 이 책을 읽게 될 사람들에게, 나는 '어떤 사람'으로 기억되고 싶나요?")
    responses['q16_word'] = st.text_input("먼저 짧은 단어로 적어보기", key="q16_w")
    responses['q16_desc'] = st.text_area("나의 솔직한 이야기가 사람들에게 어떤 작은 힘이 되기를 바라나요?", key="q16_d")

    st.info("17. 내 이름이 적힌 이 책이 세상에 나왔을 때, '작가의 말' 첫 문장에 어떤 글을 적고 싶나요?")
    responses['q17_word'] = st.text_input("먼저 짧은 문장으로 적어보기", key="q17_w")
    responses['q17_desc'] = st.text_area(
        "이 책을 쓰면서 느낀 점이나, 가장 먼저 고마움을 전하고 싶은 대상에 대해 적어보세요.",
        key="q17_d",
    )

# ─────────────────────────────────────────────
# 결과물 다운로드 섹션
# ─────────────────────────────────────────────
st.divider()
st.subheader("📝 작성 완료")
st.caption("아래 버튼으로 작성한 내용을 텍스트 파일로 저장할 수 있습니다.")

g = responses.get  # 단축

result_text = f"""[공저 프로젝트] 나의 속도로 걷는 홀로서기 (가제)

══════════════════════════════════════
 제1장. 나라는 사람의 사용 설명서 (현재의 나)
══════════════════════════════════════

1. 지금의 나를 해시태그 3개로 표현한다면?
   - 해시태그: #{g('q1_tag1', '')} #{g('q1_tag2', '')} #{g('q1_tag3', '')}
   - 이유: {g('q1_desc', '')}

2. 나만의 소울푸드는?
   - 단어: {g('q2_word', '')}
   - 이유: {g('q2_desc', '')}

3. 요즘 가장 많이 듣는 노래는?
   - 단어: {g('q3_word', '')}
   - 이유: {g('q3_desc', '')}

4. 제약이 없다면 주말에 가장 먼저 하고 싶은 일은?
   - 단어: {g('q4_word', '')}
   - 이유: {g('q4_desc', '')}

5. 자랑하고 싶은 나의 장점 한 가지는?
   - 단어: {g('q5_word', '')}
   - 이유: {g('q5_desc', '')}

══════════════════════════════════════
 제2장. 나만의 공간, 나만의 속도 (홀로서기에 대하여)
══════════════════════════════════════

6. '자립/독립' 하면 떠오르는 감정은?
   - 단어: {g('q6_word', '')}
   - 이유: {g('q6_desc', '')}

7. 내가 생각하는 '진짜 어른'은?
   - 단어: {g('q7_word', '')}
   - 이유: {g('q7_desc', '')}

8. 나만의 공간에 꼭 두고 싶은 물건 3가지는?
   - 물건: 1.{g('q8_item1', '')} / 2.{g('q8_item2', '')} / 3.{g('q8_item3', '')}
   - 이유: {g('q8_desc', '')}

9. "이제 나도 어른이구나" 뿌듯했던 순간은?
   - 단어: {g('q9_word', '')}
   - 이유: {g('q9_desc', '')}

10. 독립 첫날 아침, 가장 먼저 하고 싶은 일은?
   - 단어: {g('q10_word', '')}
   - 이유: {g('q10_desc', '')}

11. 홀로서기를 앞둔 설렘과 걱정은?
   - 설레는 점: {g('q11_excite', '')} / 걱정되는 점: {g('q11_worry', '')}
   - 이유: {g('q11_desc', '')}

══════════════════════════════════════
 제3장. 내일의 나, 그리고 세상에 띄우는 편지 (미래와 꿈)
══════════════════════════════════════

12. 10년 뒤의 나는 어떤 모습일까?
   - 단어: {g('q12_word', '')}
   - 이유: {g('q12_desc', '')}

13. 3년 뒤의 나에게 보내는 카톡 메시지는?
   - 메시지: {g('q13_word', '')}
   - 이유: {g('q13_desc', '')}

14. 자립을 준비하는 후배/친구에게 전하는 팁/응원은?
   - 단어: {g('q14_word', '')}
   - 이유: {g('q14_desc', '')}

15. 내가 세상에 줄 수 있는 작은 좋은 영향은?
   - 단어: {g('q15_word', '')}
   - 이유: {g('q15_desc', '')}

16. 독자에게 '어떤 사람'으로 기억되고 싶은가?
   - 단어: {g('q16_word', '')}
   - 이유: {g('q16_desc', '')}

17. '작가의 말' 첫 문장에 적고 싶은 글은?
   - 문장: {g('q17_word', '')}
   - 이유: {g('q17_desc', '')}
"""

st.download_button(
    label="내용 저장하기 (텍스트 파일)",
    data=result_text,
    file_name="나의_홀로서기_기록.txt",
    mime="text/plain",
)
