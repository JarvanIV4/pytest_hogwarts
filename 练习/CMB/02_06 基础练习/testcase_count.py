"""
总体描述：
请编写一个Python类，提供两个公有方法分别实现以下功能（请合理规划方法粒度，通过私有方法进行拆分）：
1）输入自动化案例的执行记录execute_records和当前日期current_date，输出过去30天的执行成功率；
2）输入自动化基础案例执行集列表basic_testsets和项目案例执行集列表project_testsets，输出基础执行集和项目执行集之间的重复案例列表；

名词解释：
过去30天执行成功的案例数：在过去30天（包含当前日期），执行成功至少一次的案例数量
过去30天执行总案例数：在过去30天（包含当前日期），执行过的案例数量（需要去重）
基础执行集和项目执行集之间的重复案例列表：同时出现在基础执行集和项目执行集中的案例

计算公式：
过去30天的执行成功率 = 过去30天执行成功的案例数 / 过去30天执行总案例数
"""
import datetime
class TestCaseData:

    def __start_date(self, current_date, delta_date=-29):
        """
        计算执行时间前29天的日期
        :param current_date: 执行时间
        :param delta_date: 当前日期偏差天数
        :return: 返回当前日期前N（默认前29）天的日期
        """
        current_date = datetime.datetime.strptime(current_date, "%Y-%m-%d")  # 将字符串转换为时间格式
        delta = datetime.timedelta(days=delta_date)    # 当前日期前29天的日期偏差值
        start_date = (current_date + delta).strftime("%Y-%m-%d")  # 计算当前日期前29天的日期
        return start_date

if __name__ == '__main__':
    t = TestCaseData()



"""
第一个功能参数示例：
execute_records：
[
  {
"执行集名": "testest-001",
"执行时间": "2019-11-05",
    "执行结果": [
      {
        "案例名": "test-001",
        "状态": "成功"
      },
      {
        "案例名": "test-002",
        "状态": "失败"
      },
      {
        "案例名": "test-003",
        "状态": "失败"
      }
    ]
  },
  {
"执行集名": "testest-001",
"执行时间": "2019-11-12",
    "执行结果": [
      {
        "案例名": "test-001",
        "状态": "成功"
      },
      {
        "案例名": "test-002",
        "状态": "成功"
      },
      {
        "案例名": "test-003",
        "状态": "失败"
      },
      {
        "案例名": "test-004",
        "状态": "成功"
      }
    ]
  },
  {
"执行集名": "testest-002",
"执行时间": "2019-10-16",
    "执行结果": [
      {
        "案例名": "test-003",
        "状态": "成功"
      },
      {
        "案例名": "test-005",
        "状态": "失败"
      }
    ]
  },
  {
"执行集名": "testest-003",
"执行时间": "2019-10-28",
    "执行结果": [
      {
        "案例名": "test-006",
        "状态": "成功"
      },
      {
        "案例名": "test-007",
        "状态": "成功"
      },
      {
        "案例名": "test-008",
        "状态": "失败"
      }
    ]
  }
]

current_date：
"2019-11-15"

输出：
"71.4%"

第二个功能参数示例：
basic_testsets：
[
  {
    "执行集名": "basic-testset-001",
"案例列表": [
  "test-001",
  "test-002",
  "test-003",
  "test-004",
  "test-005"
    ]
  },
  {
    "执行集名": "basic-testset-002",
"案例列表": [
  "test-001",
  "test-002",
  "test-006",
  "test-007",
  "test-008"
    ]
  },
  {
    "执行集名": "basic-testset-003",
"案例列表": [
  "test-009",
  "test-010"
    ]
  }
]
project_testsets：
[
  {
    "执行集名": "project-testset-001",
"案例列表": [
  "test-001",
  "test-003",
  "test-011",
  "test-012"
    ]
  },
  {
    "执行集名": "project-testset-002",
"案例列表": [
  "test-008",
  "test-010",
  "test-012",
  "test-013",
  "test-014"
    ]
  },
  {
    "执行集名": "project-testset-003",
"案例列表": [
  "test-013",
  "test-014",
  "test-015"
    ]
  }
]

输出：
[
  "test-001",
  "test-003",
  "test-008",
  "test-010"
]
"""