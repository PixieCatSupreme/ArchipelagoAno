import json
import os.path
from typing import Any, Literal, NamedTuple
from PIL import Image

from .Data.Events import all_events, EventData, EventFlags
from .Data.Locations import all_locations
from .Data.Regions import RegionEnum, all_areas, Nexus


IsFrozen = '.apworld' in os.path.abspath(__file__)

class UTStuff:
    ut_can_gen_without_yaml = True
    found_entrances_datastorage_key = "Slot:{player}:EventMap"

    tracker_world: dict
    tracked_events: EventFlags

    player_map: type[RegionEnum]
    last_map_index: int

    def __init__(self, *args, **kwargs):
        super(UTStuff, self).__init__(*args, **kwargs)
        self.tracker_world = {
            "map_page_folder": "tracker",
            "map_page_maps": "maps.json",
            "map_page_locations": "locations.json",
            "map_page_setting_key": "Slot:{player}:MapLocation",
            "map_page_index": self.map_page_index,
            "location_setting_key": "Slot:{player}:MapLocation",
            "location_icon_coords": self.location_icon_coords,
            "map_page_groups": [("Maps", [(m["name"],m["name"]) for m in BaseMaps])]
        }
        self.player_map = Nexus
        self.last_map_index = 0
        if IsFrozen:
            self.tracker_world.update({
                "external_pack_key": "ut_tracker_path",
                "ut_dialog_name": "Select Anodyne's Universal Tracker Pack"
            })

    def ut_event_check(self, event:EventData):
        return lambda _: event.flag in self.tracked_events

    def reconnect_found_entrances(self, key:str, value:Any):
        if key.endswith("EventMap") and isinstance(value,int):
            self.tracked_events = EventFlags(value)

    def map_page_index(self,coords: dict[str, int] | Literal[""] | None):
        if not isinstance(coords, dict):
            return 0
        self.player_map = all_areas[coords.get("Map",0)]
        return {
            area['name']: index
            for index, area in enumerate(BaseMaps)
        }[self.player_map.area_name()]

    def location_icon_coords(self, index: int, coords: dict[str, int] | Literal[""] | None) -> tuple[int, int, str] | None:
        """Converts player coordinates provided by the game mod into image coordinates for the map page."""
        print("location called")
        if not isinstance(coords,dict):
            self.last_map_index = index
            # Initial call with empty string or no player yet
            return None

        game_region = all_areas[coords.get("Map",0)]
        self.player_map = game_region
        ut_map:str = BaseMaps[index]["name"]

        if ut_map=="Nexus" and game_region is not Nexus:
            # Nexus
            return game_region.nexus_ut_loc()[0], game_region.nexus_ut_loc()[1], f"images/icons/young_player.png"

        if ut_map != game_region.area_name():
            return None

        return coords.get("X", 0) * 160 + 80 + game_region.ut_map_offset()[0], coords.get("Y", 0) * 160 + 80 + game_region.ut_map_offset()[1], f"images/icons/young_player.png"

class MapVariant(NamedTuple):
    mapName: str
    image_path:str
    is_split:bool
    is_swap:bool

class MapData(NamedTuple):
    has_split:bool

    def variants(self,region:type[RegionEnum]):
        ret = [MapVariant(region.area_name(),f"images/maps/{region.__name__.upper()}.png",False,False)]
        if self.has_split:
            ret.append(MapVariant(f"{region.area_name()}:Split",f"images/maps/generated/{region.__name__.upper()}_Split.png",True,False))
        return ret

def map_images():
    ret: dict[type[RegionEnum], MapData] = {}
    for region in all_areas:
        ret[region] = MapData(region is not Nexus)
    return ret

all_mapdata = map_images()

def make_map():
    return sorted([{
        "name": variant.mapName,
        "img": variant.image_path,
        "location_size": 20,
        "location_border_thickness": 1
    } for area,mapdata in all_mapdata.items() for variant in mapdata.variants(area)], key=lambda d: 0 if d["name"].startswith("Nexus") else 1)

BaseMaps = make_map()


######
# Source distribution only functions
#####

class ImageOffsetData(NamedTuple):
    map_offset: tuple[int,int]
    nexus_offset: tuple[int,int]

def gen_images(img_dir:str) -> dict[type[RegionEnum],ImageOffsetData]:
    nexus = Image.open(os.path.join(img_dir,'images/maps/NEXUS.png'))
    ret = {}
    for area,mapdata in all_mapdata.items():
        if area is Nexus:
            continue
        base_image = Image.open(os.path.join(img_dir,f'images/maps/{area.__name__.upper()}.png'))
        image_width,image_height = base_image.size
        if image_height > nexus.height:
            image_offset = 0
            nexus_offset = (image_height - nexus.height)//2
        else:
            image_offset = (nexus.height - image_height)//2
            nexus_offset = 0
        ret[area] = ImageOffsetData((0,image_offset),(image_width,nexus_offset))
        for variant in mapdata.variants(area):
            if not variant.is_swap and not variant.is_split:
                continue
            if variant.is_split:
                combined = Image.new('RGBA',(image_width+nexus.width,max(image_height,nexus.height)))
                combined.paste(base_image,(0,image_offset))
                combined.paste(nexus,(image_width,nexus_offset))
                combined.save(os.path.join(img_dir,variant.image_path))
    return ret

def location_data(offset_data:dict[type[RegionEnum],ImageOffsetData]):
    all_locs: dict[type[RegionEnum], dict[tuple[int, int], list[str]]] = {}

    for location in all_locations:
        all_locs.setdefault(location.region.__class__, {}).setdefault(location.tracker_loc, []).append(location.name)
        if location.region.__class__ is not Nexus:
            all_locs.setdefault(Nexus, {}).setdefault(location.region.nexus_ut_loc(), []).append(location.name)

    for event in all_events:
        all_locs.setdefault(event.region.__class__, {}).setdefault(event.tracker_loc, []).append(event.name)
        if event.region.__class__ is not Nexus:
            # Move event overviews a bit to the left in the nexus overview so they don't overlap
            loc = event.region.nexus_ut_loc()
            loc = (loc[0] - 25, loc[1])
            all_locs.setdefault(Nexus, {}).setdefault(loc, []).append(event.name)

    def variant_loc(map_loc:tuple[int,int],variant:MapVariant, offset:ImageOffsetData):
        if variant.is_split:
            return {"map":variant.mapName,"x":offset.map_offset[0]+map_loc[0], "y": offset.map_offset[1]+map_loc[1]}
        return {"map":variant.mapName,"x":map_loc[0], "y": map_loc[1]}

    base = [{
        "name": region.area_name(),
        "children": [
            {
                "name": region.area_name(),
                "map_locations": [variant_loc(map_loc,variant,offset_data[region] if region is not Nexus else None) for variant in all_mapdata[region].variants(region)],
                "sections": [{"name": name} for name in names]
            }
            for map_loc, names in map_locs.items()
        ]
    } for region, map_locs in all_locs.items()]

    for region, mapdata in all_mapdata.items():
        if region is Nexus:
            continue
        offset = offset_data[region].nexus_offset
        for variant in mapdata.variants(region):
            if not variant.is_split:
                continue
            base.append({
                "name": f"Nexus-{region.area_name()} split",
                "children": [
                    {
                        "name": region.area_name(),
                        "map_locations": [{"map":variant.mapName,"x":map_loc[0]+offset[0],"y":map_loc[1]+offset[1]}],
                        "sections": [{"name": name} for name in names]
                    }
                    for map_loc,names in all_locs[Nexus].items()
                ]
            })
    return base



if not IsFrozen:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(base_dir, 'tracker/maps.json'), 'w', encoding='utf-8') as f:
        json.dump(make_map(), f, ensure_ascii=True, indent=4)
    offset_data = gen_images(os.path.join(base_dir,'tracker'))
    with open(os.path.join(base_dir, 'tracker/locations.json'), 'w', encoding='utf-8') as f:
        json.dump(location_data(offset_data), f, ensure_ascii=True, indent=4)
