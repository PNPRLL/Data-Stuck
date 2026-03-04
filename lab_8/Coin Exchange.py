import json
def coinExchange(amount, coins):
    print(f"Amount: {amount}")
    
    result = {}
    total_coins = 0
    remaining = amount
    
    # ดึงมูลค่าเหรียญทั้งหมดที่มีในระบบ มาเรียงลำดับจากมากไปน้อย Greedy Algorithm
    coin_types = sorted(coins.keys(), reverse=True)
    
    for coin in coin_types:
        # คำนวณจำนวนเหรียญที่ต้องใช้
        use = min(remaining // coin, coins[coin])
        result[coin] = use
        total_coins += use
        remaining -= use * coin
        
    # ถ้าทอนเสร็จแล้วยังมีเงินเหลือ แปลว่าเหรียญไม่พอ
    if remaining > 0:
        print("Coins are not enough.")
    else:
        print("Coin exchange result:")
        for coin in coin_types:
            print(f"  {coin} baht = {result[coin]} coins")
        print(f"Number of coins: {total_coins}")

def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}

def main():
    amount = int(input())
    data = convert_key(json.loads(input()))
    coinExchange(amount, data)

main()