Some real-world constraints to booking appointments that would add complexity to this API and how would they impact the design.

1. How to properly match patients' clinical need with doctors. 
	Complexity to the API: 
		- more information required as input from the patient, i.e: insurance info, clinical need, location preferences, etc.
		- more complex database design
		- Recommender system design: User - Items design, where USER is patients and ITEM is doctors and we want to recommend items to users. 
		  Need some sort of feature engineering and feature extractions to add additional signal to the matching problem.

2. Provider Data Manangement:
	Complexity to the API:
		- Real-time resource matching.
		- Provider network optimization.
