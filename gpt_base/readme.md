## 7/27 语义向量化层工作汇报

**工作进展：**
初步实现api接口文档的向量化和与用户输入语句的匹配

**结果示例：**
- "qurey": "发起一个机器人任务请求,调用哪个接口?"
"response": "The interface to use for initiating a robot task request is "robot_task_request"  
   
-    "qurey": "操控机器人需要哪些接口"
"response": "The interfaces needed to control the robot are: \n1. pickup_and_dropoff: Used to control the robot for picking up and transferring specific items.\n2.robot_task_request: Used to request a robot task and assign it to a specific robot for execution.\n3. robot_task_response: Used to describe the response format for a robot task request.\n4. ApiRequest.msg: Used to send task requests to the server."

**技术原理：**
将每个api接口分别作为单个文档，使用"text-embedding-ada-002"模型进行向量化，并持久化存储。得到用户输入语句并embedding后进行匹配，得到结果。