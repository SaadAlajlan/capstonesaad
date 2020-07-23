import os , unittest, json
from flask_sqlalchemy import SQLAlchemy

from app import app
from models import setup_db, Coffeeshops, Visited
import os


class Capstone(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client
        self.database_name = "capstonesaad"
        self.database_path = """postgres://postgres:1@localhost:
        5432/capstonesaad"""
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
            visitor_token = os.environ.get('VISITOR_TOKEN')
            admin_token = os.environ.get('ADMIN_TOKEN')
            self.admin_header = {'Authorization': 'Bearer ' + str(admin_token)}
            self.visitor_header = {'Authorization': 'Bearer ' + str(visitor_token)}

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_coffeeshops(self):
        res = self.client().get('/coffeeshops', headers=self.visitor_header)
        data = json.loads(res.data)

        self.assertTrue(data['coffeeshop'])

    def test_get_coffeeshops_405(self):
        res = self.client().get('/coffeeshops/1', headers=self.visitor_header)

        self.assertEqual(res.status_code, 405)

    def test_get_visited(self):
        res = self.client().get('/visited', headers=self.visitor_header)
        data = json.loads(res.data)

        self.assertTrue(data['visited'])

    def test_get_visited_404(self):
        res = self.client().get('/visited/1', headers=self.visitor_header)

        self.assertEqual(res.status_code, 404)

    def test_post_coffeeshops(self):
        res = self.client().post('/coffeeshops', json={
                                                "name": "blueBottle",
                                                "rate": "5",
                                                "recommended": "cortado"
                                              },
                                 headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'yes')
        self.assertEqual(res.status_code, 201)

    def test_post_coffeeshops_500(self):
        res = self.client().post('/coffeeshops', json={
                                                "name": 1,
                                                "recommended": True
                                                },
                                 headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'no')
        self.assertEqual(res.status_code, 500)

    def test_post_visited(self):
        res = self.client().post('/visited', json={
                                                "name": "blueBottle",
                                                "recommended": "cortado"
                                                },
                                 headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'yes')

    def test_post_visited_500(self):
        res = self.client().post('/coffeeshops', json={
                                                "name": True,
                                                "recommended": True
                                                },
                                 headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'no')
        self.assertEqual(res.status_code, 500)

    def test_patch_coffeeshops(self):
        res = self.client().patch('/coffeeshops/5', json={
                                                    "name": "littleCollin",
                                                    "rate": "4",
                                                    "recommended": "latte"
                                                    },
                                  headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'yes')

    def test_patch_coffeeshops_500(self):
        res = self.client().patch('/coffeeshops/99', json={
                                                    "name": "littleCollin",
                                                    "rate": "4",
                                                    "recommended": "latte"
                                                    },
                                  headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'no')

    def test_delete_coffeeshops(self):
        res = self.client().delete('/coffeeshops/7',  headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'yes')

    def test_delete_coffeeshops_404(self):
        res = self.client().delete('/coffeeshops/99',  headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'no')

    def test_get_coffeeshops_adminRole(self):
        res = self.client().get('/coffeeshops', headers=self.admin_header)

        self.assertEqual(res.status_code, 401)

    def test_get_visited_adminRole(self):
        res = self.client().get('/visited', headers=self.admin_header)

        self.assertEqual(res.status_code, 401)

    def test_post_visited_visitorRole(self):
        res = self.client().post('/visited', json={
                                                "name": "blueBottle",
                                                "recommended": "cortado"
                                                },
                                 headers=self.visitor_header)

        self.assertEqual(res.status_code, 401)

    def test_patch_coffeeshops_visitorRole(self):
        res = self.client().patch('/coffeeshops/5', json={
                                                    "name": "littleCollin",
                                                    "rate": "4",
                                                    "recommended": "latte"
                                                    },
                                  headers=self.visitor_header)

        self.assertEqual(res.status_code, 401)


if __name__ == "__main__":
    unittest.main()