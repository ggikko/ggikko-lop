import pandas as pd
import matplotlib.pyplot as plt
import nltk
from matplotlib import rc
import re
from wordcloud import WordCloud, STOPWORDS
from konlpy.tag import Okt


# 1. 불필요 제거
# 2. url제거
# 3. 자음모음제거
# 4. 특수기호제거
def preprocessing(input):
    temp = re.sub('사진|링크|이모티콘|들어왔습니다|나갔습니다|메세지를|가렸습니다|관리자가', '', input)
    temp = re.sub(
        r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))",
        '', temp)
    temp = re.sub('[ㄱ-ㅎ]*|[ㅏ-ㅢ]*', '', temp)
    temp = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', temp)
    return temp


# messages -> tokens
def token_list(series):
    message_list = []
    for message in series:
        for token in str(message).split():
            message_list.append(token)
    return message_list


# user series -> dict
def get_user_dict(dataframe):
    users_pretty_dict = dataframe.groupby('User')
    temp = {}
    for user_name, index in users_pretty_dict.groups.items():
        temp[user_name] = list(index)
    return temp


# okt -> text to text
def get_okt_text(full_text):
    tokenizer = Okt()
    tokens = tokenizer.morphs(full_text)
    return ' '.join(tokens)


# show plot user frequency
def show_user_freq(username, data_frame):
    message_ = data_frame.loc[df['User'] == username, 'Message']
    total_tokens = token_list(message_)
    text = nltk.Text(total_tokens, name='katalk')

    plt.figure(figsize=(16, 10))
    text.plot(50)


# show plot for series
def show_plot(series):
    text = nltk.Text(token_list(series), "katalk")
    plt.figure(figsize=(16, 10))
    text.plot(50)


# show word cloud for full text and save img
def show_word_cloud(full_text, need_save=False, file_name="temp"):
    wordcloud = WordCloud(
        font_path='NanumBarunGothic.ttf',
        width=800,
        height=800
    )
    wc = wordcloud.generate_from_text(full_text)
    array = wc.to_array()
    fig = plt.figure(figsize=(12, 12))
    plt.imshow(array, interpolation="bilinear")
    plt.show()
    if need_save:
        fig.savefig(file_name)


# 1. font & load data
# 2. message 정제 & empty 제거
# 3. plot 보기
# 4. word cloud
# 4-1. word cloud with konlpy
# 5. user별 빈도분석
# 6. 연도별 빈도분석

# font & load
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_csv('data/katalk_klayton_full.csv')

# message 정재
df['Message'] = df['Message'].apply(preprocessing)
df = df[df['Message'] != '']

# plot
show_plot(df['Message'])

# word cloud
show_word_cloud(' '.join(df['Message']))

# okt
show_word_cloud(get_okt_text(' '.join(df['Message'])))

# 빈도 분석
show_user_freq('Tony Stark', df)

# 연도 기준 메세지 분석
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
year = "2020"
show_plot(df[year + '-01-01': year + '-12-31']['Message'])
