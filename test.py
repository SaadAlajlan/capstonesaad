import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app
from models import setup_db, Coffeeshops, Visited
import os



class Capstone(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client
        self.database_name = "capstonesaad"
        self.database_path ="""postgres://fuslttnjinadwk:df83c0b314934b2f64e6de8ec6f5730f7e3fb39da0d3c7fc83165c20d8ab3c76@ec2-3-215-83-17.compute-1.amazonaws.com:5432/ddevls1ouhbli0"""
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
            visitor_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkRlVzhQY1ZUZmdYeHVKd2t1TFBrcCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtc2FhZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwY2JlNThhMWY2MDMwMDE5YjBiYjI5IiwiYXVkIjoiQ29mZmVlIHRhc3RlciIsImlhdCI6MTU5NTU0NDg0MiwiZXhwIjoxNTk1NjMxMjQyLCJhenAiOiJCQlpGRnhGZEJQRFV2bndvWjlNZmEwYkxyb1ZmSUE1SiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0Om5hbWUiLCJnZXQ6dmlzaXRlZCIsInBvc3Q6dmlzaXRlZCJdfQ.QQ0cSHSZEHVnvhzBUts59vvXJ_aPqodtNabyHHlXKq_cujkf8F60BrYPR8YDUrWwebWFKWLD2dyuH_41HgDnoNLBSkmNMY5wQSbOK8AppI_qrgXjHZNQ4ZWQDUcsJIl5gSUb8E1lEKZypVCEEg6urosk_rAnmScUiabj13ihKZ3qsTP3y27iCFa-idtiqniJPxtrbPS_uNNQR85MkDyPt87tuBFiGyDosRErKCAGil4fhe9XI-dKOVSPUf-mI2n6Yqp1vocgU-gVtSC0oS0guR0245WFRcqShb55N66iO2sRJqKly8Qws-OTQAefDkNXm01nUJ_ELFrkjgd1VHgWpg'
            admin_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkRlVzhQY1ZUZmdYeHVKd2t1TFBrcCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtc2FhZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwYzlkZWI3MTQ2OGMwMDEzMDAyMjRkIiwiYXVkIjoiQ29mZmVlIHRhc3RlciIsImlhdCI6MTU5NTU0NDY5MywiZXhwIjoxNTk1NjMxMDkzLCJhenAiOiJCQlpGRnhGZEJQRFV2bndvWjlNZmEwYkxyb1ZmSUE1SiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOm5hbWUiLCJnZXQ6bmFtZSIsImdldDp2aXNpdGVkIiwicGF0Y2g6bmFtZSIsInBvc3Q6bmFtZSIsInBvc3Q6dmlzaXRlZCJdfQ.oHROj5eKy0lTy2wvElty2fHxmP4ToYNwSE7tUdYawnubhXZ_IKTVoCdzjSmZFV_peMctjJ6pySkmZ5xJNsxbsOiiE4e8Ef5VreCNJNneIGIM7stwznIqWxaZB2lYBgu1PVY9aFIQN3unZjCJ8V3CamHyWbpOFcFEvBU_TtN9yWjynMVY1BrRwe4EyV6Wj-tGmmv9Vxf_N5V49htGqENGGTvJnxxsLqt38EuOwDBytm0NJ7aX2vTVRSUnPWIZRcKj_F98QLe9UsQyDi9a0FbG4WuDyQvrqn8GkGiJHLyOWHKDOPD_SOyx6PBrMZn1_E8MnvXx8EZLrTTZq2Kt3wzeTg'
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