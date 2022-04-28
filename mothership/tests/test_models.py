from django.test import TestCase
from ..models import Mothership
from django.conf import settings

class MothershipTest(TestCase):
    def setUp(self) -> None:
        Mothership.objects.create(name='TesMother')
        
    def test_ship(self):
        mship1 = Mothership.objects.get(name='TesMother')
        ships = mship1.ships.count()
        ship_no = int(settings.SHIP_CREW)
        self.assertEqual(ships, ship_no)
        
    def test_ship_crew(self):
        mship1 = Mothership.objects.get(name='TesMother')
        ship1 = mship1.ships.get(pk=1).crew_member.count()
        self.assertEqual(ship1, int(settings.SHIP_CREW) )
        
        