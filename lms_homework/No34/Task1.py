import requests

request = requests.get('https://uk.wikipedia.org/wiki/Artemis_1')

if request.ok:
    print(f"Connecting successfully with status: {request.status_code}")
    data = request.text

    last = 0
    while True:
        start = data[last:].find('<p>')
        end = data[last:].find('</p>')

        with open('download.txt', 'a') as f:
            f.write(data[start:end])

        if end == 0:
            break
        last = end
        print("-> Add row")
    print("Finally!")

else:
    print(f"Error {request.status_code}")
