// Used site : https://www.websequencediagrams.com/
// Updated date : 20180503

title Product Customization Sequence
opt customizing process
loop user still need to find their pet feed
User->+Pet information: Insert Pet Information
Pet information->-*Pet food processing system: Send Pet Data
activate Pet food processing system
Pet food processing system->IngredientDB: Request Required Ingredients
IngredientDB-->>Pet food processing system: Send Required Ingredients
Pet food processing system->+Jipbabsystem: Send Processed Data
Jipbabsystem-->>-Pet food processing system: Provide Assorted Feed Incredients
Pet food processing system->+Feedbap: Send Assorted Feed Ingredients
deactivate Pet food processing system
destroy Pet food processing system
Feedbap-->>-User: Send Actual Assorted Feed
end
end
Feedbap->User : ask whether save the info or not
User -->> Feedbap : response
opt user want to save their info
Feedbap->UserDB : reqUserkey
UserDB-->>Feedbap : resUserkey
Feedbap->PetfoodDB : update the feed information with user key
PetfoodDB-->>Feedbap : update complete msg
Feedbap->User : update completed msg

title EditUserInfo
User->+Feedbap : requestEdit
alt Login status
Feedbap-->>User : resEditType
User->Feedbap : reqEdit
alt editUserInfo
Feedbap->UserDB : reqUserInfo
UserDB-->>Feedbap : resUserInfo
Feedbap-->>User : showUserInfo
Feedbap->User : what to change?
User-->Feedbap : reqUserInfoEdit
Feedbap->UserDB : update
UserDB-->>Feedbap : resUpdatedInfo
Feedbap-->User : showUpdatedInfo
else edit petInfo
Feedbap->Pet information : reqPetInfo
Pet information-->>Feedbap : resPetInfo
Feedbap-->>User : showPetInfo
Feedbap->User : what to change?
User-->Feedbap : reqPetInfoEdit
Feedbap->Pet information : update
Pet information-->>Feedbap : resUpdatedInfo
Feedbap-->User : showUpdatedInfo


title Purchase
User->Feedbap : reqPurchasePage()
Feedbap-->>User : resPurchasePage()
Feedbap->User : askPetFoodQuantity
User-->>Feedbap : decideQuantity
Feedbap->User : askPetFoodOrderingType
User-->>Feedbap : decideOrderingType
alt Ordering type == periodically
Feedbap->User : askLogin
User-->>Feedbap : LoginToFeedbap
User->Feedbap : decidedOrderingPeriod
end
Feedbap->User : askPaymentMethod
User-->>Feedbap : ChoosePaymentMethod
Feedbap->*+Payment system : sendTotalPayment
Payment system->User : reqAcceptPayment
User-->>Payment system : accept
Payment system-->>-Feedbap : PaymentEnded
Feedbap->User : showEndedPaymentInfo
Feedbap->PurchaseDB : deliverPurchaseInfo



title Register User ID and Pet Info
User->Feedbap : reqRegisterPage()
Feedbap-->>User : resRegisterPage()
alt InseertNotCompleted
User->+Feedbap : Input User Name
User->Feedbap : Input User Id
User->Feedbap :Input User Address
User->Feedbap :Input User PhoneNumber
User->Feedbap : Input User ValidateEmail
Feedbap -> Feedbap : Check valid
Feedbap ->-User:Send valid message
Feedbap ->UserDB : Insert User Info
end
Feedbap ->User : send Registered Completed


title Monitoring Product Delivery Process
User->+Feedbap : reqDeliveryStatus() with valid key
Feedbap -> PurchaseDB : reqPurchaseRow() with key
PurchaseDB -->> Feedbap : resPurchaseInformation
alt Product Not Ready
Feedbap -> -User : showProductStatus
alt if user requested streaming service
Feedbap -> +Manufacturing System : reqStreaming() with key
alt if network is valid and user still want service
Manufacturing System-->>-User : show Streaming service
else if network is not valid
Feedbap -->> User : NetworkErrorMsg
end
end
else Product Is Ready and on delivery state
Feedbap -> +DelieverySystem : reqDelieveryInfoUrl() with key
DelieverySystem -->> -User : DelieveryInfoUrl



title CRM
alt if want to get information on Feedbap homepage
User -> Feedbap : reqServiceCenterPage()
Feedbap -->> User : resServiceCenterPage()
opt
loop while customer want service more
User->Feedbap :question
Feedbap -> User : answer
end
end
Feedbap -> CRM DB : Update freqyebtky Asked
else if want to get information on Chatbot
User -> Feedbap : reqChatbotPage()
Feedbap -> +ChatbotSystem : reqChatbotOpen()
ChatbotSystem -->> User : resChatbotReadyMsg()
opt
loop while customer want chatbot
User -> ChatbotSystem : question
ChatbotSystem -->> User : Answer
end
end
ChatbotSystem -> -CRM DB : Update Frequently Asked
end

alt if user want more information
User -> Consultant : ask about specified information that above systems cannot handle

