class Teams:
    countries = []
    with open("country.csv", "r") as g:
        for i in g.readlines():#Looping countries in list and removing new line
            countries.extend(i.strip().split(","))
    def __init__(self, countries = []):
        with open("Nations.csv","r") as f:  #Handling results file in reading mode
            n = len(f.readlines())      
            f.seek(0)
            list_raw = []
            for i in range(n):
                list_raw.extend(f.readline().strip().split(","))
            f.seek(0)                           #Putting cursor at beginning position
            list_refined = list_raw
            # print(list_refined)
            # Putting list in groups as 4 elements
            list_infour = [list_refined[i:i+4] for i in range(len(list_refined)) if i%4==0]  
            print(list_infour)
            # Reading Total countries file 
            countries = []
            with open("country.csv", "r") as g:
                n = len(g.readlines())
                g.seek(0)
                for i in range(n):#Looping countries in list and removing new line
                    countries.extend(g.readline().strip().split())
            dict_secure = {}
            dict_attack = {}
            dict_win = {}
            dict_loss = {}
            dict_draw = {}
            dict_played = {}
            dict_diff = {}
            dict_points = {}
            for i in countries:
                dict_secure[i] = 0
                dict_attack[i] = 0
                dict_win[i] = 0
                dict_loss[i] = 0
                dict_draw[i] = 0
                dict_played[i] = 0
                dict_diff[i] = 0
            for i in list_infour:
                dict_secure[i[0]] += (int(i[1]))
                dict_secure[i[2]] += (int(i[3]))
            print(dict_secure)

            for i in list_infour:
                dict_attack[i[0]] += int(i[3])
                dict_attack[i[2]] += int(i[1])
            print(dict_attack)

            for i in list_infour:
                if(i[1]>i[3]):
                    dict_win[i[0]] += 1
                elif(i[3]>i[1]):
                    dict_win[i[2]] += 1
            print(dict_win)

            for i in list_infour:
                if(i[1]<i[3]):
                    dict_loss[i[0]]+=1
                elif(i[3]<i[1]):
                    dict_loss[i[2]]+=1
            print(dict_loss)

            for i in list_infour:
                if(i[1] == i[3]):
                    dict_draw[i[0]] += 1
                    dict_draw[i[2]] += 1
            print(dict_draw)

            for i in countries:
                dict_played[i] = list_refined.count(i)
            print(dict_played)

            for i in range(0,len(countries)):
                dict_diff[list(dict_secure.keys())[i]] = list(dict_secure.values())[i] - list(dict_attack.values())[i]
            print(dict_diff)

            for i in range(0,len(countries)):
                dict_points[list(dict_secure.keys())[i]] = 3*list(dict_win.values())[i] + list(dict_draw.values())[i]
            print(dict_points)

            # sorted_points = sorted(dict_points.sort())

Team1 = Teams()



        