##### 기본 정보 불러오기 ####
# Streamlit 패키지 추가
import streamlit as st
# OpenAI 패키기 추가
import openai

##### 기능 구현 함수 #####
def askGpt(prompt,apikey):
    client = openai.OpenAI(api_key = apikey)
    response = client.chat.completions.create(
    model="gpt-5",
    messages=[{"role": "user", "content": prompt}])
    gptResponse = response.choices[0].message.content
    return gptResponse

##### 메인 함수 #####
def main():
    st.set_page_config(page_title="요약 프로그램")
    # session state 초기화
    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""

    # 사이드바
    with st.sidebar:
        # Open AI API 키 입력받기
        open_apikey = st.text_input(label='OPENAI API 키', placeholder='Enter Your API Key', value='',type='password')    
        # 입력받은 API 키 표시
        if open_apikey:
            st.session_state["OPENAI_API"] = open_apikey
        st.markdown('---')

    st.header("📃요약 프로그램")
    st.markdown('---')
    
    text = st.text_area("요약 할 글을 입력하세요")
    if st.button("요약"):
        prompt = f'''
            **Instructions** :
    You are an online content analysis expert. Given an internet content URL, you have the expertise to accurately and clearly summarize its content using the following methods:

    Extracting key phrases: TF-IDF method
    Summarizing the content: TextRank algorithm
    Listing chapter headings: Clustering technique
    Please provide me with the internet content URL so I can perform the following tasks and provide the results in Markdown format:

    1) Content Title
    2) Extract key phrases
    3) Write a brief summary in 50 characters or less
    4) Analyze the content to create a concise list of chapter headings
    5) Summarize the entire post
    - Include important details without omission
    - Bold new terms and provide definitions at the end of the summary if necessary
    - Summarize in 500 characters or less

    Please do not add any content that is not included in the URL I provide. Answer in Korean.
    -text : {text}
    '''
        st.info(askGpt(prompt,st.session_state["OPENAI_API"]))

if __name__=="__main__":
    main()
