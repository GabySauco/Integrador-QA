import requests
import unittest

class TestPokeApi(unittest.TestCase):

 def setUp (self):
    self.url = 'https://pokeapi.co/api/v2/'


 def test_get_berry(self):
    r = requests.get (self.url + 'berry/1')
    self.assertEqual(r.status_code, 200)
    berry_data = r.json()
    self.assertEqual(berry_data['size'], 20)
    self.assertEqual(berry_data['soil_dryness'], 15) 
    self.assertEqual(berry_data['firmness']['name'], 'soft')

def test_get_berry_2(self):
    r =requests.get(self.url + 'berry/2')
    self.assertEqual(r.status_code, 200)
    berry_2_data = r.json()
    self.assertEqual(berry_2_data['firmness']['name'], 'super-hard')
    self.assertEqual(berry_2_data['size'], 20)
    self.assertEqual(berry_2_data['soil_dryness'], 15)

def test_get_pikachu(self):
    r = requests.get (self.url + 'pokemon/pikachu')
    self.assertEqual(r.status_code, 200)
    pikachu_data= r.json()
    experiencia_base= pikachu_data['experiencia_base']
    self.assertGreater(experiencia_base, 10)
    self.assertLess(experiencia_base, 1000)
    types= [t['type']['name'] for t in pikachu_data['types']]
    self.assertIn('electric', types)


if __name__ == '__main__':
    unittest.main()

