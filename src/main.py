import requests

# ブラウザの開発者ツールなどで取得したCookieとXSRFトークンをここに貼り付ける
YOUR_COOKIE_STRING = "xxxx"
YOUR_XSRF_TOKEN = "xxxxxx"

def main():
    user_id = "kotonoha_musical"
    url = f"https://note.com/api/v2/creators/{user_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        
        "Cookie": YOUR_COOKIE_STRING,
        "X-Xsrf-Token": YOUR_XSRF_TOKEN,
        
        "Accept": "application/json, text/plain, */*",
        "Referer": f"https://note.com/{user_id}/all", # 参照元URLを設定
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("APIリクエスト成功")
        data = response.json()
        print(data)  # 取得したデータ全体を表示（デバッグ用）
        creator_info = data.get("data", {})
        
        follower_count = creator_info.get("followerCount")
        following_count = creator_info.get("followingCount")
        
        # 結果の表示
        print(f"フォロワー数: {follower_count}")
        print(f"フォロー数: {following_count}")
    else:
        print("ユーザー情報の取得に失敗しました。")


if __name__ == "__main__":
    main()
