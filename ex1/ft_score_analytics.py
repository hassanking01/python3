import sys

list = []
arguments_len = len(sys.argv) - 1
if not arguments_len:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> \
 <score2> ...")
else:
    i = 1
    while i <= arguments_len:
        try:
            list += [int(sys.argv[i])]
        except Exception as e:
            print(e)
        i += 1
    try:
        max_s = max(list)
        min_s = min(list)
        print("Scores processed:", list)
        print("Total players:", len(list))
        print("Total score:", sum(list))
        print("Average score:", sum(list)/(i-1))
        print("High score:", max_s)
        print("Low score:", min_s)
        print("Score range:", max_s - min_s)
    except Exception as e:
        print(e)
