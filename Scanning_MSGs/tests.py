import folium


def inline_map(m, width=650, height=500):
    """Takes a folium instance and embed HTML."""
    m._build_map()
    srcdoc = m.HTML.replace('"', '&quot;')
    embed = HTML('<iframe srcdoc="{}" '
                 'style="width: {}px; height: {}px; '
                 'border: none"></iframe>'.format(srcdoc, width, height))
    return embed


width, height = 650, 500
radars = folium.Map(location=[40, -122], zoom_start=5,
                    tiles='OpenStreetMap', width=width, height=height)

locations = {}
for name, location in locations.items():
    radars.simple_marker(location=location, popup=name)

inline_map(radars)

