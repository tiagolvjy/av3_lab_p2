def add_cart(conexao, user_id, skin_name, price):
    cursor = conexao.cursor()

    sql = f"INSERT INTO cart (user_id, skin_name, price) VALUES (?, ?, ?)"
    cursor.execute(sql, [user_id, skin_name, price])
    conexao.commit()
    print("Skin adicionada ao carrinho de compras!")

    return cursor.fetchall()

def list_cart(conexao, user_id):
    cursor = conexao.cursor()
    sql = f"SELECT * FROM cart WHERE user_id = ?"
    cursor.execute(sql, [user_id])
    skins = cursor.fetchall()

    if skins:
        for skin in skins:
            print(f"Skin: {skin[2]}, Preço: {skin[3]}")
    else:
        print("Seu carrinho de compras está vazio. :(")

def edit_cart(conexao, user_id, new_price, skin_id):
    sql = f"UPDATE cart SET price = ? WHERE skin_id = ? AND user_id = ?"
    cursor = conexao.cursor()
    cursor.execute(sql, [new_price, skin_id, user_id])

    if cursor.rowcount > 0:
        print("Skin atualizada com sucesso! >:)")
    else:
        print("Você não possui uma skin com esse ID no carrinho de compras. =C")

    conexao.commit()

def del_cart(conexao, user_id, skin_id):
    sql = f"DELETE FROM cart WHERE skin_id = ? AND user_id = ?"
    cursor = conexao.cursor()
    cursor.execute(sql, [skin_id, user_id])

    if cursor.rowcount > 0:
        print("Skin removida com sucesso!")
    else:
        print("Você não possui uma skin com esse ID no seu carrinho de compras.")

    conexao.commit()

def search_skin(conexao, user_id, skin_busca):
    sql = f"SELECT * FROM cart WHERE skin_name LIKE ? AND user_id = ?"
    cursor = conexao.cursor()
    cursor.execute(sql,['%' + skin_busca + '%', user_id])
    skins = cursor.fetchall()

    if skins:
        for skin in skins:
            print(f"Skin: {skin[2]}, Preço: {skin[3]}")
    else:
        print("Nenhuma skin correspondente encontrada.")

    conexao.commit()