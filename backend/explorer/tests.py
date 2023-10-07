from django.test import TestCase
from explorer.models import Oilfield, OperationalUnit, Well

from explorer.services import process_data_challenge1, process_data_challenge2

class Challenge1TestCase(TestCase):
    def setUp(self):
        self.opunit1 = OperationalUnit.objects.create(id=1, name="Unidade operacional 6")
        self.opunit2 = OperationalUnit.objects.create(id=2, name="Unidade operacional 7")
        self.oilfield1 = Oilfield.objects.create(id=1, name="Campo 1", operational_unit=self.opunit1)
        self.oilfield2 = Oilfield.objects.create(id=2, name="Campo 2", operational_unit=self.opunit1)
        self.well1 = Well.objects.create(id=1, name="Poço 1", oilfield=self.oilfield1)

    def test_process_data_challenge1(self):
        """Describe the test"""
        opunits = OperationalUnit.objects.all()
        oilfields = Oilfield.objects.all()
        wells = Well.objects.all()
        result = [
            [["opunit/1"]],
            [["opunit/2"]],
            [["opunit/1"], ["oilfield/1"]],
            [["opunit/1"], ["oilfield/2"]],
            [["opunit/1"], ["oilfield/1"], ["well/1"]]
        ]
        
        self.assertEqual(process_data_challenge1(opunits, oilfields, wells), result)

class Challenge2TestCase(TestCase):
    def setUp(self):
        self.opunit1 = OperationalUnit.objects.create(name="Unidade operacional 1")
        self.opunit2 = OperationalUnit.objects.create(name="Unidade operacional 2")
        self.opunit3 = OperationalUnit.objects.create(name="Unidade operacional 3")

        self.oilfield1 = Oilfield.objects.create(name="Campo 1", operational_unit=self.opunit1)
        self.oilfield2 = Oilfield.objects.create(name="Campo 2", operational_unit=self.opunit3)

        self.well1 = Well.objects.create(name="Poço 1", oilfield=self.oilfield1)
        self.well2 = Well.objects.create(name="Poço 2", oilfield=self.oilfield1)
        self.well3 = Well.objects.create(name="Poço 3", oilfield=self.oilfield2)

    def test_process_data_challenge2(self):
        """Describe the test"""
        opunits = OperationalUnit.objects.all()
        oilfields = Oilfield.objects.all()
        wells = Well.objects.all()

        result = [
            {
                "id": self.opunit1.id,
                "name": "Unidade operacional 1",
                "children": [
                    {
                        "id": self.oilfield1.id,
                        "name": "Campo 1",
                        "children": [
                            {"id": self.well1.id, "name": "Poço 1"},
                            {"id": self.well2.id, "name": "Poço 2"},
                        ],
                    }
                ],
            },
            {
                "id": self.opunit2.id,
                "name": "Unidade operacional 2",
            },
            {
                "id": self.opunit3.id,
                "name": "Unidade operacional 3",
                "children": [
                    {
                        "id": self.oilfield2.id,
                        "name": "Campo 2",
                        "children": [
                            {"id": self.well3.id, "name": "Poço 3"},
                        ],
                    }
                ],
            },
        ]

        self.assertEqual(process_data_challenge2(opunits, oilfields, wells), result)