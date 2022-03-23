import time
import random
from locust import HttpUser, task, TaskSet, between

'''
class LoadTest(HttpUser):
	@task
	def load_test(self):
		url = "luas-lingkaran-kali-x/" + str(random.randint(0, 200)) + "/" + str(random.randint(0, 200))
		self.client.get(url)
'''
'''
class StressTest(HttpUser):
    @task
    def stress_test(self):
        wait_time = between(15,20)
        payload = 'a=' + str(random.randint(0, 200)) + '&b=' + str(random.randint(0, 200))
        a = self.client.post(url="hasil-kali-ganjil/", 
            data=payload, headers={"Content-Type": "application/x-www-form-urlencoded"})
        time.sleep(1)
'''

class EnduranceTest(HttpUser):


    x = str(9726)
    y = str(800)
    
    @task
    def test1(self):
        url = "luas-lingkaran-kali-x/" + self.x + "/" + self.y
        self.client.get(url)
    
    @task
    def test2(self):
        payload = 'a=' + self.x + '&b=' + self.y
        self.client.post(url="hasil-kali-ganjil/", 
            data=payload, headers={"Content-Type": "application/x-www-form-urlencoded"})

    @task
    def test3(self):
        url = 'pangkat/?a='+self.x+'&b='+self.y
        self.client.post(url=url)