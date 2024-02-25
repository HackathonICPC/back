from github import Auth, Github
from api import db_api_class

#кто украдет токен тот лох
auth = Auth.Token("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")
org_name = "ICPCoursesORG"

class github_api_class:    
	def __init__(self):
		self.g = Github(auth=auth)
		self.org = self.g.get_organization(org_name)

	def invite_user(self, task_id, user_id):
		github_username = db_api_class.get_github_username(user_id)
		self.g.get_repo(f"Task{task_id}_{user_id}").add_to_collaborators(github_username)
		
	def create_task(self, task_id, user_id):
		self.org.create_repo(f"Task{task_id}_{user_id}", private=True)
		self.invite_user(task_id, user_id)
	
	def get_url(self, task_id, user_id):
		return f"http://github.com/ICPCoursesORG/Task{task_id}_{user_id}"



kek = github_api_class()
kek.create_task(0, 0)

#repo = user.get_repo(repo_name)

#for repo in org.get_repos():
#	print(repo);