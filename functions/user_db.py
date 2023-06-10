def register(conexao, username, password):
    cursor = conexao.cursor()

    sql = f"INSERT INTO users (username, password) VALUES (?, ?)"
    cursor.execute(sql, [username, password])
    conexao.commit()
    print("Usuário cadastrado com sucesso! :)")

    return cursor.fetchall()

def login(conexao, username, password):
    cursor = conexao.cursor()

    sql = f"SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(sql, [username, password])
    conexao.commit()

    user = cursor.fetchone()

    if user:
        print("Login bem-sucedido! :)")
        return user[0]
    else:
        print("Nome de usuário ou senha incorretos.")
        return None