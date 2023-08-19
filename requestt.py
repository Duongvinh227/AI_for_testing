import requests
import concurrent.futures

def send_request(url):
    try:
        response = requests.get(url)
        return response.status_code
    except Exception as e:
        return str(e)

url = 'http://127.0.0.1:5000/hello'

num_requests = 1000

with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    urls = [url] * num_requests
    results = list(executor.map(send_request, urls))

print("Kết quả kiểm tra hiệu suất:")
print(f"Số request thành công: {results.count(200)}")
print(f"Số request thất bại: {results.count('error')}")
