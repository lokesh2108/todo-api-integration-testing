# Request library lets us intract with http directly from python
import requests
import uuid # Universally unique identifier

ENDPOINT = "https://todo.pixegami.io"

# response = requests.get(ENDPOINT)
# print(response)

# # actually response will have more information like header, body and more.
# data = response.json()
# print(data)

# status_code= response.status_code
# print(status_code)


    
def test_can_create_task():
    # payload is the requets body that needs an schema 
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    data = create_task_response.json()
    
    
    task_id = data['task']['task_id']
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]
   
def test_can_update_task():
    # create the task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    task_id = create_task_response.json()['task']['task_id']
    
    # update the task
    new_payload= {
        "user_id" : payload["user_id"],
        "task_id" : task_id,
        "content" : "my updated content",
        "is_done" : True,
    }
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200
    
    # get and validate the changes
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]    

def test_can_list_tasks():
    # create n tasks
    n = 3
    payload = new_task_payload()
    for _ in range(n):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200
    
    # list tasks and check that there are 3 items
    user_id = payload["user_id"]
    list_task_response = list_tasks(user_id)
    assert list_task_response.status_code == 200
    data = list_task_response.json()
    tasks = data["tasks"]
    assert len(tasks) == n
    print(data)

def test_can_delete_task():
    # create task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]
    
    # delete Task
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200
    
    
    # Get the task and check that it's not found
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404
    

def create_task(payload):
    return requests.put(ENDPOINT + "/create-task",json= payload)

def update_task(payload):
    return requests.put(ENDPOINT + "/update-task",json= payload)

def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def list_tasks(user_id):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")

def delete_task(task_id):
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}")

def new_task_payload():
    user_id = f"test_user_{uuid.uuid4().hex}"  # .hex is used to represent in hexadecimal
    content = f"test_content_{uuid.uuid4().hex}" 
    return {
        "content": content,
        "user_id": user_id,
        "is_done": False
    }