from . import AnodyneTestBase
from ..Data import Locations,Regions

class TestData(AnodyneTestBase):
    run_default_tests = False

    def test_consistent_region_names(self):
        for loc_region in Locations.locations_by_region:
            self.assertIn(loc_region,Regions.all_regions,"Location region not a real region")