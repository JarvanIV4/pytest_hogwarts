import datetime
class TestCaseInfo():
    def __init__(self):
        pass

    def __satrt_date(self,current_date):
        current_date = datetime.datetime.strptime(current_date, '%Y-%m-%d')
        delta = datetime.timedelta(days=-29)
        start_date = current_date + delta
        start_date = start_date.strftime('%Y-%m-%d')
        return start_date

    def testcase_suc_rate(self,execute_records,current_date):
        execute_suc_count=0
        execute_suc_list=[]
        execute_all_count=0
        execute_all_list=[]
        start_date=self.__satrt_date(current_date)
        for execute_record in execute_records:
            execute_date=execute_record["执行时间"]
            # print(start_date,current_date)
            print(execute_record)
            if start_date<=execute_date and execute_date<=current_date:
                execute_results=execute_record["执行结果"]
                for execute_result in execute_results:
                    if execute_result["状态"]=="成功" and execute_result["案例名"] not in execute_suc_list:
                        execute_suc_count+=1
                        execute_suc_list.append(execute_result["案例名"])
                    if execute_result["案例名"] not in execute_all_list:
                        execute_all_count+=1
                        execute_all_list.append(execute_result["案例名"])
        #print(execute_suc_count,execute_all_count)
        execute_suc_rate=('%.1f%%' % (execute_suc_count/execute_all_count*100))
        return execute_suc_rate

    def __testcase_list(self,testsets):
        all_test_list=[]
        for test_set in testsets:
            test_list=test_set["案例列表"]
            for test in test_list:
                if test not in all_test_list:
                    all_test_list.append(test)
        return all_test_list

    def dupli_test_list(self,basic_testsets,project_testsets):
        basic_test_set=set(self.__testcase_list(basic_testsets))
        project_test_set=set(self.__testcase_list(project_testsets))
        dupli_set=basic_test_set & project_test_set
        dupli_all_test_list=list(dupli_set)
        dupli_all_test_list.sort()
        return dupli_all_test_list




execute_records=[
        {
            "执行集名": "testest-001",
            "执行时间": "2019-11-05",
            "执行结果": [
                {
                    "案例名": "src-001",
                    "状态": "成功"
                },
                {
                    "案例名": "src-002",
                    "状态": "失败"
                },
                {
                    "案例名": "src-003",
                    "状态": "失败"
                }
            ]
        },
        {
            "执行集名": "testest-001",
            "执行时间": "2019-11-12",
            "执行结果": [
                {
                    "案例名": "src-001",
                    "状态": "成功"
                },
                {
                    "案例名": "src-002",
                    "状态": "成功"
                },
                {
                    "案例名": "src-003",
                    "状态": "失败"
                },
                {
                    "案例名": "src-004",
                    "状态": "成功"
                }
            ]
        },
        {
            "执行集名": "testest-002",
            "执行时间": "2019-10-16",
            "执行结果": [
                {
                    "案例名": "src-003",
                    "状态": "成功"
                },
                {
                    "案例名": "src-005",
                    "状态": "失败"
                }
            ]
        },
        {
            "执行集名": "testest-003",
            "执行时间": "2019-10-28",
            "执行结果": [
                {
                    "案例名": "src-006",
                    "状态": "成功"
                },
                {
                    "案例名": "src-007",
                    "状态": "成功"
                },
                {
                    "案例名": "src-008",
                    "状态": "失败"
                }
            ]
        }
    ]

basic_testsets=[
  {
    "执行集名": "basic-testset-001",
"案例列表": [
  "src-001",
  "src-002",
  "src-003",
  "src-004",
  "src-005"
    ]
  },
  {
    "执行集名": "basic-testset-002",
"案例列表": [
  "src-001",
  "src-002",
  "src-006",
  "src-007",
  "src-008"
    ]
  },
  {
    "执行集名": "basic-testset-003",
"案例列表": [
  "src-009",
  "src-010"
    ]
  }
]
project_testsets=[
  {
    "执行集名": "project-testset-001",
"案例列表": [
  "src-001",
  "src-003",
  "src-011",
  "src-012"
    ]
  },
  {
    "执行集名": "project-testset-002",
"案例列表": [
  "src-008",
  "src-010",
  "src-012",
  "src-013",
  "src-014"
    ]
  },
  {
    "执行集名": "project-testset-003",
"案例列表": [
  "src-013",
  "src-014",
  "src-015"
    ]
  }
]


current_date="2019-11-15"
testCaseInfo=TestCaseInfo()
print(testCaseInfo.testcase_suc_rate(execute_records,current_date))
print(testCaseInfo.dupli_test_list(basic_testsets,project_testsets))