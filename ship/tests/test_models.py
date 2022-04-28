from django.test import TestCase
from ..models import Ship
from mothership.models import Mothership
from django.conf import settings

class ShipTest(TestCase):
    def setUp(self) -> None:
        Mothership.objects.create(name='TesMother')
        mship=Mothership.objects.get(name='TesMother')
        Ship.objects.create(name='Ship_Veracious', mship=mship)
        
    def test_ship_crew(self):
        ship1 = Ship.objects.get(name='Ship_Veracious')
        crew = ship1.crew_member.count()
        self.assertEqual(crew, int(settings.SHIP_CREW) )
        
        