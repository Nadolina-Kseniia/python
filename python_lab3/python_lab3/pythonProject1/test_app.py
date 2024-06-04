import unittest
from main import app


class VolumeCalculatorTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<h1>Объемы геометрических фигур</h1>'.encode('utf-8'), response.data)

    def test_calculate_volume_cube(self):
        response = self.app.post('/', data=dict(shape='cube', a='5', precision='2'))
        self.assertIn('125.0'.encode('utf-8'), response.data)

    def test_calculate_volume_sphere(self):
        response = self.app.post('/', data=dict(shape='sphere', a='3', precision='2'))
        self.assertIn('113.1'.encode('utf-8'), response.data)

    def test_calculate_volume_cylinder(self):
        response = self.app.post('/', data=dict(shape='cylinder', a='2', b='5', precision='2'))
        self.assertIn('62.83'.encode('utf-8'), response.data)

    def test_calculate_volume_cone(self):
        response = self.app.post('/', data=dict(shape='cone', a='3', b='6', precision='2'))
        self.assertIn('56.55'.encode('utf-8'), response.data)

    def test_calculate_volume_torus(self):
        response = self.app.post('/', data=dict(shape='torus', a='2', b='4', precision='2'))
        self.assertIn('197.92'.encode('utf-8'), response.data)

    def test_calculate_volume_paraboloid(self):
        response = self.app.post('/', data=dict(shape='paraboloid', a='3', b='5', precision='2'))
        self.assertIn('141.37'.encode('utf-8'), response.data)

    def test_calculate_volume_hyperboloid(self):
        response = self.app.post('/', data=dict(shape='hyperboloid', a='2', b='4', precision='2'))
        self.assertIn('50.27'.encode('utf-8'), response.data)

    def test_calculate_volume_ellipsoid(self):
        response = self.app.post('/', data=dict(shape='ellipsoid', a='2', b='3', c='4', precision='2'))
        self.assertIn('100.53'.encode('utf-8'), response.data)

    def test_calculate_volume_parallelepiped(self):
        response = self.app.post('/', data=dict(shape='parallelepiped', a='2', b='3', c='4', precision='2'))
        self.assertIn('24.0'.encode('utf-8'), response.data)

    def test_calculate_volume_trapezoid(self):
        response = self.app.post('/', data=dict(shape='trapezoid', a='3', b='5', c='4', precision='2'))
        self.assertIn('16.0'.encode('utf-8'), response.data)

    def test_calculate_volume_invalid_shape(self):
        response = self.app.post('/', data=dict(shape='invalid', a='2', b='3', c='4', precision='2'))
        self.assertIn('Неподдерживаемая фигура'.encode('utf-8'), response.data)


if __name__ == '__main__':
    unittest.main()
