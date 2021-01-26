from connection import RedisConnection


def user_auth(conn, user):
    if not conn.get_user_auth(user):
        while True:
            password = input('Input password: \n')
            if conn.auth(user, password):
                break
            else:
                print('Access denied')


def todolist_work(conn, user, tasks):
    print('WELCOME TO TODO-LIST!!!')
    while conn.get_user_auth(user):
        print('Enter ADD "task_name" to add new task')
        print('Enter DEL "task_name" to delete task')
        print('Your tasks: ', tasks)
        input_raw = input()
        command, task_name = input_raw.split()
        if command == 'ADD':
            tasks.append(task_name)
        elif command == 'DEL':
            if task_name in tasks:
                tasks.remove(task_name)
        else:
            print(f'Wrong command {command}...')
    return tasks


def main(conn, user):
    tasks = []
    while True:
        user_auth(conn, user)
        tasks = todolist_work(conn, user, tasks)


if __name__ == '__main__':
    connection = RedisConnection(host='0.0.0.0', port=6379, db=0)
    username = input('Input username: \n')
    main(connection, username)
