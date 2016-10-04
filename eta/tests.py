from django.test import TestCase

class GetValueFromETAGroupTestCase(TestCase):
	def testGetValueFromETAGroup(self):
		with freeze_time("2014-01-01 10:00:00+00:00", tz_offset=+8):
			self.assertEquals(etaGroupValue('TEST3', 'limit'), 15)

		with freeze_time("2014-01-01 1:00:01+00:00", tz_offset=+8):
			self.assertEquals(etaGroupValue('TEST3', 'limit'), 30)
			self.assertEquals(etaGroupValue('TEST3', 'limit'), 30)

		with freeze_time("2014-01-01 10:00:00+00:00", tz_offset=+8):
			self.assertEquals(etaGroupValue('TEST3', 'gap'), None)

