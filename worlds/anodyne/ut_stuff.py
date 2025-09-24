import json
import os.path

from .Data.Regions import all_areas

UTTrackerData = {
    "map_page_folder": "tracker",
    "map_page_maps": "maps.json",
    "map_page_locations": "locations.json"
}

def make_map():
    return [{
        "name": area.area_name(),
        "img": f"images/maps/{area.__name__.upper()}.png",
        "location_size": 30
    } for area in all_areas]

def location_data():
    return [{
    "name": "Nexus",
    "children": [
      {
        "name": "Apartment",
        "sections": [
          {"name": "Apartment - 1F Ledge Chest"},
          {"name": "Apartment - 1F Rat Maze Chest"}
        ],
        "map_locations": [{"map": "Nexus", "x": 592, "y": 833}]
      },
      {
        "name": "Street",
        "sections": [
          {"name": "Street - Broom Chest"}
        ],
        "map_locations": [{"map": "Nexus","x": 256,"y": 897}]
      }
    ]
  }]

if '.apworld' not in os.path.abspath(__file__):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(base_dir,'tracker/maps.json'),'w',encoding='utf-8') as f:
        json.dump(make_map(), f, ensure_ascii=True, indent=4)
    with open(os.path.join(base_dir,'tracker/locations.json'),'w',encoding='utf-8') as f:
        json.dump(location_data(),f,ensure_ascii=True,indent=4)