from intasend import APIService

API_PUBLISHABLE_KEY = 'ISPubKey_test_23af1be8-8958-4230-86b5-709565f0355c'

API_TOKEN = 'ISSecretKey_test_5435df52-7f09-4d35-b4cf-47b0d0ae816f'


service = APIService(token=API_TOKEN, public_key=API_PUBLISHABLE_KEY, test=True)

create_order = service.collect.mpesa_stk_push(phone_number= 254708374149, email='test@gmail.com', amount=100,
                                              narrative='Purchase of items')

print(create_order)
