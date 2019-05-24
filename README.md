# Igralnica-Zanimalnica
Final project for my Django course at Software Univesity.

## Urls:

#### Accounts (authenticated users)

###### /accounts/profile/ (redirects to authenticated user's profile)
###### /accounts/profile/{pk}/
###### /accounts/edit/{pk}/
###### /accounts/change_password/
###### /accounts/change_password/done/

#### Accounts (unauthenticated users)

###### /accounts/login/
###### /accounts/signup/ 
###### /accounts/logout/ (redirects to index)
###### /accounts/reset_password/
###### /accounts/reset_password/done/
###### /accounts/reset_password/{uidb64}/{token}/
###### /accounts/reset_password/complete/

#### News 

###### /news/create/ (admin users)
###### /news/details/{pk}/ (authenticated users can post coments)
###### /news/delete/{pk}/ (admin users)
###### /news/edit/{pk}/ (admin users)
###### / (non-authenticated)

#### Comments

###### /comment/edit/{pk}/ (authenticated owner and admins)
###### /comment/delete/{pk}/ (authenticated owner and admins)

#### Pictures

###### /pictures/ (lists public albums to unauthenticated users and all albums to admins)
###### /pictures/album/{pk}/ (unauthenticated users)
###### /pictures/album/add/ (admin users)
###### /pictures/album/edit/{pk}/ (admin users)
###### /pictures/delete/album/{pk}/ (admin users)
###### /pictures/delete/picture/{pk}/ (admin users)

#### Application form

###### /application/ (authenticated users)

#### About

###### /about/


