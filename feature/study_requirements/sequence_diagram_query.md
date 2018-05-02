// Used site : https://www.websequencediagrams.com/
// Updated date : 20180502

title Product Customization Sequence
User->+PetDB: Insert Pet Information 
PetDB->-*FeedbapCal: Send Pet Data
activate FeedbapCal
FeedbapCal->+IngredientDB: Request Required Ingredients
IngredientDB-->>-FeedbapCal: Send Required Ingredients
FeedbapCal->+Jipbabsystem: Send Processed Data
Jipbabsystem-->>-FeedbapCal: Provide Assorted Feed Incredients
FeedbapCal->+Feedbap: Send Assorted Feed Ingredients
deactivate FeedbapCal
destroy FeedbapCal
Feedbap-->>-User: Send Actual Assorted Feed

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
Feedbap->PetDB : reqPetInfo
PetDB-->>Feedbap : resPetInfo
Feedbap-->>User : showPetInfo
Feedbap->User : what to change?
User-->Feedbap : reqPetInfoEdit
Feedbap->PetDB : update
PetDB-->>Feedbap : resUpdatedInfo
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
Feedbap->*+PaymentMgr : sendTotalPayment
PaymentMgr->User : reqAcceptPayment
User-->>PaymentMgr : accept
PaymentMgr-->>-Feedbap : PaymentEnded
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
Feedbap ->UserInfoDB : Insert User Info
end
Feedbap ->User : send Registered Completed




title Monitoring Product Delivery Process
User->Feedbap : reqDeliveryStatus() with valid key
Feedbap -> PurchaseInfoDB : reqPurchaseRow() with key
PurchaseInfoDB -->> Feedbap : PurchaseInfo
alt Product Not Ready
Feedbap -> User : showProductStatus
alt if user requested streaming service
Feedbap -> ProcessingFactorySystem : reqStreaming() with key
alt if network is valid and user still want service
ProcessingFactorySystem-->>User : show Streaming service
else if network is not valid
Feedbap -->> User : NetworkErrorMsg
end
end
else Product Is Ready and on delivery state
Feedbap -> DelieverySystem : reqDelieveryInfoUrl() with key
DelieverySystem -->> User : DelieveryInfoUrl



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
Feedbap -> CustomerMngDB : Update freqyebtky Asked
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
ChatbotSystem -> -CustomerMngDB : Update Frequently Asked
end
