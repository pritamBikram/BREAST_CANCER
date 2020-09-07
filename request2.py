import requests

url = 'http://localhost:5000/breastcancer_api'
r = requests.post(url,json={'Clump Thickness':2, 'Uniformity of Cell Size':9, 'Uniformity of Cell Shape':6,'Marginal Adhesion':4,'Single Epithelial Cell Size':7,'Bare Nuclei':8,'Bland Chromatin':1,'Normal Nucleoli':7,'Mitoses':2})

print(r.json())

