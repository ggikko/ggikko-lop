import math
import time
import pandas as pd
import json

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


def getSalary(df, company_name: str):
    find = df.loc[df['사업장명'].str.contains(company_name, regex=False)].head(1)
    if hasItem(find):
        return find["평균월급"].values[0]
    else:
        return 0


# data list
month_data_list = []
result_dict_list = []

loadStartTime = time.time()

# load data
for i in range(1, 9):
    path = "/Users/jihongpark/Documents/Week2/refined/salary_0" + str(i) + "month.csv"
    month_data_list.append(pd.read_csv(path))

loadEndTime = time.time()
print("elapsed time for load data : " + str(int(loadEndTime - loadStartTime)) + "s")

df_size = len(month_data_list)
df_last_index = df_size - 1
latest_df = month_data_list[df_last_index]
latest_df_copy = latest_df.copy()
print(latest_df_copy.info())


def addCompanyInfo(target_company):
    # condition
    find_condition = latest_df['사업장명'].str.contains(target_company, regex=False)

    # find
    find_company_row = latest_df.loc[find_condition, :].head(1)
    find_dict = find_company_row.to_dict('records')
    if not bool(find_dict):
        print("not found")
        return
    find_company = find_dict[0]
    find_company["index"] = find_company_row.index.values[0]

    test1 = time.time()

    if bool(find_company):
        # 연봉 상위 몇프로
        find_company_name = find_company["사업장명"]
        find_company_rank = find_company["index"]
        find_company_expected_salary = math.ceil(find_company["평균연봉"])
        find_company_address = find_company["도로명주소"]
        find_company_join_count = find_company["가입자수"]
        total_company_count = len(latest_df_copy)

        # join & leave
        join_total_count = 0
        leave_total_count = 0
        month_salary_total_count = 0

        for temp_df in month_data_list:
            join_total_count += getJoinCount(temp_df, target_company)
            leave_total_count += getLeaveCount(temp_df, target_company)
            month_salary_total_count += getSalary(temp_df, target_company)

        print(str(df_size))
        print(str(month_salary_total_count / (df_size - 1) * 12))

        # salary_percent
        find_percent = round((find_company_rank / total_company_count * 100), 2)

        test2 = time.time()
        print(test2 - test1)

        temp_dict = {"company": find_company_name,
                     "salary_rank": format(find_company_rank, ",") + "위",
                     "total_company": format(total_company_count, ",") + "개",
                     "total_member": format(find_company_join_count, ",") + "명",
                     "addr": find_company_address,
                     "expected_salary": format(find_company_expected_salary, ",") + "원",
                     "salary_percent": format(find_percent, ",") + "%",
                     "new_join": format(join_total_count, ",") + "명",
                     "new_leave": format(leave_total_count, ",") + "명"
                     }

        result_dict_list.append(temp_dict)
    else:
        print("not found")


json_val = json.dumps(result_dict_list, ensure_ascii=False)
print(json_val)

endTime = time.time()
print("elapsedTIme : " + str(int(endTime - startTime)) + "s")

"""
out

elapsed time for load data : 5s
회사이름 : 삼성전자(주)
연봉순위 : 1,829위
전체회사 수 : 515,827개
가입자수 : 103,139명
도로명주소 : 경기도 수원시 영통구 삼성로
예상연봉 : 59,254,189원
상위퍼센트 : 0.35%
입사 : 5,056명
퇴사 : 4,053명
elapsedTIme : 6s
"""

"""
데이터 로드 : 5s
분배 : 1s ~ 2s
예상 시간 : 5 + 515827 * 1 =  515832s = 143.28h 
약 143시간..? 더 빠르게 할 수 있는 방법은 없을까? 데이터 encoding을 해야하나    
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
# (X) 회사 검색 => 추천, 비추천, 에라 모르겠다. 


  #   Column  Non-Null Count   Dtype  
---  ------  --------------   -----  
 0   사업장명    486885 non-null  object 
 1   가입자수    490078 non-null  int64  
 2   도로명주소   490078 non-null  object 
 3   신규      490078 non-null  int64  
 4   상실      490078 non-null  int64  
 5   고지금액    490078 non-null  int64  
 6   평균월급    490078 non-null  float64
 7   평균연봉    490078 non-null  int64  
 
  #   Column  Non-Null Count   Dtype  
---  ------  --------------   -----  
 0   사업장명    490078 non-null  object 
 1   가입자수    490078 non-null  int64  
 2   도로명주소   490078 non-null  object 
 3   신규      490078 non-null  int64  
 4   상실      490078 non-null  int64  
 5   고지금액    490078 non-null  int64  
 6   평균월급    490078 non-null  float64
 7   평균연봉    490078 non-null  float64
 
 empty string
 https://stackoverflow.com/questions/29314033/drop-rows-containing-empty-cells-from-a-pandas-dataframe
 
  #   Column  Non-Null Count   Dtype  
---  ------  --------------   -----  
 0   사업장명    486885 non-null  object 
 1   가입자수    486885 non-null  int64  
 2   도로명주소   486885 non-null  object 
 3   신규      486885 non-null  int64  
 4   상실      486885 non-null  int64  
 5   고지금액    486885 non-null  int64  
 6   평균월급    486885 non-null  float64
 7   평균연봉    486885 non-null  float64 
"""

# 하면서 느낀점
# json을 만든다? 정제된 데이터 만드는 법 연습. + 여러 데이터를 보고 데이터를 describe, info, head, pivot,loc 등 뭔가 큰 데이터를 바라보는 연습을 해보면 어떨까?
# 125개를 테스트를 해봤는데 생각보다 시간이 걸림.. 모든 회사를 할 수 없다? (막힘) -> 더욱 빠른 정제된 값을 만들어야지
# 좋은회사, 보통회사, 나쁜회사? 를 구분해볼까? -> 영향을 미치는 조건들을 분석하면?
# 관련 좋은 회사를 추천해볼까? -> 인사담당자와 연결? 느낌이.. 링크드인은 이미 하고 있을 것 같다..? 이런 관련된 것들을.. 그러면.. 이미 공개된 알고리즘이나 피쳐 라벨들이 있지 않을까?
