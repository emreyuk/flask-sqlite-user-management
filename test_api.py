import requests
import base64


url = "http://localhost:8888"




# Yeni bir kullanıcı eklemek için POST isteği yapma örneği
def create_user(id,username, email):
    user_data = {'id': id,'username': username, 'email': email}
    response = requests.post(f'{url}/users', json=user_data)
    return response

# Belirli bir kullanıcıyı GET isteği ile sorgulama örneği
def get_user(user_id):
    response = requests.get(f'{url}/users/{user_id}')
    return response

def get_users_all():
    response = requests.get(f'{url}/users')
    return response


def del_user(user_id):
    response = requests.delete(f'{url}/users/{user_id}')
    return response


def update_user(user_id,user_name,email):
    user_data = {'id': user_id,'username': user_name, 'email': email}
    response = requests.patch(f'{url}/users', json = user_data)
    return response


#def convert_image_to_base64(frame):
    # print("converting image to base64..")
    
    # retval, buffer = cv2.imencode('.jpg', frame)
    # return base64.b64encode(buffer).decode('utf-8')



# Örnek bir base64 kodlu görüntü oluşturun (örneğin, 'image.jpg' yerine gerçek bir görüntünün yolunu kullanın)
with open('image.jpg', 'rb') as image_file:
    #base64_image = convert_image_to_base64(image_file)
    base64_image = base64.b64encode(image_file.read()).decode()
    

# JSON verisi oluşturun ve POST isteği yapın
data = {'service_img': base64_image}

response = requests.post(f'{url}/save_image', json=data)

print(response.status_code)
try:

    print(response.json())
except:
    print(response.text)


ocr_results = response.json()['extracted_text']








# get_response = update_user("1","ugurdoktur","ugurdoktur2@yapayzeka.co")
# print(get_response.status_code)
# print(get_response.text)

# get_response_all = get_users_all()
# print(get_response_all.status_code)
# print(get_response_all.json())

# # Yeni kullanıcı eklemek için POST isteği yapma
# create_response = create_user("1","ugur", "ugur@example.com")
# print("Create User Response:")
# print(create_response.status_code)
# print(create_response.json())

# # Belirli bir kullanıcıyı sorgulama
# user_id = 1  
# get_response = get_user(user_id)
# print("Get User Response:")
# print(get_response.status_code)
# print(get_response.json())
# get_response = del_user(-1)
# print(get_response.status_code)
# print (get_response.json())


# get_response_all = get_users_all()
# print(get_response_all.status_code)
# print(get_response_all.json())

# POST isteği örneği
#data = {'item': 'emore'}  # Eklenecek öğe
#response = requests.post(url, json=data)
#print("\nPOST Response:")
#print(response.status_code)  # İstek durum kodu
#print(response.json())       # Yanıt verisi (JSON)

#response2 = requests.get(url)
#print("\nUpdated GET Response:")
#print(response2.status_code)  # İstek durum kodu
#print(response2.json())       # Yanıt verisi (JSON)


# DELETE isteği ile bir öğeyi silme örneği
#item_to_delete = 'emre'  # Silinecek öğe
#delete_url = f'{url}/{item_to_delete}'

#response = requests.delete(delete_url)
#try:
#    print("DELETE Response:")
#    print(response.status_code)  # İstek durum kodu
#    print(response.json())       # Yanıt verisi (JSON)
#except:
#    print("exception occured")
#    print(response.text)
# Listeyi tekrar GET ile alarak güncellemeyi kontrol edebilirsiniz
#response = requests.get(url)
#print("\nUpdated GET Response:")
#print(response.status_code)  # İstek durum kodu
#print(response.json())       # Yanıt verisi (JSON)


#item_to_pick = 'ali'
#pick_url=f'{url}/{item_to_pick}'
#response = requests.get(pick_url)

#print("GET Response:")
#print(response.text)
#output = response.json()
#print(output["item"])

#nonexistent_item = 'karpuz'  # Var olmayan bir öğe
#nonexistent_url = f'{url}/{nonexistent_item}'

#response = requests.get(nonexistent_url)
#print("\nNonexistent GET Response:")
#print(response.status_code)  # İstek durum kodu
#print(response.json())       # Yanıt verisi (JSON)



#add_new_user = {'username':'hayrettin'}
#adding_url = f'{url}/users'
#response = requests.post(adding_url,json = add_new_user)
#print(response.text)
#print(response.status_code)
#print(response.json())


#base_url = f'{url}/users'
#response = requests.get(base_url)
# print("Users before PATCH:")
# print(response.json())
# user_to_update = 'emre'
# new_username = 'pervettin'

# update_data = {'new_username':new_username}

# update_url = f'{base_url}/{user_to_update}'

# response = requests.patch(update_url, json = update_data)

# print("Response:")
# print(response.status_code)
# print(response.json())



# response = requests.get(base_url)
# print("Users after PATCH:")
# print(response.json())