import requests
import datetime

def submit_zoho_form():
    today = datetime.datetime.now().strftime("%d-%b-%Y")

    url = "https://forms.zohopublic.in/gurmindersinghkal1/form/Signup/formperma/GeJFMLBDfoWlIJfhI46Qyx0Dlf3kHhMSRsvMItq_Riw/formSubmit"

    data = {
        "Email": "hanshul.k@kalvium.community",
        "SingleLine": today,
        "Checkbox": "I accept the Terms and Conditions.",
        "Dropdown": "Work Integrated - Simulated",
        "MultiLine": "Completing milestones",
        "Slider": "5",
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        print("✅ Form submitted successfully at", datetime.datetime.now())
    else:
        print("❌ Submission failed:", response.status_code, response.text)

if __name__ == "__main__":
    submit_zoho_form()
