from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):
    "Locust任务集，定义每个lucost的行为"
    @task(1)                    # 任务的权重为1，如果有多个任务，可以将权重值定义成不同的值
    def index(self):
        "模拟发送数据"
        body = {
            "user_name" : "xuzhao_test001",
            "product_price" : "100",
            "product_discount" : "0.5"
        }
        response = self.client.get("/query_account_get_test")
        print(response)
        if not response.ok:
            print(response.text)
            response.failure('Got wrong response')

class WebsiteUser(HttpLocust):
    """自定义Locust类，可以设置Locust的参数。"""
    task_set = WebsiteTasks
    host = "http://127.0.0.1:8000/"          # 被测服务器地址
    min_wait = 1000                         # 最小等待时间，即至少等待多少秒后Locust选择执行一个任务。
    max_wait = 5000                         # 最大等待时间，即至多等待多少秒后Locust选择执行一个任务。
