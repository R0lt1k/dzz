for i in range(1, 100):
    response=requests.get(f'https://jsonplaceholder.typicode.com/photos/{i}')
    with open(f'./bibip/data{i}.json','w') as file:
        file.write(response.text)
