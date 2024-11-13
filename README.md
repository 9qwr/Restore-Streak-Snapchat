# SnapStreaks-Restorer

### الوصف:
هذا سكربت بلغة بايثون يهدف إلى استعادة "ستريكس" سناب شات باستخدام رمز "آركوس لابز". يقوم السكربت بتنفيذ طلبات HTTP لإرسال البيانات المطلوبة إلى API الخاص بـ Snap، بعد استرداد الرمز المطلوب من Arkose Labs.



(![Snapstreak Logo](https://github.com/9qwr/Restore-Streak-Snapchat/blob/main/image_2024-11-13_19-39-19.jpg)


### المتطلبات:
- Python 3.x
- مكتبة `requests`
- مكتبة `colorama`

### التثبيت:
1. تأكد من أنك قد قمت بتثبيت Python 3.x على جهازك.
2. قم بتثبيت المكتبات المطلوبة باستخدام الأمر التالي:
   ```bash
   pip install requests colorama
كيفية الاستخدام:
قم بتشغيل السكربت:

bash
نسخ الكود
python restore_snap_streak.py
سيطلب منك إدخال:

اسم المستخدم.
البريد الإلكتروني.
اسم المستخدم الخاص بصديقك.
بعد إدخال البيانات، سيتم إرسال الطلب إلى API لاستعادة الستريكس، وسيتم إعلامك ما إذا تم استعادة الستريكس بنجاح أم لا.

ملاحظات:
تأكد من أنك قمت بتوفير البيانات بشكل دقيق لضمان النجاح في استعادة الستريكس.
هذا السكربت يستخدم خدمة Arkose Labs للحصول على رمز التوثيق، وإذا واجهت مشاكل في الحصول على الرمز، يمكنك المحاولة لاحقًا.
إذا لم يتم استعادة الستريكس بنجاح، يرجى محاولة الإرسال مرة أخرى.
التواصل:
إذا كنت بحاجة إلى مساعدة إضافية، يمكنك التواصل عبر حساب GitHub أو على سناب شات @v88p.


# SnapStreaks-Restorer

### Description:
This is a Python script designed to restore Snapchat streaks using the Arkose Labs token. The script sends HTTP requests to submit the necessary data to the Snap API after fetching the required token from Arkose Labs.

### Requirements:
- Python 3.x
- `requests` library
- `colorama` library

### Installation:
1. Make sure Python 3.x is installed on your system.
2. Install the required libraries using the following command:
   ```bash
   pip install requests colorama
Usage:
Run the script:

bash
نسخ الكود
python restore_snap_streak.py
You will be prompted to enter:

Your username.
Your email.
Your friend's username.
Once the data is entered, the request will be sent to the API to restore the streak, and you will be notified if the streak was successfully restored.

Notes:
Ensure you provide accurate data to ensure successful streak restoration.
This script uses Arkose Labs to fetch the authentication token. If you encounter issues retrieving the token, you can try again later.
If the streak was not successfully restored, please try submitting the request again.
Contact:
If you need further assistance, you can reach out through the GitHub account or Snapchat @v88p.
