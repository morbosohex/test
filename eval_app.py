import streamlit as st
import numpy
import time
import pandas
import datetime
from Config import Config
config = Config()

keywords = ['apple', 'laptop', 'MacBook Air',
            'siver', 'gray', '15 inch', '16Gb']

clf_result = [('brand', {'MacBook Air'}),
              ('category', set()),
              ('color', {'MacBook Air', 'apple', 'gray'}),
              ('country', set()),
              ('currency', set()),
              ('group', set()),
              ('material', set()),
              ('scene', set()),
              ('ship', set()),
              ('size', {'16Gb', '15 inch'}),
              ('style', set()),
              ('other', {'siver', 'laptop'})]

# 按钮
if st.button('获取关键词'):
    st.write(pandas.DataFrame({'keywords': keywords}))

# 多个选择框
drop_keywords = []
for keyword in keywords:
    drop = st.checkbox(keyword)
    if drop:
        drop_keywords.append(keyword)
st.write(pandas.DataFrame({'drop_keywords': drop_keywords}))
        


combinations = pandas.read_csv('keywords.csv')


# 静态信息显示
df = pandas.DataFrame({'col1': [1, 2, 3]})
df  # <-- Draw the dataframe
st.text('This is some text.\nasdfas asdfa asdfsa')
st.markdown('Streamlit is **_really_ cool**.')
st.header('This is a header')
st.subheader('This is a subheader')
st.dataframe(combinations.keyphrase, 2000, 500)

# 单一选择框
genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")

# 选择框二
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

# 选择框三
options = st.multiselect(
    'What are your favorite colors',
    ('Green', 'Yellow', 'Red', 'Blue'))

st.write('You selected:', options)

# 滑杆
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)


# 字符串输入框
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

# 数字输入框
number = st.number_input('Insert a number', 1, 50, 25, 5)
st.write('The current number is ', number)

# 输入多行文本
txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')
model_result = 1
st.write('This model predict result:', model_result)


# 输入日期
d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

# 输入时间
t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)


# 进度条

st.text('加载词典')
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.02)
    my_bar.progress(percent_complete + 1)
st.text('加载完成！')

st.write('\n\n\n')

# 横幅+进度条
with st.spinner('加载词典...'):
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.02)
        my_bar.progress(percent_complete + 1)
st.success('加载完成!')


# 成功条幅信息
st.success('This is a success message!')

# 数据合并
df1 = pandas.DataFrame(
   numpy.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))
my_table = st.table(df1)

df2 = pandas.DataFrame(
   numpy.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))
my_table.add_rows(df2)
