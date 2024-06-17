def find_wallets(binance_file, wallets_file, result_file):
    with open(binance_file, 'r') as f:
        binance_wallets = set(line.strip().lower() for line in f)

    with open(wallets_file, 'r') as f:
        my_wallets = set(line.strip().lower() for line in f)

    matches = binance_wallets.intersection(my_wallets)

    with open(result_file, 'w') as f:
        for match in matches:
            f.write(match + '\n')

binance_file = 'data/binance_list.txt'
wallets_file = 'wallets.txt'
result_file = 'result.txt'

find_wallets(binance_file, wallets_file, result_file)
