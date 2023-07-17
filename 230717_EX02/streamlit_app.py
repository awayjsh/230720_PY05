import streamlit as st
import math

msg = "Hello World!!!"
st.write(msg)  # 문자열 직접 넣어도 상관 없음 (streamlit -> print?)

# 터미널(git bash, cmd) : pip install streamlit (ctrl+`)

st.write(math.pi)

# 원주율
PI = math.pi
# 반지름
radius = 15

PI_is = '원주율 : '
radius_is = '반지름 : '
circum = '원의 둘레 : '
area = '원의 넓이 : '

st.write(PI_is, PI)
st.write(radius_is, radius)
st.write(circum, radius * 2 * PI)
# st.write(area, radius * radius * PI)
st.write(area, radius ** 2 * PI)

with st.echo():
    st.write(PI_is, PI)
    st.write(radius_is, radius)
    st.write(circum, radius * 2 * PI)
    # st.write(area, radius * radius * PI)
    st.write(area, radius ** 2 * PI)

with st.echo():
    radius = st.number_input("반지름 입력")
    st.write(PI_is, PI)
    st.write(radius_is, radius)
    st.write(circum, radius * 2 * PI)
    # st.write(area, radius * radius * PI)
    st.write(area, radius ** 2 * PI)