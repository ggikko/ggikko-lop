import math
import time
import pandas as pd

startTime = time.time()


def hasItem(df):
    if len(df) > 0:
        return True
    else:
        return False


def getJoinCount(df, company_name: str):
    find = df.loc[df['사업장명'].str.contains(company_name, regex=False)].head(1)
    if hasItem(find):
        return find["신규"].values[0]
    else:
        return 0


def getLeaveCount(df, company_name: str):
    find = df.loc[df['사업장명'].str.contains(company_name, regex=False)].head(1)
    if hasItem(find):
        return find["상실"].values[0]
    else:
        return 0


# data list
month_data_list = []

loadStartTime = time.time()

# load data
for i in range(1, 9):
    path = "/Users/jihongpark/Documents/Week2/data/salary_0" + str(i) + "month.csv"
    month_data_list.append(pd.read_csv(path))

loadEndTime = time.time()
print("elapsed time for load data : " + str(int(loadEndTime - loadStartTime)) + "s")

# change columns
columns = ['자료생성년월', '사업장명', '사업자번호', '가입상태', '우편번호', '지번주소', '도로명주소', '법정주소코드',
           '행정주소코드', '광역시코드', '시군구코드', '읍면동코드', '사업장형태', '업종코드', '업종코드명',
           '적용일', '재등록일', '탈퇴일', '가입자수', '고지금액', '신규', '상실', ]

for temp_df in month_data_list:
    temp_df.columns = columns

latestDataFrame = month_data_list[len(month_data_list) - 1]
latestDataFrameCopy = latestDataFrame.copy()

# sort(평균연봉)
latestDataFrameCopy['인당고지금액'] = latestDataFrameCopy['고지금액'] / latestDataFrameCopy['가입자수']
latestDataFrameCopy['평균월급'] = latestDataFrameCopy['인당고지금액'] / 9 * 100
latestDataFrameCopy['평균연봉'] = latestDataFrameCopy['평균월급'] * 12
sorted_by_salary = latestDataFrameCopy.sort_values(by="평균연봉", ascending=False).reset_index(drop=True).copy()

# condition
target_company = "삼성전자"
find_condition = sorted_by_salary['사업장명'].str.contains(target_company, regex=False)

# find
find_company = sorted_by_salary.loc[find_condition, ["사업장명", "가입자수", "도로명주소", "신규", "상실", "고지금액", "평균연봉"]].head(1)

if hasItem(find_company):
    # 연봉 상위 몇프로
    find_company_name = find_company["사업장명"].values[0]
    find_company_rank = find_company.index.values[0]
    find_company_expected_salary = math.ceil(find_company["평균연봉"].values[0])
    find_company_address = find_company["도로명주소"].values[0]
    find_company_join_count = find_company["가입자수"].values[0]
    new_join_count = find_company["신규"].values[0]
    total_company_count = len(latestDataFrameCopy)

    # rank
    find_percent = round((find_company_rank / total_company_count * 100), 2)

    # join
    joinTotalCount = 0
    for temp_df in month_data_list:
        joinTotalCount = joinTotalCount + getJoinCount(temp_df, target_company)

    # leave
    leaveTotalCount = 0
    for temp_df in month_data_list:
        leaveTotalCount = leaveTotalCount + getLeaveCount(temp_df, target_company)

    print("회사이름 : " + find_company_name)
    print("연봉순위 : " + format(find_company_rank, ",") + "위")
    print("전체회사 수 : " + format(total_company_count, ",") + "개")
    print("가입자수 : " + format(find_company_join_count, ",") + "명")
    print("도로명주소 : " + find_company_address)
    print("예상연봉 : " + format(find_company_expected_salary, ",") + "원")
    print("상위퍼센트 : " + str(find_percent) + "%")
    print("입사 : " + format(joinTotalCount, ",") + "명")
    print("퇴사 : " + format(leaveTotalCount, ",") + "명")
else:
    print("not found")

endTime = time.time()
print("elapsedTIme : " + str(int(endTime - startTime)) + "s")

"""
out

elapsed time for load data : 15s
회사이름 : 삼성전자(주)
연봉순위 : 1,829위
전체회사 수 : 515,827개
가입자수 : 103,139명
도로명주소 : 경기도 수원시 영통구 삼성로
예상연봉 : 59,254,189원
상위퍼센트 : 0.35%
입사 : 5,056명
퇴사 : 4,053명
elapsedTIme : 18s
"""

"""
데이터 로드 : 15s
분배 : 3s
예상 시간 : 15 + 515827 * 3 =  1547496s = 429.86h 
약 430시간..? 더 빠르게 할 수 있는 방법은 없을까?   
"""

"""
# (o) 연봉상위 몇프로인가 -> 마지막달 기준 -> orderby -> index -> index / total 전체회사 * 100
# (o) 예상평균연봉 - 마지막달 기준
# (o) 주소 - 마지막달 기준
# (o) 산업군 - 마지막달 기준
# (o) 인원 -> 마지막달 기준
# (?) 업력 -> ?
# (?) 입사 -> 신규 모두 더한다 (연기준?) -> 왜 안맞을까?.. 전체일까?
# (?) 퇴사 -> 상실 모두 더한다 (연기준?) -> 왜 안맞을까?.. 전체일까?
# (x) 동종산업군 -> 입사 or 퇴사 인원 평균
# (x) 전체기업 -> 입사 or 퇴사 인원 평균
# (x) 뉴스 -> api or parsing
# (x) 월별그래프(인원 ,평균급여)

# 추가 해볼 것
# (x) 관련기업 추천 -> 비슷한 연봉 + 비슷한 상위 or 하위 업종 + 가입자수 많은 것으로 랜덤으로 추천해줄까?
# (x) 월 별 차이를 이용한 해당 달에 들어온 사람들 예측 -> 역으로 입사한사람들의 금액을 추적할 수 있지 않을까?
# (X) 정리해서 새로운 데이터 프레임 만들기
# (X) 분석시간을 더 단축하는 방법은 없을까? 
"""

# 하면서 느낀점
# formatter 을 배워야.
# 언어 불편.
# 익숙하지 않음. -> 사용하려는 것이 항상 없다.
# 조금 더 학습이 많이 필요함.
# 더 많은 분석 예시를 보면 좋겠다.
# 더 많은 데이터를 분석해 봐야한다.
# type 안쓰고 return 타입을 바로 알 수는 없나..?
# extension이 없나..
# null처리, 에러핸들링, function 모듈화, 네이밍 규칙, log 라이브러리 등 기본적인게 힘든 상황 -> 훈련필요
