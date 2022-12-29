inputs = [line.rstrip('\n') for line in open("inputs/19.txt")]
from collections import deque
import math
for line in inputs:
    s = line.split(" ")
    bp = int(s[1][:-1])
    oreb, clayb = int(s[6]), int(s[12]) 
    obsb, geob = (int(s[18]), int(s[21])),(int(s[27]), int(s[30]))
    print(bp, oreb, clayb, obsb, geob)

    
    req = {"ore": oreb, "clay": clayb, "obs": obsb, "geo": geob}
    mats = {"ore": 0, "clay": 0, "obs": 0, "geo": 0}
    bots = {"ore": 1, "clay": 0, "obs": 0, "geo": 0}

    q = deque([(mats, bots, 24)])

    geodes = -1

    while q:
        m, b, t = q.popleft()
        # print(t)
        
        if t == 0:
            if m["geo"] > geodes:
                print(m["geo"])
            
            geodes = m["geo"] if m["geo"] > geodes else geodes
            continue
        if t < 0:
            continue
        
        if b["ore"] != 0:
            delta = math.ceil((req["ore"] - m["ore"]) / b["ore"]) if req["ore"] > m["ore"] else 0 
            if t - delta >= 0 and delta > 0:
                mcp, bcp = m.copy(), b.copy()
                mcp["ore"] += (delta * bcp["ore"]) - req["ore"]
                bcp["ore"] += 1
                q.append((mcp, bcp, t-delta))
        
        
        if b["ore"] != 0:
            delta = math.ceil((req["clay"] - m["ore"]) / b["ore"]) if req["clay"] > m["ore"] else 0
            if t - delta >= 0 and delta > 0:
                mcp, bcp = m.copy(), b.copy()
                mcp["ore"] += (delta * bcp["ore"]) - req["clay"]
                bcp["clay"] += 1
                q.append((mcp, bcp, t-delta))
        
        if b["ore"] != 0 and b["clay"] != 0:
            delta1 = math.ceil((req["obs"][0] - m["ore"]) / b["ore"]) if req["obs"][0] > m["ore"] else 0
            delta2 = math.ceil((req["obs"][1] - m["clay"]) / b["clay"]) if req["obs"][1] > m["clay"] else 0
            delta = max(delta1, delta2)
            if t - delta >= 0 and delta > 0:
                mcp, bcp = m.copy(), b.copy()
                mcp["ore"] += (delta * bcp["ore"]) - req["obs"][0]
                mcp["clay"] += (delta * bcp["clay"]) - req["obs"][1]
                bcp["obs"] += 1
                q.append((mcp, bcp, t-delta))
        
        
        if b["ore"] != 0 and b["obs"] != 0:
            delta1 = math.ceil((req["geo"][0] - m["ore"]) / b["ore"]) if req["geo"][0] > m["ore"] else 0 
            delta2 = math.ceil((req["geo"][1] - m["obs"]) / b["obs"]) if req["geo"][1] > m["obs"] else 0
            delta = max(delta1, delta2)
            if t - delta >= 0 and delta > 0:
                mcp, bcp = m.copy(), b.copy()
                mcp["ore"] += (delta * bcp["ore"]) - req["geo"][0]
                mcp["obs"] += (delta * bcp["obs"]) - req["geo"][1]
                bcp["geo"] += 1
                q.append((mcp, bcp, t-delta))
        
        # m["ore"] += t * b["ore"]
        # m["clay"] += t * b["clay"]
        # m["obs"] += t * b["obs"]
        # m["geo"] += t * b["geo"]
        
        # q.append((m, b, 0))
        
        m["ore"] += b["ore"]
        m["clay"] += b["clay"]
        m["obs"] += b["obs"]
        m["geo"] += b["geo"]
        
        q.append((m, b, t-1))
        
        # if mats["ore"] >= req["geo"][0] and mats["obs"] >= req["geo"][1]:
        #     mcp, bcp = m.copy(), b.copy()
        #     mcp["ore"] -= req["geo"][0]
        #     mcp["obs"] -= req["geo"][1]
        #     bcp["geo"] += 1
        #     q.append((mcp, bcp, t-1))
            
        # if mats["ore"] >= req["obs"][0] and mats["clay"] >= req["obs"][1]:
        #     mcp, bcp = m.copy(), b.copy()
        #     mcp["ore"] -= req["obs"][0]
        #     mcp["clay"] -= req["obs"][1]
        #     bcp["obs"] += 1
        #     q.append((mcp, bcp, t-1))
            
        # if mats["ore"] >= req["clay"]:
        #     mcp, bcp = m.copy(), b.copy()
        #     mcp["ore"] -= req["clay"]
        #     bcp["clay"] += 1
        #     q.append((mcp, bcp, t-1))
        
        # if mats["ore"] >= req["ore"]:
        #     mcp, bcp = m.copy(), b.copy()
        #     mcp["ore"] -= req["ore"]
        #     bcp["ore"] += 1
        #     q.append((mcp, bcp, t-1))

    print(geodes)
            
        
        
        
        
        
        
        
        
        
    # for m in range(1,25):
        
    #     update = [0, 0, 0, 0]
        
    #     if ore >= geob[0] and obs >= geob[1]:
    #         ore -= geob[0]
    #         obs -= geob[1]
    #         update[3] = 1
        
    #     if ore >= obsb[0] and clay >= obsb[1]:
    #         ore -= obsb[0]
    #         clay -= obsb[1]
    #         update[2] = 1
        
    #     if ore >= clayb:
    #         ore -= clayb
    #         update[1] = 1
            
    #     if ore >= oreb:
    #         ore -= oreb
    #         update[0] = 1
            
    #     ore += oren
    #     clay += clayn
    #     obs += obsn
    #     geo += geon
        
    #     print(m)
    #     print("material", ore, clay, obs, geo)
    #     print("robot",oren, clayn, obsn, geon)
    #     print()
        
    #     oren, clayn, obsn, geon = oren + update[0], clayn + update[1], obsn + update[2], geon + update[3]
            
        
        

    # print("geodes", geo)


# Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.