import requests


DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 AI-CTF-Agent-Lab",
    "Accept": "*/*",
}


def send_get(url, params=None, headers=None, timeout=10):
    final_headers = DEFAULT_HEADERS.copy()

    if headers:
        final_headers.update(headers)

    try:
        response = requests.get(
            url,
            params=params,
            headers=final_headers,
            timeout=timeout,
            verify=False,
        )

        print(f"[GET] {response.url}")
        print(f"[STATUS] {response.status_code}")
        print(f"[LENGTH] {len(response.text)}")
        print(response.text[:1000])

        return response

    except requests.RequestException as e:
        print(f"[-] Request error: {e}")
        return None


def send_post(url, data=None, json_data=None, headers=None, timeout=10):
    final_headers = DEFAULT_HEADERS.copy()

    if headers:
        final_headers.update(headers)

    try:
        response = requests.post(
            url,
            data=data,
            json=json_data,
            headers=final_headers,
            timeout=timeout,
            verify=False,
        )

        print(f"[POST] {url}")
        print(f"[STATUS] {response.status_code}")
        print(f"[LENGTH] {len(response.text)}")
        print(response.text[:1000])

        return response

    except requests.RequestException as e:
        print(f"[-] Request error: {e}")
        return None


if __name__ == "__main__":
    test_url = "http://example.com"
    send_get(test_url)
