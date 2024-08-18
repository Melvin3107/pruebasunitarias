import unittest
from flask import json
from app import app  # Asegúrate de que `app` se importe correctamente desde tu aplicación

class AppTestCase(unittest.TestCase):
    
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_addition(self):
        response = self.client.post('/calculate', json={'a': 5, 'b': 3, 'operation': '+'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], 8)

    def test_subtraction(self):
        response = self.client.post('/calculate', json={'a': 5, 'b': 3, 'operation': '-'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], 2)

    def test_multiplication(self):
        response = self.client.post('/calculate', json={'a': 5, 'b': 3, 'operation': '*'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], 15)

    def test_division(self):
        response = self.client.post('/calculate', json={'a': 6, 'b': 3, 'operation': '/'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], 2.0)

    def test_division_by_zero(self):
        response = self.client.post('/calculate', json={'a': 5, 'b': 0, 'operation': '/'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)['error'], 'Division by zero')

    def test_invalid_operation(self):
        response = self.client.post('/calculate', json={'a': 5, 'b': 3, 'operation': '%'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)['error'], 'Invalid operation')

    def test_invalid_input(self):
        response = self.client.post('/calculate', json={'a': 'five', 'b': 3, 'operation': '+'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)['error'], 'Invalid number format')

if __name__ == '__main__':
    unittest.main()
