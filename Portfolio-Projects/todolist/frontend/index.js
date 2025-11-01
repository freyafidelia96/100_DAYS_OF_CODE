
function fetchTodosFromAPI() {
    fetch('http://127.0.0.1:5000/todos', {
        method: 'GET',
        mode: 'no-cors',
    }).then(function (response) {
        console.log({ response })
        return response.text();
    }).then(function (data) {
        console.log(data);
    })
}

fetchTodosFromAPI();

function loadTodos() {
    const data = [
        {
            "created_at": "2024-12-01 16:52:02",
            "description": "cook beans and plantain",
            "done": false,
            "due_date": "2024-12-02 00:00:00",
            "id": 2,
            "title": "Cook beans"
        },
        {
            "created_at": "2024-12-01 16:52:02",
            "description": "discuss life",
            "done": false,
            "due_date": "2024-12-02 00:00:00",
            "id": 3,
            "title": "Join google meet"
        },
        {
            "created_at": "2024-12-01 16:42:42",
            "description": "Kiss him by 2:00",
            "done": false,
            "due_date": "2024-10-16 00:00:00",
            "id": 1,
            "title": "Kiss Joseph"
        }
    ];


    let html = '';
    for (let i = 0; i < data.length; i++) {
        const todo = data[i];
        html = html + `
            <div class="todo-list-item">
                <h4 class="todo-title">${todo.title}</h4>
                <p class="todo-description">${todo.description}</p>
                Due date: <span class="todo-due-date">${todo.due_date}</span>
            </div>
        `;
    }

    const todoListWrapper = document.querySelector('.todo-list-wrapper');
    todoListWrapper.innerHTML = html;
}

loadTodos()