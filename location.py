import folium


def generate_map(users_data):
    m = folium.Map(location=[45.5236, 22.6750],
                   zoom_start=3, tiles='Stamen Terrain')
    for user, v in users_data.items():
        folium.Marker(v['location'], popup=f"<img src='{v['image']}' \
         alt='Avatar' style='height:20px; width:20px'>",
                      tooltip=user).add_to(m)
    m.save('templates/temp.html')
    with open('templates/temp.html', 'r') as file:
        htmls = file.read()
    return htmls


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
