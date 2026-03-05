def paginate_filter_sort(data, page, page_size, filters, sort_by, order):

    filtered_data = []

    for item in data:
        match = True

        for key, value in filters.items():
            if item[key] != value:
                match = False
                break

        if match:
            filtered_data.append(item)

    reverse = True if order == "desc" else False

    filtered_data.sort(key=lambda x: x[sort_by], reverse=reverse)

    start = (page - 1) * page_size
    end = start + page_size

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
page_size = 3


filters = {"category":"Electronics","status":"active"}


sort_by = input("Enter field to sort by (id/name/category/status): ")
order = input("Enter order (asc/desc): ")


result = paginate_filter_sort(data, page, page_size, filters, sort_by, order)


print("\nResult:")
for item in result:
    print(item)
