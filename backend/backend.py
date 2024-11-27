from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/api/restore_streak', methods=['POST'])
def restore_streak():
    try:
        # استلام البيانات من الواجهة
        data = request.json
        username = data['username']
        email = data['email']
        friend = data['friend']

        # إرسال الطلب إلى Arkose Labs
        arkose_url = "https://client-api.arkoselabs.com/fc/gt2/public_key/F2388D0C-F087-4EAB-B3B0-0358C40FE1EA"
        arkose_headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0",
        }
        arkose_payload = "bda=zz"  # أضف البايلود هنا

        arkose_response = requests.post(arkose_url, data=arkose_payload, headers=arkose_headers)
        arkose_data = arkose_response.json()

        if "token" in arkose_data:
            arkose_token = arkose_data['token']

            # إرسال الطلب إلى Snap API
            snap_url = "https://wassupsnap.appspot.com/en-US/api/v2/zendesk/send"
            snap_headers = {
                "Content-Type": "multipart/form-data",
                "User-Agent": "Mozilla/5.0",
            }

            snap_payload = {
                "key": "snapstreaks-restore",
                "arkose-token": arkose_token,
                "field-24281229": username,
                "field-24335325": email,
                "field-24369736": friend,
            }

            snap_response = requests.post(snap_url, data=snap_payload, headers=snap_headers)
            if snap_response.status_code == 200:
                return jsonify({"status": "success", "message": "Snap streak restored!"})
            else:
                return jsonify({"status": "error", "message": "Failed to restore streak."}), 500

        return jsonify({"status": "error", "message": "Failed to fetch Arkose token."}), 500

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
