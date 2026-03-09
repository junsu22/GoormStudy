"""
토이 프로젝트 - 유튜브 썸네일 이미지 추출하기
만들앱 : yt-img-app
앱의 기능 :
- 사용자로부터 YouTube URL을 입력받기
- URL 의 텍스트 처리를 수행하여 고유한 YouTube 비디오ID 추출하기
- YouTube 비디오의 썸네일 이미지를 검색하고 표시하는 사용자 정의 함수에
YouTube 비디오ID를 입력으로 사용하기

출력 | 스트림릿 앱을 사용하기 위해서는 YouYube URL 을 입력 텍스트 상자에 복사하여 붙여넣으세요.
"""

# 라이브러리 가지고 오기
import streamlit as st

# 앱의 제목과 헤더
st.title("yt-img-app")
st.header("YouTube 썸네일 이미지 추출기 앱")
# 확장 가능한 상자 추가
with st.expander("이 앱에 대하여"):
    st.write("이 앱은 YouTube 동영상의 썸네일 이미지를 검색합니다.")


# 이미지 설정
st.sidebar.header("설정")
img_dict = {
    "Max": "maxresdefault",  # 최대화질
    "High": "hqdefault",  # 고화질
    "Medium": "mqdefault",  # 중화질
    "Standard": "sddefault",  # 표준화질
}
#   사이드바에서 품질선택 → 딕셔너리 로 실제 파일 명 변환(드롭다운 생성)
selected_img_quality = st.sidebar.selectbox(
    "이미지 품질 선택",
    [
        "Max",
        "High",
        "Medium",
        "Standard",
    ],  # 선택한 품질에 따라 다른 해상도의 썸네일 이미지가 출력됨
)
# 선택한 품질을 유튜브 API 파일명으로 변환
img_quality = img_dict[selected_img_quality]

# 이미지를 추출할 동영상 URL 입력. 텍스트 상자
yt_url = st.text_input("YouTube URL 붙여넣기", "https://youtu.be/")


# YouTube URL에서 video ID만 추출하는 함수
def get_ytid(input_url):
    ytid = ""  # 변수 초기화 (에러 방지)
    if "youtu.be" in input_url:  # 단축 URL 형식 (youtu.be/abc123)
        ytid = input_url.split("/")[-1].split("?")[0]  # "/"로 나눈 뒤 ? 앞부분 추출
    elif "youtube.com" in input_url:  # 일반 URL 형식 (youtube.com/watch?v=abc123)
        ytid = input_url.split("=")[1].split("&")[0]  # "="로 나눈 뒤 & 앞부분 추출
    return ytid


# Youtube URL 이 입력되면 썸네일, 아니라면 안내메세지 출력
# 실제 URL 이 입력되었는지 확인
if yt_url != "https://youtu.be/":
    ytid = get_ytid(yt_url)  # URL에서 비디오 ID 추출
    #  썸네일 이미지 URL 생성
    yt_img = f"http://img.youtube.com/vi/{ytid}/{img_quality}.jpg"
    st.image(yt_img)  # 썸네일 이미지를 표시
    st.write("YouTube 동영상 썸네일 이미지 URL: ", yt_img)  # (확인용) 이미지 URL 표시
else:
    st.write("URL을 입력해 계속하세요!")  # 입력하지 않았을경우
