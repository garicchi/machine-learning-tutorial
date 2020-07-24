import random

NUM = 50

def main():
    
    result = []
    for i, n in enumerate(range(NUM)):
        user_id = random.randint(1000, 5000)
        if i < (NUM / 2):
            is_bot = 'FALSE'
            attack = round(random.uniform(10, 40), 1)
            guard = round(random.uniform(50, 100), 1)
            life = round(random.uniform(100, 400), 1)
        else:
            is_bot = 'TRUE'
            attack = round(random.uniform(30, 80), 1)
            guard = round(random.uniform(40, 60), 1)
            life = round(random.uniform(200, 800), 1)
        result.append([
            user_id, attack, guard, life, is_bot
        ])

    random.shuffle(result)
    print(result)
    header = ['user_id', 'attack', 'guard', 'life', 'is_cheat']
    with open('dataset.csv', 'w') as f:
        f.write(','.join(header) + '\n')
        f.write('\n'.join([','.join([str(y) for y in x]) for x in result]))



if __name__ == '__main__':
    main()
