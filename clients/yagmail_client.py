import os
import yagmail

contents = """
<div class=""><div class="aHl"></div><div id=":3e7" tabindex="-1"></div><div id=":3eb" class="ii gt" jslog="20277; u014N:xr6bB; 4:W251bGwsbnVsbCxbXV0."><div id=":3ea" class="a3s aiL msg-8748652637163331374"><u></u><div style="margin:0;padding:0" bgcolor="#FFFFFF"><table width="100%" height="100%" style="min-width:348px" border="0" cellspacing="0" cellpadding="0" lang="en"><tbody><tr height="32" style="height:32px"><td></td></tr><tr align="center"><td><div><div></div></div><table border="0" cellspacing="0" cellpadding="0" style="padding-bottom:20px;max-width:516px;min-width:220px"><tbody><tr><td width="8" style="width:8px"></td><td><div style="border-style:solid;border-width:thin;border-color:#dadce0;border-radius:8px;padding:40px 20px" align="center" class="m_-8748652637163331374mdv2rw"><img src="{email}" width="74" height="24" aria-hidden="true" style="margin-bottom:16px" alt="" class="CToWUd"><div style="font-family:'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif;border-bottom:thin solid #dadce0;color:rgba(0,0,0,0.87);line-height:32px;padding-bottom:24px;text-align:center;word-break:break-word"><div style="font-size:24px">A new sign-in </div><table align="center" style="margin-top:8px"><tbody><tr style="line-height:normal"><td align="right" style="padding-right:8px"><img width="20" height="20" style="width:20px;height:20px;vertical-align:sub;border-radius:50%" src="{email}" alt="" class="CToWUd"></td><td><a style="font-family:'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif;color:rgba(0,0,0,0.87);font-size:14px;line-height:20px">{email}</a></td></tr></tbody></table> </div><div style="font-family:Roboto-Regular,Helvetica,Arial,sans-serif;font-size:14px;color:rgba(0,0,0,0.87);line-height:20px;padding-top:20px;text-align:left">We noticed a new sign-in to your Account on a device. If this was you, you don’t need to do anything. If not, we’ll help you secure your account.<div style="padding-top:32px;text-align:center"><a href="https://accounts.google.com/AccountChooser?Email=chadlimjinjie@gmail.com&amp;continue=https://myaccount.google.com/alert/nt/1653665395092?rfn%3D20%26rfnc%3D1%26eid%3D-4466804903087859634%26et%3D0" style="font-family:'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif;line-height:16px;color:#ffffff;font-weight:400;text-decoration:none;font-size:14px;display:inline-block;padding:10px 24px;background-color:#4184f3;border-radius:5px;min-width:90px" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://accounts.google.com/AccountChooser?Email%3Dchadlimjinjie@gmail.com%26continue%3Dhttps://myaccount.google.com/alert/nt/1653665395092?rfn%253D20%2526rfnc%253D1%2526eid%253D-4466804903087859634%2526et%253D0&amp;source=gmail&amp;ust=1653796490887000&amp;usg=AOvVaw0JILR8VHBisomtuut7LWn3">Check activity</a></div></div><div style="padding-top:20px;font-size:12px;line-height:16px;color:#5f6368;letter-spacing:0.3px;text-align:center">You can also see <span class="il">security</span> activity at<br><a style="color:rgba(0,0,0,0.87);text-decoration:inherit">https://myaccount.google.com/<wbr>notifications</a></div></div><div style="text-align:left"><div style="font-family:Roboto-Regular,Helvetica,Arial,sans-serif;color:rgba(0,0,0,0.54);font-size:11px;line-height:18px;padding-top:12px;text-align:center"><div>You received this email to let you know about important changes to your Account and services.</div><div style="direction:ltr">© 2022 Chad Lim .Tech LLC, <a class="m_-8748652637163331374afal" style="font-family:Roboto-Regular,Helvetica,Arial,sans-serif;color:rgba(0,0,0,0.54);font-size:11px;line-height:18px;padding-top:12px;text-align:center">417 Hougang, Avenue 8, 13-972, SG 530417, SG</a></div></div></div></td><td width="8" style="width:8px"></td></tr></tbody></table></td></tr><tr height="32" style="height:32px"><td></td></tr></tbody></table></div></div><div class="yj6qo"></div></div><div id=":2u4" class="ii gt" style="display:none"><div id=":2u3" class="a3s aiL "></div></div><div class="hi"></div></div>
"""

yag = yagmail.SMTP(user={"chad@chadlim.tech": "Chad Lim"},
                   password=os.getenv("MAIL_PASS"),
                   host="smtp.chadlim.tech",
                   port=587,
                   smtp_starttls=True,
                   smtp_ssl=False)


def send_email(to_email: str):
    yag.send(to_email, "Security alert", contents.format(email=to_email))
    print("Sent")


def send_raw_email(to_email: str, subject: str, text: str):
    yag.send(to_email, subject, text)
    print("Sent")
