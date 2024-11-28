def sieve_of_eratosthenes(limit):
    # Tạo một danh sách đánh dấu các số nguyên tố
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False  # 0 và 1 không phải là số nguyên tố

    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            for multiple in range(number * number, limit, number):
                is_prime[multiple] = False

    # Trả về các số nguyên tố dưới dạng tuple
    return tuple(i for i in range(limit) if is_prime[i])

# Tạo tuple P chứa các số nguyên tố nhỏ hơn 1 triệu
P = sieve_of_eratosthenes(1_000_000)

# In ra kết quả
print("Các số nguyên tố nhỏ hơn 1 triệu:")
print(P)
#nguyenkeloi235752021610061
