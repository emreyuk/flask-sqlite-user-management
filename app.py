from flask import Flask, jsonify,request, g
import sqlite3
import os




app = Flask(__name__)



def get_db():
    database = 'user_db.sqlite'
    con = sqlite3.connect(database)
    con.row_factory = sqlite3.Row
    return con

def init_db():
    con = get_db()
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(id,username, email);")
    con.commit()



init_db()

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    con = get_db()
    cursor = con.cursor()
    cursor.execute('SELECT id, username, email FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    con.close()
    if user is not None:
        return jsonify({'id': user[0], 'username': user[1], 'email': user[2]})
    return jsonify({"message": "Kullanıcı bulunamadı"}), 404

@app.route('/users/<string:user_id>', methods=['DELETE'])
def del_user(user_id):
    con = get_db()
    cursor = con.cursor()
    if user_id == '-1':
        print("deneme")
        cursor.execute('DELETE FROM users WHERE id is null')
    else:
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))

    con.commit()
    con.close()
    return jsonify({"message": f"Kullanıcı ID {user_id} başarıyla silindi"}), 200

@app.route('/users', methods=['GET'])
def get_users_all():
    con = get_db()
    cursor = con.cursor()
    cursor.execute('SELECT id, username, email FROM users;')
    users = cursor.fetchall()
    con.close()
    user_list = []
    for user in users:
        user_list.append({'id': user[0], 'username': user[1], 'email': user[2]})
    
    return jsonify(user_list)


@app.route('/users', methods=['POST'])
def create_user():
    con = get_db()
    user_data = request.json
    if 'username' in user_data and 'email' in user_data:
        cursor= con.cursor()
        cursor.execute('INSERT INTO users (id,username, email) VALUES (?,?,?)', (user_data['id'],user_data['username'],user_data['email']))
        con.commit() 
        con.close()
        return jsonify ({"message": "kullanıcı başarıyla eklendi", "username": user_data['username']}),201
    else:
        return jsonify({"message": "Eksik veya Geçersiz Veri!"}),400


@app.route('/users', methods=['PATCH'])
def update_user():
    con = get_db()
    user_data = request.json
    cursor= con.cursor()
    cursor.execute("UPDATE users SET username = ?, email = ? WHERE id = ?", (user_data['username'],user_data['email'],user_data['id']))
    con.commit()
    con.close()
    return jsonify({"message": f"Kullanıcı ID {user_data['username']} başarıyla güncellendi"}), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True, threaded=False)
