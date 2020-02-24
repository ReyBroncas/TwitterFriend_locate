import folium


def generate_map(users_data):
    m = folium.Map(location=[45.5236, 22.6750],
                   zoom_start=3, tiles='Stamen Terrain')
    for user, v in users_data.items():
        folium.Marker(v['location'], popup=f"<img src='{v['image']}' \
         alt='Avatar' style='height:20px; width:20px'>",
                      tooltip=user).add_to(m)
    htmls = m.get_root().render()
    return htmls


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
