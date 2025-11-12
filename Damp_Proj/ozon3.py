import requests

def get_city_air(city):
    """
    Fetch air quality data for a given city using open API or mock response.
    Replace this with real logic from original ozon3.py
    """
    try:
        # Mock example (replace with actual API endpoint)
        api_url = f"https://api.openaq.org/v2/latest?city={city}"
        res = requests.get(api_url)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        return {"error": str(e)}
