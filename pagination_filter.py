def paginate_filter(data, page, page_size, filters):

    filtered_data = []

    for item in data:
        match = True

        for key, value in filters.items():
            if key not in item or item[key] != value:
                match = False
                break

        if match:
            filtered_data.append(item)

    start = (page - 1) * page_size
    end = start + page_size

    if start >= len(filtered_data):
        return []

    return filtered_data[start:end]


data = [
{"id":1,"name":"Product A","category":"Electronics","status":"active"},
{"id":2,"name":"Product B","category":"Clothing","status":"inactive"},
{"id":3,"name":"Product C","category":"Electronics","status":"active"},
{"id":4,"name":"Product D","category":"Electronics","status":"inactive"},
{"id":5,"name":"Product E","category":"Clothing","status":"active"},
{"id":6,"name":"Product F","category":"Electronics","status":"active"}
]

page = 1
page_size = 2
filters = {"category":"Electronics","status":"active"}

result = paginate_filter(data, page, page_size, filters)

print(result)