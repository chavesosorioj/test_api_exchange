
import requests


payload = {'username':'Juucha','password':'Anypointjucha1'}
r = requests.post(' https://stgx.anypoint.mulesoft.com/accounts/login', jason=payload)
print(r)

h = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en",
    "Connection": "keep-alive",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarysdG6A4vE7tXo4Uz4",
    "Cookie": "exchange.sess=eyJhY2Nlc3NUb2tlbiI6ImQwOTcxY2RlLTM2MzctNDQ3ZS04MGQ2LWYzNDQ1NmY1MjJhZCIsInRva2VuVHlwZSI6ImJ"
              "lYXJlciJ9; exchange.sess.sig=yWLr1wooNyiK2syLjzkXHfk4vMI; OptanonConsent=isIABGlobal=false&datestamp=Tue+"
              "Sep+13+2022+17%3A18%3A37+GMT-0300+(Argentina+Standard+Time)&version=6.17.0&hosts=&consentId=e65aced1-73cc"
              "-4e9f-a91b-ca77b026872d&interactionCount=2&landingPath=NotLandingPage&groups=1%3A1%2C3%3A1%2C4%3A1&Awaiti"
              "ngReconsent=false&geolocation=AR%3BB&isGpcEnabled=0; _vwo_uuid_v2=D10D1C0472B87D376B34F2321EEA2A5AA|b0123"
              "d60726ba844c9fe578b1e40446e; _vis_opt_test_cookie=1; _vwo_uuid=D10D1C0472B87D376B34F2321EEA2A5AA; Optanon"
              "AlertBoxClosed=2022-08-22T14:57:55.823Z; _cs_c=0; _mkto_trk=id:564-SZS-136&token:_mch-mulesoft.com-166118"
              "0277058-79239; __qca=P0-1703246842-1661186854485; amplitude_idundefinedmulesoft.com=eyJvcHRPdXQiOmZhbHNlL"
              "CJzZXNzaW9uSWQiOm51bGwsImxhc3RFdmVudFRpbWUiOm51bGwsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYm"
              "VyIjowfQ==; _hly_vid=ea468f5d-3f0e-4b4a-a529-739b63855adf; _mkto_trk_http=id:564-SZS-136&token:_mch-mules"
              "oft.com-1661180277058-79239; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjgwNGRjMmUxLTY0NzItNGIyN"
              "S05MjVjLThkMTk0YTBmNGI3YSIsIm9yZ2FuaXphdGlvbiI6eyJpZCI6ImZiOWFkYjcwLTY2NDktNDNlNC04OTU0LTU5ZjY5Yjc1NzdiOC"
              "IsImVudGl0bGVtZW50cyI6eyJhcGlzIjp7ImVuYWJsZWQiOnRydWV9LCJjcm93ZCI6eyJoaWRlQXBpTWFuYWdlckRlc2lnbmVyIjp0cnV"
              "lLCJoaWRlRm9ybWVyQXBpUGxhdGZvcm0iOnRydWUsImVudmlyb25tZW50cyI6dHJ1ZX0sImNyb3dkU2VsZlNlcnZpY2VNaWdyYXRpb24i"
              "OnsiZW5hYmxlZCI6ZmFsc2V9LCJoeWJyaWQiOnsiZW5hYmxlZCI6dHJ1ZX0sIndvcmtlckNsb3VkcyI6eyJhc3NpZ25lZCI6MCwicmVhc"
              "3NpZ25lZCI6MH0sInNlcnZpY2VNZXNoIjp7ImVuYWJsZWQiOnRydWV9LCJmbGV4R2F0ZXdheSI6eyJlbmFibGVkIjp0cnVlfX19LCJpbn"
              "RlcmFjdGl2ZUxvZ2luIjp0cnVlLCJ0b2tlbiI6IjdkMzI1YTEwLWVhNDAtNDQxMi1iOGRmLWFlYTg3ZTUwMzg0ZCIsImlhdCI6MTY2MzE"
              "wMDEwNiwiYXVkIjoiaHR0cDovL2FwaS1wbGF0Zm9ybS1hcGkvcmVwb3NpdG9yeSIsImlzcyI6Imh0dHA6Ly9hcGktcGxhdGZvcm0tYXBp"
              "L3JlcG9zaXRvcnkifQ.KlvsxCtRlSWGLikGxpneTDqPzxKYhr0HHVn7HPhcOHM; ajs_user_id=%22804dc2e1-6472-4b25-925c-8d"
              "194a0f4b7a%22; ajs_anonymous_id=%227ce648bb-9a06-4708-8108-cd8bae78848e%22; vid=07c83707-1725-4b1e-a577-3"
              "78b6d76a227; debug_vis_opt_test_cookie=1; debug_vwo_ds=3%241665513763%3A31.66455147%3A%3A; _vis_opt_exp_1"
              "37_goal_1=1; _csrf=NURWG7uQabWTXEZSisF2FM6j; _vis_opt_exp_140_combi=1; _vis_opt_exp_138_split=3; _vis_opt"
              "_exp_138_combi=3; _vis_opt_exp_138_goal_1=1; _vis_opt_exp_140_goal_2=1; _vis_opt_exp_138_goal_4=1; _vis_o"
              "pt_exp_138_goal_3=1; _vis_opt_exp_138_goal_2=1; _gcl_au=1.1.2132886424.1669116037; _vis_opt_exp_148_combi"
              "=2; _vis_opt_exp_148_goal_2=1; _vis_opt_exp_148_goal_1=1; _vis_opt_exp_150_split=2; _vis_opt_exp_150_comb"
              "i=2; _vis_opt_exp_150_goal_1=1; amplitude_id_7856322d613393b800727439f0954eb9mulesoft.com=eyJkZXZpY2VJZCI"
              "6ImQ4Mzk4YmFhLTE4NjAtNDE0Ny1iNmIwLWJlODI0ZDc1ZDNiN1IiLCJ1c2VySWQiOiJkYjExNzdmNy1mNmFiLTQ2NTYtODkxMy0wMzY"
              "3ZDhlYzY0OTYiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE2NzIwNjMzMTA4NzAsImxhc3RFdmVudFRpbWUiOjE2NzIwNjMzMTA4"
              "NzQsImV2ZW50SWQiOjIyNCwiaWRlbnRpZnlJZCI6MTgsInNlcXVlbmNlTnVtYmVyIjoyNDJ9; _gac_UA-605632-33=1.1672067088."
              "CjwKCAiAnO2MBhApEiwA8q0HYdHcqytQ5PV31pzmzpXEi4AAtNqPqNRWgVuKphx7UoHuAMZI9l7mKRoC6yQQAvD_BwE; _gac_UA-1183"
              "67394-32=1.1672067088.CjwKCAiAnO2MBhApEiwA8q0HYdHcqytQ5PV31pzmzpXEi4AAtNqPqNRWgVuKphx7UoHuAMZI9l7mKRoC6yQ"
              "QAvD_BwE; _gcl_aw=GCL.1672067088.CjwKCAiAnO2MBhApEiwA8q0HYdHcqytQ5PV31pzmzpXEi4AAtNqPqNRWgVuKphx7UoHuAMZI"
              "9l7mKRoC6yQQAvD_BwE; _gcl_dc=GCL.1672067088.CjwKCAiAnO2MBhApEiwA8q0HYdHcqytQ5PV31pzmzpXEi4AAtNqPqNRWgVuKp"
              "hx7UoHuAMZI9l7mKRoC6yQQAvD_BwE; _gac_UA-605632-12=1.1672067088.CjwKCAiAnO2MBhApEiwA8q0HYdHcqytQ5PV31pzmzp"
              "XEi4AAtNqPqNRWgVuKphx7UoHuAMZI9l7mKRoC6yQQAvD_BwE; _ga=GA1.1.790559710.1661180276; utm_medium=direct; deb"
              "ug_vis_preview_582086=%7B%22137%22%3A%7B%22v%22%3A%223%22%2C%22ts%22%3A1665514273295%7D%7D; debug_vis_opt"
              "_exp_131_combi=2; debug_vis_opt_exp_131_goal_1=1; _vis_opt_exp_131_goal_203=1; debug_vwo_uuid=JB134F48C04"
              "64FB09AE7F6058202CE949; _ga_GXS68FGQZP=GS1.1.1673117057.121.1.1673117133.60.0.0; _gid=GA1.2.979729746.167"
              "3269338; SLEditMode=0; trwv.uid_http=mulesoft-1671117801985-e8e075d6%3A81%3A1; debug_vis_opt_exp_131_goal"
              "_203=1; _vwo_ds=3%3At_0%2Ca_0%3A-1%241661180091%3A6.80325026%3A%3A%3A130_0%2C119_0%2C6_0%2C5_0%2C4_0%3A0;"
              " _cs_id=676adb21-f642-a8a6-c639-939d0c62ff40.1661180276.298.1673457392.1669809667.1.1695344276023; BE_CLA"
              "3=p_id%3D%26bf%3D6d5b9b64aca8877b4f2a1c7b7fb86bb2%26bn%3D79%26bv%3D3.44%26s_expire%3D1673549266094%26s_id%"
              "3D676adb21-f642-a8a6-c639-939d0c62ff40.1661180276.298.1672326424.1669809667.1.1695344276023%253B%2520_cs_"
              "s%253D1; RT='z=1&dm=mulesoft.com&si=nha8egqmwsm&ss=lc4xr52a&sl=0&tt=0'; _ga=GA1.1.790559710.1661180276; "
              "trwv.uid=mulesoft-1671117801985-e8e075d6%3A94%3A1; OptanonConsent=isIABGlobal=false&datestamp=Wed+Jan+11+"
              "2023+16%3A04%3A59+GMT-0300+(Argentina+Standard+Time)&version=6.17.0&hosts=&consentId=e65aced1-73cc-4e9f-a"
              "91b-ca77b026872d&interactionCount=2&landingPath=NotLandingPage&groups=1%3A1%2C3%3A1%2C4%3A1&AwaitingRecon"
              "sent=false&geolocation=AR%3BB; _ga_HQLG2N93Q1=GS1.1.1673465763.400.0.1673467366.0.0.0; _gid=GA1.1.9797297"
              "46.1673269338; OptanonConsent=isIABGlobal=false&datestamp=Wed+Jan+11+2023+20%3A22%3A47+GMT-0300+(Argentin"
              "a+Standard+Time)&version=6.14.0&hosts=&consentId=e65aced1-73cc-4e9f-a91b-ca77b026872d&interactionCount=2&"
              "landingPath=NotLandingPage&groups=1%3A1%2C3%3A1%2C4%3A1&AwaitingReconsent=false&geolocation=AR%3BB; ampli"
              "tude_id_af54216f1488bfe2148ba742ea6c60dbmulesoft.com=eyJkZXZpY2VJZCI6IjRiZjVlMTg3LWEzZWUtNDRjMy04N2Y4LTk5"
              "YWFiYzk3MTkwY1IiLCJ1c2VySWQiOiI4MDRkYzJlMS02NDcyLTRiMjUtOTI1Yy04ZDE5NGEwZjRiN2EiLCJvcHRPdXQiOmZhbHNlLCJzZ"
              "XNzaW9uSWQiOjE2NzM0NzkyNzk5NDIsImxhc3RFdmVudFRpbWUiOjE2NzM0NzkzNjc3MzIsImV2ZW50SWQiOjI3LCJpZGVudGlmeUlkIj"
              "oxMywic2VxdWVuY2VOdW1iZXIiOjQwfQ==; mulesoft.sess=eyJpZCI6InNzMEFTLWZnUVByVk5lTm9lN0JFcFF5SXFWZTlNLW9rIiw"
              "icGFzc3BvcnQiOnsidXNlciI6eyJ1c2VyX2lkIjoiODA0ZGMyZTEtNjQ3Mi00YjI1LTkyNWMtOGQxOTRhMGY0YjdhIn19LCJhdXRob3J"
              "pemUiOnt9fQ==; mulesoft.sess.sig=p3cC8mhB7byg891TcLovg2kgZy8; XSRF-TOKEN=fBQD8LRs-Fwm0B35PmovyD_YsKzXLL6ImhCw",
    "Host": "stgx.anypoint.mulesoft.com",
    "Origin": "https://stgx.anypoint.mulesoft.com",
    "Referer": "https://stgx.anypoint.mulesoft.com/exchange/create/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "accept": "application/json",
    "authorization": "bearer d0971cde-3637-447e-80d6-f34456f522ad",
    "sec-ch-ua": 'Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"' ,
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "x-forwarded-for": '147.161.128.254',
    "x-from-service": "Exchange UI",
    "x-ms-developer": "true",
    "x-sync-publication": "false"
}